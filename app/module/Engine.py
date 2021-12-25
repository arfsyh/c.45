import pandas as pd
import string
import numpy as np
from sklearn import tree
import pandas as pd
import pydotplus
from IPython.display import Image


def datset(test):
    ds = pd.read_excel('DataTraining.xls')
    datatraining = pd.get_dummies(ds[['G01', 'G02', 'G03', 'G04', 'G05', 'G06', 'G07', 'G08',
                                      'G09', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21']])
    hasil = tree.DecisionTreeClassifier(criterion='entropy')
    hasil_train = hasil.fit(datatraining, ds['Hasil'])
    dot_data = tree.export_graphviz(hasil_train, out_file=None, feature_names=list(datatraining.columns.values),
                                    class_names=['P01', 'P02', 'P03', 'P04', 'P05', 'Tidak Diketahui'], rounded=True, filled=True)
    graph = pydotplus.graph_from_dot_data(dot_data)
    output = graph.write_png("app/static/huja.png")
    predic = hasil_train.predict(test)

    return output, predic


def proses():
    ds = pd.read_excel('DataTraining.xls')
    datatraining = pd.get_dummies(ds[['G01', 'G02', 'G03', 'G04', 'G05', 'G06', 'G07', 'G08',
                                      'G09', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21']])
    hasil = tree.DecisionTreeClassifier(criterion='entropy')
    hasil_train = hasil.fit(datatraining, ds['Hasil'])
    dot_data = tree.export_graphviz(hasil_train, out_file=None, feature_names=list(datatraining.columns.values),
                                    class_names=['P01', 'P02', 'P03', 'P04', 'P05', 'Tidak Diketahui'], rounded=True, filled=True)
    graph = pydotplus.graph_from_dot_data(dot_data)
    output = graph.write_png("app/static/huja.png")

    return output
