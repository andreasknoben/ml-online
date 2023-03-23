import pandas as pd

# Classifiers
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


def data_statistics(filename):
    df = pd.read_csv('uploads/dataset.csv')

    statistics = [{
        "filename": filename,
        "ncols": len(df.columns),
        "nrows": len(df.index)
    }]

    return statistics


def get_algorithm_parms(alg):
    match alg:
        case 'nn':
            parms = [('n_neighbours', 'int')]
            return {'function': KNeighborsClassifier,
                    'funcname': "K-Nearest Neighbours Classifier",
                    'parms': parms}
        
        case 'logreg':
            parms = [('penalty', ['l1', 'l2', 'none']),
                     ('C', 'float')]
            return {'function': LogisticRegression,
                    'funcname': "Logistic Regression",
                    'parms': parms}
        
        case 'svm':
            parms = [('C', 'float'),
                     ('degree', 'int')]
            return {'function': SVC,
                    'funcname': "Support Vector Classifier",
                    'parms': parms}
        
        case 'dt':
            parms = [('max_depth', 'int')]
            return {'function': DecisionTreeClassifier,
                    'funcname': "Decision Tree Classifier",
                    'parms': parms}
        
        case 'rf':
            parms = [('n_estimators', 'int'),
                     ('max_depth', 'int')]
            return {'function': RandomForestClassifier,
                    'funcname': "Random Forest Classifier",
                    'parms': parms}
        
        case _:
            return ValueError()
