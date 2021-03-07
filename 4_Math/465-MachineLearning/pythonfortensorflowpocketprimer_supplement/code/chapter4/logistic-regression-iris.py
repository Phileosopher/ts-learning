from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

# load the iris datasets
dataset = datasets.load_iris()

# fit a logistic regression model to the data
model = LogisticRegression()
model.fit(dataset.data, dataset.target)
#print(model)

# make predictions
expected = dataset.target
predicted = model.predict(dataset.data)

# summarize the fit of the model
print("classification report:")
print(metrics.classification_report(expected, predicted))
print("confusion matrix:")
print(metrics.confusion_matrix(expected, predicted))

