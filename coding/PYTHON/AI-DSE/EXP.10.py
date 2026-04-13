import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
# Load the Glass dataset
df = pd.read_csv('glass.csv')
X = df.drop('Type', axis=1)
y = df['Type']
# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Decision Tree
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)
print("Decision Tree Accuracy:", accuracy_score(y_test, dt_pred))
# SVM with Linear Kernel
svm_linear = SVC(kernel='linear', random_state=42)
svm_linear.fit(X_train, y_train)
linear_pred = svm_linear.predict(X_test)
print("SVM (Linear Kernel) Accuracy:", accuracy_score(y_test, linear_pred))
# SVM with Polynomial Kernel
svm_poly = SVC(kernel='poly', degree=3, random_state=42)
svm_poly.fit(X_train, y_train)
poly_pred = svm_poly.predict(X_test)
print("SVM (Polynomial Kernel) Accuracy:", accuracy_score(y_test, poly_pred))
# SVM with RBF Kernel
svm_rbf = SVC(kernel='rbf', random_state=42)
svm_rbf.fit(X_train, y_train)
rbf_pred = svm_rbf.predict(X_test)
print("SVM (RBF Kernel) Accuracy:", accuracy_score(y_test, rbf_pred)
