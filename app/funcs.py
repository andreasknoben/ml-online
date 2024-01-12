import pandas as pd

# Classifiers
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split

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
        
def run_classifier(alg_parms,seed):
    data = pd.read_csv('uploads/dataset.csv')

    train, test = train_test_split(data, test_size=0.2, random_state=seed)
    X_train = train.iloc[:, :-1]
    y_train = train.iloc[:, -1]
    X_test = test.iloc[:, :-1]
    y_test = test.iloc[:, -1]

    # check if model has random_state parameter
    if 'random_state' in alg_parms['function']().get_params().keys():
        model = alg_parms['function'](random_state = seed)
    else:
        model = alg_parms['function']()
    print(seed)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)

    results = {"test_accuracy": score}

    return results
