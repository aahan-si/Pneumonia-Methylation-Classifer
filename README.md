<<<<<<< HEAD
## Code Walkthrough

- `01_preprocessing_and_SMOTE.ipynb`: Loads methylation data, scales values, and applies SMOTE for class balancing.
- `02_feature_selection_RFE_SHAP.ipynb`: Uses Recursive Feature Elimination (RFE) to select CpGs, then interprets feature importance using SHAP.
- `03_model_training_and_results.ipynb`: Trains multiple models (Elastic Net, Random Forest), evaluates performance, and exports top biomarkers.

=======
>>>>>>> 0892bd47e27f1770304137b88c8a22b14a395a9d
# Pneumonia Epigenetic Clock

A machine learning classifier built on CpG methylation data to predict pneumonia presence and time since onset using Elastic Net regression.

<<<<<<< HEAD
## Problem
Pneumonia lacks early, accurate diagnostic tools. DNA methylation offers a powerful avenue for non-invasive prediction.

## Data
=======
##  Problem
Pneumonia lacks early, accurate diagnostic tools. DNA methylation offers a powerful avenue for non-invasive prediction.

##  Data
>>>>>>> 0892bd47e27f1770304137b88c8a22b14a395a9d
- DNA methylation beta values from 126 patients (pneumonia vs. control)
- ~250 CpG sites selected using RFE, SHAP, and biological relevance
- Annotated using UCSC Genome Browser and GREAT

<<<<<<< HEAD
## Methods
=======
##  Methods
>>>>>>> 0892bd47e27f1770304137b88c8a22b14a395a9d
- Preprocessing: StandardScaler, SMOTE for class balancing
- Modeling: Logistic Regression, Random Forest, Elastic Net
- Feature expansion + dimensionality reduction using:
  - Recursive Feature Elimination (RFE)
  - SHAP values
  - Domain-informed gene/CpG annotation

<<<<<<< HEAD
## Results
=======
##  Results
>>>>>>> 0892bd47e27f1770304137b88c8a22b14a395a9d
- **Elastic Net** model achieved:
  - Accuracy: 98%
  - Precision: 98%
  - Recall: 98%
  - F1-score: 98%
- Biomarkers enriched for immune & pulmonary pathways (e.g., **C1QB, SMAD9, LILRB4, EPHB2**)

<<<<<<< HEAD
## Future Work
=======
##  Future Work
>>>>>>> 0892bd47e27f1770304137b88c8a22b14a395a9d
- External cohort validation
- Prototype clinical dashboard
- Add time-dependent infection classification

<<<<<<< HEAD
## Skills & Tools
=======
##  Skills & Tools
>>>>>>> 0892bd47e27f1770304137b88c8a22b14a395a9d
`Python`, `pandas`, `scikit-learn`, `matplotlib`, `SHAP`, `RFE`, `GREAT`, `UCSC Genome Browser`

---

## License
MIT
<<<<<<< HEAD

=======
>>>>>>> 0892bd47e27f1770304137b88c8a22b14a395a9d
