# import module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.logistic_model import LogisticRegression
############################ import data #################################
admissions = pd.read_table("D:/Study/Dataquest/Data sets/admissions.csv", sep=',')

# =============================================================================
# # about the data
# gap is  the collage grade range R -> [0, 4]
# gre is  the test score range R -> [200, 800]
# admit is  the boolean value whether candidate admitated or rejected
# =============================================================================

plt.scatter(admissions['gpa'], admissions['admit'], alpha=0.2)

def logistics(x):
    return np.exp(x)/(np.exp(x)+1)

x = np.linspace(-6, 6, 50)
y = logistics(x)

plt.plot(x, y)

# appling logistic regression using sklearn
from sklearn.linear_model import LogisticRegression
logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])
probabilities = logistic_model.predict_proba(admissions['gpa'])
print(probabilities[:,0])
fitted_labels = logistic_model.predict(admissions[['gpa']])

admissions.rename(index=str, columns={"admit":"actual_label"}, inplace=True)
admissions['predicted_label'] = fitted_labels
correct_predictions = admissions[admissions['actual_label'] == admissions['predicted_label']].shape[0]
accuracy = correct_predictions/admissions.shape[0]

# true poistiive
true_positive = admissions[(admissions['actual_label'] == 1) & (admissions['predicted_label'] == 1)].shape[0]
true_negative = admissions[(admissions['actual_label'] == 0) & (admissions['predicted_label'] == 0)].shape[0]
# Sensitivity or True Positive Rate - The proportion of applicants that were correctly admitted
