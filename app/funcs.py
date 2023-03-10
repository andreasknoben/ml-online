import pandas as pd


def data_statistics(filename):
    df = pd.read_csv('uploads/dataset.csv')

    statistics = [{
        "filename": filename,
        "ncols": len(df.columns),
        "nrows": len(df.index)
    }]

    return statistics