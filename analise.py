import pandas as pd

dados = pd.read_csv("Atividade2.csv")
pd.set_option("display.float_format", "{:.2f}".format)

# filtro
sem_avc = dados[dados["stroke"] == 0]
com_avc = dados[dados["stroke"] == 1]


print("Pacientes sem AVC:", len(sem_avc))
print("Pacientes com AVC:", len(com_avc))


print("\nIDADE MÉDIA")
print("Sem AVC:", round(sem_avc["age"].mean()))
print("Com AVC:", round(com_avc["age"].mean()))


print("\nHIPERTENSÃO")

print("Sem AVC:")
print(sem_avc["hypertension"].value_counts())

print("\nCom AVC:")
print(com_avc["hypertension"].value_counts())


print("\nDOENÇA CARDÍACA")

print("Sem AVC:")
print(sem_avc["heart_disease"].value_counts())

print("\nCom AVC:")
print(com_avc["heart_disease"].value_counts())


print("\nGLICOSE MÉDIA")

print(f"Sem AVC:", round(sem_avc["avg_glucose_level"].mean()))
print(f"Com AVC:", round(com_avc["avg_glucose_level"].mean()))


print("\nIMC MÉDIO")

print(f"Sem AVC:", round(sem_avc["bmi"].mean()))
print(f"Com AVC:", round(com_avc["bmi"].mean()))


print("\nTABAGISMO")

print("Sem AVC:")
print(sem_avc["smoking_status"].value_counts())

print("\nCom AVC:")
print(com_avc["smoking_status"].value_counts())


# Agrupamento conforme as características informadas
# Separa os dados em grupos de acordo com o valor da coluna stroke (filtro)

print("\nMÉDIAS POR GRUPO DE AVC")
print(
    dados.groupby("stroke")[
        ["age", "hypertension", "heart_disease",
         "avg_glucose_level", "bmi"]
    ].mean().round(0).to_string()
)