import pandas as pd

# Classifiers
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression


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
    return alg
