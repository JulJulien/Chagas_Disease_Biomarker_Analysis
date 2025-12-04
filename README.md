# 🧬 Chagas Disease Biomarker Analysis

## 🩸 Overview

This project develops a **machine learning pipeline** to identify
**diagnostic and prognostic biomarkers** for *Chagas Disease* --- a
parasitic infection affecting millions across Latin America and
responsible for roughly **3 million deaths annually**.

Researchers at the **University of Texas Medical Branch** have
identified **12 protein parameters** and **6 mitochondrial DNA (mtDNA)
types** that potentially indicate Chagas infection.\
Using these biomarkers, this project builds **logistic regression
models** and applies **cross-validated AUC analysis** to determine which
biomarkers best classify healthy, symptomatic, and asymptomatic
patients.

------------------------------------------------------------------------

## 🎯 Objectives

-   Determine **which biomarkers can diagnose** Chagas Disease
    (distinguish healthy vs. infected).\=
-   Identify **which biomarkers can predict** symptom severity
    (asymptomatic vs. symptomatic).\=
-   Evaluate **Serum vs. Plasma** biomarker reliability.
-   Provide a **data-driven shortlist of biomarkers** for potential
    diagnostic blood test development.

------------------------------------------------------------------------

## 🧠 Research Context

  **NHS**    Normal Healthy Subjects (no Chagas Disease)
  **ASYM**   Asymptomatic Subjects (infected, no symptoms)
  **SYM**    Symptomatic Subjects (infected with symptoms)

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

------------------------------------------------------------------------

## 🧩 Results Summary

### 🧪 **Protein Parameters (24 total)**

  **Classification                Examples             Mean AUC**
  **Perfect Diagnostic          Copeptin, PARP1,     1.000
  (AUC=1.0)**                   etOhDG               

  **Strong Diagnostic           Endostatin, HnRNPA1  0.91--0.98
  (AUC≥0.9)**                                        

  **Perfect Prognostic          Myostatin, Copeptin, 1.000
  (AUC=1.0)**                   etOhDG               

  **Both Diagnostic +           Copeptin,            ≥0.9
  Prognostic**                  Endostatin, etOhDG   

🧩 *Serum vs Plasma:* No statistically significant differences detected.

### 🧬 **Mitochondrial DNA (6 biomarkers)**

  **Classification        Biomarkers             Mean AUC**
  **Diagnostic**        mtND1, mtATP6          0.81--0.84
  **Prognostic**        mtND1, mtND5, mtATP6   0.92--1.0
  **Not Significant**   mtCOII, mtCytB         \<0.6

🧩 *mtATP6* and *mtND1* stand out as the most reliable **dual
biomarkers** (both diagnostic & prognostic).

------------------------------------------------------------------------

## 📈 Visualization Highlights

-   **Boxplots:** Biomarker distribution by symptom group
-   **Lollipop plots:** ROC--AUC per biomarker
-   **Barplots:** Diagnostic vs. Prognostic classification categories
-   **Comparative charts:** Serum vs Plasma, Protein vs mtDNA

------------------------------------------------------------------------

## 🩺 Key Findings

-   **Most Reliable Diagnostic Biomarkers:**
    -   Copeptin, Myostatin, PARP1 (AUC = 1.0)
-   **Most Reliable Prognostic Biomarkers:**
    -   Myostatin, mtATP6, mtND1
-   **Dual-Purpose Biomarkers (Diagnostic + Prognostic):**
    -   Copeptin, Endostatin, etOhDG, mtATP6, mtND1

------------------------------------------------------------------------

## ❓ Research Questions for Geneticists

1.  Why do Serum and Plasma yield similar results --- was this expected
    biologically?
2.  Would a minimal-biomarker test (e.g., 3--5 features) be clinically
    viable?
3.  Are mtDNA-based assays easier or more cost-effective than
    protein-based ones?
4.  Should diagnostic and prognostic biomarkers be **mutually
    exclusive** for clarity in test results?

------------------------------------------------------------------------

