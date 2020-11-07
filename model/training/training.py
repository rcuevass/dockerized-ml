# importing libraries
import pandas as pd
import numpy as np
import warnings

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble.gradient_boosting import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pickle

warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore', category=DeprecationWarning)

df = pd.read_csv('../../data/input/diabetestype.csv')

# Dropping the class feature
df.drop("Class", 1, inplace=True)

X = df.drop('Type', 1)
y = df.iloc[:, -1]


def compute_score(clf, X, y, scoring='accuracy'):
    xval = cross_val_score(clf, X, y, cv=10, scoring=scoring)
    return np.mean(xval), np.std(xval)


# instantiate different base models

logreg = LogisticRegression()
logreg_cv = LogisticRegressionCV()
svm = SVC()


# create dictionary
dict_models = {'LR': logreg, 'LRCV': logreg_cv, 'SVM': svm}


for model_name in dict_models.keys():
    model_obj = dict_models[model_name]
    print('Cross-validation of : {0}'.format(model_obj.__class__))
    score = compute_score(clf=model_obj, X=X, y=y, scoring='accuracy')
    print('Algorithm ', model_name)
    print('CV score mean = {0}'.format(score[0]))
    print('CV score std = {0}'.format(score[1]))
    print('========================================')


# Lets try train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)


# Using the random forest algorithm
model = dict_models['LRCV'].fit(X_train, y_train)

# Saving the model with pickle

# save the model to disk
model_name = '../../model/objects/rf_model.pkl'
pickle.dump(model, open(model_name, 'wb'))
print("[INFO]: Finished saving model...")

