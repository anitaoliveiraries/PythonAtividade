import pandas as pd

dados = pd.read_csv("Atividade2.csv")

print("Primeiras linhas da base:")
print(dados.head())

print("\nQuantidade de registros:", dados.shape[0])
print("Quantidade de características:", dados.shape[1])

print("\nCaracterísticas:")
print(dados.columns)

print("\nDados ausentes por característica:")
print(dados.isnull().sum())

# Tratamento dos dados ausentes
# Substituindo os valores ausentes de BMI(IMC) pela média da coluna
dados["bmi"] = dados["bmi"].fillna(dados["bmi"].mean())

print("\nDados ausentes após o tratamento:")
print(dados.isnull().sum())

print("\nDados após o tratamento:")
print(dados.head())