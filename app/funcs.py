import pandas as pd
import sklearn

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
            return {'function': sklearn.neighbors.KNeighborsClassifier,
                    'parms': parms}
        case 'logreg':
            parms = [('penalty', ['l1', 'l2', 'none']),
                     ('C', 'float')]
            return {'function': sklearn.linear_model.LogisticRegression,
                    'parms': parms}
    return alg
