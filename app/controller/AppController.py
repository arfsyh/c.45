from flask import request, jsonify
from app import app
from app.module.Engine import datset, proses
import os
from flask import render_template

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from xlrd import open_workbook
from xlutils.copy import copy


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        a = []
        for i in range(1, 22):
            a.append(request.form["g"+str(i)])
        test = []
        for i in range(len(a)):
            if(a[i] == 'ya'):
                test += [0, 1]
            else:
                test += [1, 0]
        hasil = datset([test])[1]
        rb = open_workbook("DataTraining.xls")
        wb = copy(rb)
        s = wb.get_sheet(0)
        ds = pd.read_excel('DataTraining.xls')
        col = len(ds)+1
        for x in range(21):
            s.write(col, x, a[x])
        s.write(col, 21, hasil[0])
        wb.save("DataTraining.xls")

        return render_template('index.html', option=hasil)
    return render_template('index.html', option='')


@app.route('/proses')
def pros():
    proses()
    return render_template('proses.html')
