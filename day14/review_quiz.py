from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.metrics import accuracy_score


X,y = load_iris(return_X_y=True)

train_X, test_X, train_y, test_y = train_test_split(X,y,test_size=0.3,random_state=42)

d_model = DecisionTreeClassifier(random_state=42)
b_model = BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=10,
    random_state=42
)

d_model.fit(train_X,train_y)
b_model.fit(train_X,train_y)

pred_d = d_model.predict(test_X)
pred_b = b_model.predict(test_X)

print(accuracy_score(test_y,pred_d))
print(accuracy_score(test_y,pred_b))
