# 🧬 Chagas Disease Biomarker Analysis

## How to Navigate this Repository

### Python
Find the.ipynb Jupyter Notebook ,where the project is written.
>/Chagas Disease Analysis/notebook
/ChagasDisease_Biomarker_Analysis.ipynb

src folder contain modules used in ChagasDisease_Biomarker_Analysis.ipynb.

>Chagas Disease Analysis/src

data folder contains the data sets for protein parameters and mtDNA biomarker expression.

>Chagas Disease Analysis/src/data


### R
You can find the same project written in R as a qmd file.
>SIBDS_Chagas_Disease_Biomarkers.qmd

You can also view the R qmd file as a pdf.
>SIBDS Chagas Disease Project.pdf


## 🩸 Overview & Goals

This project develops a **machine learning pipeline** to identify
**diagnostic and prognostic biomarkers** for *Chagas Disease*, a
parasitic infection affecting millions across Latin America and
responsible for roughly **3 million deaths annually**.

Researchers at the **University of Texas Medical Branch** have
identified **12 protein parameters** and **6 mitochondrial DNA (mtDNA)
types** that potentially indicate Chagas infection.
Using these biomarkers, this project builds **logistic regression
models** and applies **cross-validated AUC analysis** to determine which
biomarkers best classify healthy, symptomatic, and asymptomatic
patients.

Our goals are:
-   Determine **which biomarkers can diagnose** Chagas Disease
    (distinguish healthy vs. infected).
    
-   Identify **which biomarkers can predict** symptom severity
    (asymptomatic vs. symptomatic).
    
-   Evaluate **Serum vs. Plasma** biomarker reliability.

-   Provide a **data-driven shortlist of biomarkers** for potential
    diagnostic blood test development.


## 🧠 Research Context

  **NHS**    Normal Healthy Subjects (no Chagas Disease)
  
  **ASYM**   Asymptomatic Subjects (infected, no symptoms)
  
  **SYM**    Symptomatic Subjects (infected with symptoms
  

-   **Subjects:** 42 total
    -   12 NHS
    -   15 ASYM
    -   15 SYM
-   **Biomarkers:**
    -   12 Protein Parameters × 2 Blood Sources (Serum, Plasma) → 24
        total
    -   6 Mitochondrial DNA (mtDNA) types

**Goal:** Identify biomarkers that distinguish between NHS vs. infected
(diagnostic) and SYM vs. ASYM (prognostic).


## 📊 Data Exploration

Each classification (red for asymptomatic, blue for symptomatic and white for normal healthy subjects (control))
These boxplots show each biomarkers expression levels in for each symptom.

<img width="1800" height="1200" alt="image" src="https://github.com/user-attachments/assets/e068817f-26ba-4402-a4cb-0ba25f1b66b9" />
<img width="1800" height="1200" alt="image" src="https://github.com/user-attachments/assets/b46db623-68ef-4eea-b9b9-01507b21bb02" />


## ⚙️ Methodology
 
- Create a dummy variable 'With Chagas' to encompass SYM and ASYM records.
  
For each biomarker:
- Develop a Logisitic Regression model that takes in 42 records and biomarker expression as a continuous feature, and use
  the symptom classification as the categorical target.
- For Logistic Regression models that test for Diagnostic potential use NHS / With Chagas as the target.
- For Logistic Regression models that test for Prognostic potential use SYM / ASYM as the target.
- ROC and AUC Evaluation
- Cross Validation


## 🧩 Results Summary

### 🧪 **Protein Parameters (24 total)**

  **Perfect Diagnostics AUC = 1** :
  Copeptin, PARP1, etOhDG               

  **Strong Diagnostic AUC ≥0.9** :
  Endostatin, HnRNPA1  0.91--0.98

  **Perfect Prognostic AUC = 1** :          
  Myostatin, Copeptin, 1.000
  
  **Strong Prognostic AUC = 0.9**:
  etOhDG               

  **Both Diagnostic & Prognostic** :          
  Copeptin, Endostatin, etOhDG   

  <img width="1197" height="593" alt="image" src="https://github.com/user-attachments/assets/6a33efc6-094a-4a2c-9b77-92e6efe02191" />


🧩 *Serum vs Plasma:* No statistically significant differences detected.

### 🧬 **Mitochondrial DNA (6 biomarkers)**

  Diagnostic AUC: 0.81--0.84 : 
  mtND1, mtATP6
  
  Prognostic AUC: 0.92--1.0 : 
  mtND1, mtND5, mtATP6, mtCOII, mtCytB
  

🧩 *mtATP6* and *mtND1* stand out as the most reliable **dual
biomarkers** (both diagnostic & prognostic).

<img width="1197" height="593" alt="image" src="https://github.com/user-attachments/assets/73b0881a-367f-43fd-9eb4-de19e0a5b1de" />


## 🩺 Key Findings

-   **Most Reliable Diagnostic Biomarkers:**
    -   Copeptin, Myostatin, PARP1 (AUC = 1.0)
-   **Most Reliable Prognostic Biomarkers:**
    -   Myostatin, mtATP6, mtND1
-   **Dual-Purpose Biomarkers (Diagnostic + Prognostic):**
    -   Copeptin, Endostatin, etOhDG, mtATP6, mtND1


## ❓ Research Questions for Geneticists

1.  Why do Serum and Plasma yield similar results --- was this expected
    biologically?
2.  Would a minimal-biomarker test (e.g., 3--5 features) be clinically
    viable?
3.  Are mtDNA-based assays easier or more cost-effective than
    protein-based ones?
4.  Should diagnostic and prognostic biomarkers be **mutually
    exclusive** for clarity in test results?


