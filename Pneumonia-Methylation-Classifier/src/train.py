from sklearn.linear_model import LogisticRegressionCV

def train_model(x_train, y_train):
    """Train pneumonia prediction model"""
    model = LogisticRegressionCV(
        cv=5,
        penalty='elasticnet',
        solver='saga',
        l1_ratios=[0.1, 0.5, 0.9],
        scoring='f1',
        max_iter=5000,
        n_jobs=-1
    )
    model.fit(x_train, y_train)
    return model