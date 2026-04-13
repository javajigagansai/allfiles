from sklearn.datasets import load_diabetes
from sklearn.linear_model import Lasso, Ridge, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score
diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)
lasso_pred = lasso.predict(X_test)
ridge = Ridge(alpha=0.1)
ridge.fit(X_train, y_train)
ridge_pred = ridge.predict(X_test)
print("Lasso Regression RMSE:", np.sqrt(mean_squared_error(y_test, lasso_pred)))
print("Ridge Regression RMSE:", np.sqrt(mean_squared_error(y_test, ridge_pred)))
y_binary = (diabetes.target > diabetes.target.mean()).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.2, random_state=42)
log_reg = LogisticRegression(penalty='l2', solver='liblinear')
log_reg.fit(X_train, y_train)
log_reg_pred = log_reg.predict(X_test)
accuracy = accuracy_score(y_test, log_reg_pred)
print("Logistic Regression Accuracy:", accuracy)