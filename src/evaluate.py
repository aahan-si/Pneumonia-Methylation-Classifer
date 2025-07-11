import shap
from sklearn.metrics import classification_report, accuracy_score

def evaluate_model(model, x_test, y_test):
    """Evaluate model performance"""
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    
    # SHAP feature importance
    explainer = shap.Explainer(model, x_test)
    shap_values = explainer(x_test)
    shap.summary_plot(shap_values, x_test, show=False)
    
    return accuracy, report