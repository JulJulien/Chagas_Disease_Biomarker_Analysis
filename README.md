# Chagas_Disease_Biomarker_Analysis

### How to view this project
- Open the Main Chagas Disease Disease folder
- /notebook contains the main pynb file that shows the full pipeline from EDA -> Model Development -> Model Evaluation -> Visualize Results -> Concluding Findings.
- /src contains modules used for EDA and training data. I decided to used a modular approach since several functions are called multiple times in variations but take up a lot of cell space.
- /data contains the datasets used with permission.

### Project Background
During June-July 2025, I participated in the University of Texas Summer Data Science & Biostatistics Research Internship. This project is statistical anlaysis of me and my parter's (see png) work conducting analysis on a given data set. Originally the project was done in R, but I have 'translated' the work into python.

### Context
Chagas disease, caused by the Trypanosoma cruzi parasite, affects an estimated 3 million people annually, primarily in Latin America. The infection is typically transmitted by blood-feeding insects and, over time, can cause severe cardiac damage leading to cardiomyopathy (heart failure). Currently, there is no reliable diagnostic test or cure for Chagas disease. However, researchers have identified several potential genetic biomarkers that may help detect infection and predict disease progression.

### Goal
The goal of this project is to analyze biomarker data provided by our research team to identify two key types of markers: Diagnostic: genetic data that can distinguish a healthy person from an infected. Prognostic: geneitc data that tells us whether an infected person will develop symptoms.

We will use 42 subject records to predict the categorical outcomes: Healthy, Symptomatic or Asymptomatic. Due to the low amount of records, and multitude of biomarkers needed to be evaluated, we decided to use Logisitic Regression models. Biomarkers that can accurately classify a healthy subject from an infected will be deemed diagnostic. Biomarkers that can accurately classify a symptomatic from asymptomatic will be deemed prognostic.
