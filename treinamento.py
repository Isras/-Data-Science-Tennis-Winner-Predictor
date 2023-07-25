#importando bibliotecas
import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

#importando dataset
dataset = "dadostratados.xlsx"
basepanda = pd.read_excel(dataset)

basepanda['Best of'] = basepanda['Best of'].fillna(1)

#importando biblioteca de regressão logística e separando amostra de treino e teste
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
x = basepanda[['Date', 'Surface', 'Round', 'Best of', 'player1', 'player2', 'Comment', 'Court_type']]
y = basepanda['Vencedor']
x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.01, random_state=1)

#treinando o modelo
logistic_regression = LogisticRegression()
logistic_regression.fit(x_train, y_train)
y_pred = logistic_regression.predict(x_test)

#analisando precisão
print("Precisão:", metrics.accuracy_score(y_test, y_pred))

teste = {'Date':20230724, 'Surface': 0, 'Round': 6, 'Best of': 1, 'player1': 500, 'player2': 1411, 'Comment': 0, 'Court_type': 0}
dft = pd.DataFrame(data = teste, index=[0])
resultado = logistic_regression.predict(dft)
print(resultado)