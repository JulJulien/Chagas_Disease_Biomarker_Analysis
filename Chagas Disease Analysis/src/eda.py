from plotnine import ggplot, aes, geom_boxplot, facet_wrap, labs, theme, scale_fill_manual, theme_bw, scale_y_continuous
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def boxplot(df, biomarker_col, value_col, class_col, title=None, facet_ncol=4, log_y=False):
    """
    Creates a boxplot for any long-format dataset.
    Parameters:
    - df: pandas DataFrame in long format
    - biomarker_col: str, column name containing biomarkers / markers
    - value_col: str, column name containing values
    - class_col: str, column name containing classification ('Sym', 'Asym', 'NHS')
    - title: str, optional plot title
    - facet_ncol: int, number of columns for facet_wrap
    - log_y (bool): whether to log-transform the y-axis
    """
    
    # Ensure classification column is string type
    df[class_col] = df[class_col].astype(str)
    
    p = (
        ggplot(df, aes(x=class_col, y=value_col, fill=class_col))
        + geom_boxplot(outlier_shape='o', outlier_size=2)
        + facet_wrap(f'~{biomarker_col}', ncol=facet_ncol, scales='free_y')
        + labs(title=title, x='', y='Value')
        + theme(figure_size=(9,6))
        + scale_fill_manual(values={'SYM': "blue", 'ASYM': "red", "NHS": "white"})
    )
    
    if log_y:
            p += scale_y_continuous(trans='log10')  # log-transform y-axis

    return p



def biomarker_barplot(
    df: pd.DataFrame,
    biomarker_col: str,
    value_col: str,
    group_col: str,
    classification_col: str,
    title: str = "Biomarker Role Analysis",
    label_order: list = None,
    threshold: float = 0.8
):
    """
    Create side-by-side horizontal barplots comparing biomarker performance across groups.

    Parameters
    ----------
    df : pandas.DataFrame
        The input dataframe containing biomarker, value, group, and classification columns.
    biomarker_col : str
        Name of the column with biomarker identifiers.
    value_col : str
        Name of the numeric column (e.g., AUC).
    group_col : str
        Name of the column defining groups for subplot separation.
    classification_col : str
        Name of the column defining biomarker type (e.g., Diagnostic, Prognostic, Both).
    title : str, optional
        Figure title.
    label_order : list, optional
        Custom order of biomarkers on the y-axis.
    threshold : float, optional
        Vertical reference line value (default = 0.8).
    """

    # Determine unique groups from the data (automatic)
    groups = df[group_col].dropna().unique()

    # Define consistent color palette
    class_colors = {
        'Both': 'purple',
        'Diagnostic': 'red',
        'Prognostic': 'blue',
        'None': '#999999',
        'Not Significant': '#999999'
    }

    # Determine biomarker order if not provided
    if label_order is None:
        label_order = sorted(df[biomarker_col].unique())

    # Create subplots based on number of unique groups
    fig, axes = plt.subplots(1, len(groups), figsize=(14, 7), sharex=True)

    if len(groups) == 1:
        axes = [axes]  # ensure iterable

    # Plot each group
    for ax, group in zip(axes, groups):
        subset = df[df[group_col] == group]

        sns.barplot(
            data=subset,
            x=value_col,
            y=biomarker_col,
            hue=classification_col,
            hue_order=['Both', 'Diagnostic', 'Prognostic', 'Not Significant'],
            palette=class_colors,
            dodge=False,
            order=label_order,
            ax=ax
        )

        ax.axvline(threshold, color='k', linestyle='--', linewidth=1.5)
        ax.set_xlim(0.5, 1.05)
        ax.set_xlabel('AUC', fontsize=12)
        ax.set_ylabel('')
        ax.set_title(group, fontsize=14, fontweight='bold')
        ax.legend_.remove()

    # Shared legend
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, title='Biomarker Role', loc='center right', fontsize=12)

    plt.suptitle(title, fontsize=18, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 0.9, 0.95])
    plt.show()



def lolipop_plot(df, biomarker_col, value_col, group_col, threshold=0.8, title="", label_order_list=None):
    """
    Plots lollipop charts for 'With vs W/o Chagas' and 'Asym vs Sym' groups side-by-side.
    
    Parameters:
        df : pandas.DataFrame
            The dataset containing biomarker values.
        biomarker_col : str
            Column name for the biomarker labels.
        value_col : str
            Column name for the numeric values (e.g., AUC).
        group_col : str
            Column name used to split data into subplots.
        threshold : float
            Threshold to highlight significant biomarkers.
        title : str
            Overall title for the figure.
        label_order_list : list, optional
            Ordered list for biomarker labels on the y-axis.
    """

    # Fixed groups
    expected_groups = ["With vs W/o Chagas", "Asym vs Sym"]
    
    # Prepare subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=False)
    
    # Colors
    colors = {'Diagnostic': '#e31a1c', 'Prognostic': '#1f78b4', 'Not Predictive': '#999999'}

    for ax, group in zip(axes, expected_groups):
        subset = df[df[group_col] == group].copy()
        if subset.empty:
            ax.axis("off")
            ax.set_title(f"No data for {group}", fontsize=12, color='gray')
            continue

        # Apply label order if provided
        if label_order_list is not None:
            subset[biomarker_col] = pd.Categorical(subset[biomarker_col],
                                                   categories=label_order_list,
                                                   ordered=True)
        subset = subset.sort_values(biomarker_col, ascending=False)

        # Highlight logic
        def highlight_row(row):
            if group == 'With vs W/o Chagas':
                if (row[value_col] >= threshold) or (row.get('Diagnostic', 0) == 1):
                    return 'Diagnostic'
            elif group == 'Asym vs Sym':
                if (row[value_col] >= threshold) or (row.get('Prognostic', 0) == 1):
                    return 'Prognostic'
            return 'Not Predictive'
        
        subset['Highlight'] = subset.apply(highlight_row, axis=1)

        # Draw stems
        for _, row in subset.iterrows():
            ax.plot([0, row[value_col]], [row[biomarker_col], row[biomarker_col]],
                    color='lightgray', linewidth=2, zorder=1)

        # Draw dots
        sns.scatterplot(
            data=subset,
            x=value_col,
            y=biomarker_col,
            hue='Highlight',
            palette=colors,
            s=200,
            ax=ax,
            zorder=2
        )

        # Vertical threshold line
        ax.axvline(threshold, color='k', linestyle='--', linewidth=1)
        ax.set_xlim(0.5, 1.05)
        ax.set_xlabel(value_col, fontsize=13)
        ax.set_ylabel('')
        ax.set_yticks(range(len(subset)))
        ax.set_yticklabels(subset[biomarker_col], fontsize=10)
        ax.set_title(group, fontsize=14, fontweight='bold')
        ax.legend_.remove()

    # Shared legend
    handles = [
        plt.Line2D([0],[0], marker='o', color='w', markerfacecolor=colors['Diagnostic'], markersize=10),
        plt.Line2D([0],[0], marker='o', color='w', markerfacecolor=colors['Prognostic'], markersize=10),
        plt.Line2D([0],[0], marker='o', color='w', markerfacecolor=colors['Not Predictive'], markersize=10)
    ]
    labels = ['Diagnostic','Prognostic','Not Predictive']
    fig.legend(handles, labels, loc='center right', fontsize=11, title='Classification')

    plt.suptitle(title, fontsize=16, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 0.88, 0.93])
    plt.show()

