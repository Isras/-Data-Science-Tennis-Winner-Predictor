import pandas as pd

atual = "database/final.xlsx"

base = pd.read_excel(atual)

#Transformando Surfaces em números
base = base.replace("Hard", 0)
base = base.replace("Clay", 1)
base = base.replace("Grass", 2)
base = base.replace("Carpet", 3)

#Transformando Comments
n = 0
for i in base['Comment'].unique():
    base = base.replace(i, n)
    n += 1

#Transformando round
n = 0
for i in base['Round'].unique():
    base = base.replace(i, n)
    n += 1

#Transformando data
base = base.astype({"Date": str})

for i in base['Date'].unique():
    k = str(i).replace("-","")
    base = base.replace(i, k)

base = base.astype({"Date": int})

#Transformando Winners e Losers em Players
players = list(set(base['Winner'].unique())|set(base['Loser'].unique()))

base['Vencedor'] = base['Winner']
base = base.rename(columns={'Winner':'player1', 'Loser':'player2'})

#Transformando todos em números
for player in players:
    base = base.replace(player, str(players.index(player)))
    with open("jogadores.txt", 'a') as arquivo:
        arquivo.write(f"{player} = {str(players.index(player))}\n")

base = base.astype({"player1": int, "player2": int, "Vencedor": int})

#Salva tudo no excel novo
base.to_excel('dadostratados.xlsx')