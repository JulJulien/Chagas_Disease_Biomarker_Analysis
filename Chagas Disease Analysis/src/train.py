import sklearn
import pandas as pd
import numpy as np
import plotnine
from plotnine import (  # I miss R
    ggplot, aes, geom_line, geom_abline, labs,geom_boxplot, facet_wrap, theme, scale_fill_manual)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, roc_curve, auc
from sklearn.model_selection import StratifiedKFold
from plotnine import *


def setup():
  global protein_parameters
  protein_parameters = ["Copeptin_Serum","Endostatin_Serum","HnRNPA1_Serum","Myostatin_Serum",	"PARP1_Serum", "etOhDG_Serum",
                      "Copeptin_Plasma","Endostatin_Plasma","HnRNPA1_Plasma","Myostatin_Plasma","PARP1_Plasma","etOhDG_Plasma"]
  global mtDNA_biomarkers
  mtDNA_biomarkers = ["mtND1","mtND5","mtATP6","mtCOII","mtCytB"]
  global def_temp
  def_temp = []
  global roc_all
  roc_all = []
  global roc_df
  roc_df = []


def chagasLogReg(dataframe, outcome, biomarker):

    y = dataframe[outcome]
    x = dataframe[[biomarker]]

    # Train logistic regression
    model = LogisticRegression(penalty='l2', C=1e42, solver='liblinear')
    model.fit(x, y)

    # Predict probabilities
    preds = model.predict_proba(x)[:, 1]

    # ROC + AUC
    fpr, tpr, threshold = roc_curve(y, preds)
    roc_auc = auc(fpr, tpr)

    # Data Frame to Save ROC data for this protein
    df_temp = pd.DataFrame({
        'FPR': fpr,
        'TPR': tpr,
        'Biomarker': f'{biomarker} (AUC={roc_auc:.2f})'
    })
    roc_all.append(df_temp)
    return roc_auc


def print_ROC(dataframe, column_predictor, graph_title):
  # Combine all ROC data
  dataframe= pd.concat(roc_all, ignore_index=True)

  # Single facet_wrap plot
  plot = (
      ggplot(dataframe, aes(x='FPR', y='TPR'))
      + geom_line(color='blue')
      + geom_abline(linetype='dashed', color='gray')
      + facet_wrap(column_predictor, ncol=4)  # 3x4 grid
      + labs(
          title= graph_title,
          x='False Positive Rate',
          y='True Positive Rate'
      )
      + theme(figure_size=[9,6]))

  display(plot)

def chagasLogReg_CV(dataframe, outcome, biomarker, n_splits=5):
    """
    Perform stratified K-fold logistic regression for a single biomarker.
    Returns mean AUC ± std.
    """
    X = dataframe[[biomarker]]
    y = dataframe[outcome]

    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)

    aucs = []
    global roc_all
    fold = 1

    for train_idx, test_idx in skf.split(X, y):
        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

        model = LogisticRegression(penalty='l2', C=1e42, solver='liblinear')
        model.fit(X_train, y_train)
        preds = model.predict_proba(X_test)[:, 1]

        fpr, tpr, _ = roc_curve(y_test, preds)
        fold_auc = auc(fpr, tpr)
        aucs.append(fold_auc)

        roc_all.append(pd.DataFrame({
            'FPR': fpr,
            'TPR': tpr,
            'Fold': fold,
            'Biomarker': biomarker,
            'AUC': fold_auc
        }))
        fold += 1

    mean_auc = np.mean(aucs)
    std_auc = np.std(aucs)
    return mean_auc, std_auc
