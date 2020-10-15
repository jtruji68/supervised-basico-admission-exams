from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler as sc
import pickle
import numpy as np
import pandas as pd


def clasificador(examen1,examen2,clf):
    #creacion de df con las notas 
    df_info = pd.DataFrame(columns = ['examen 1', 'examen 2'])
    row = {'examen 1': examen1,'examen 2':examen2}
    df_info =df_info.append(row,ignore_index=True)

    #transformacion de los datos en la df
    data_array = sc.transform(df_info.values)
    transfo_df = pd.DataFrame(data_array,index = df_info.index, columns = df_info.columns)

    #prediccion
    test= list(transfo_df.iloc[0])
    res = clf.predict([test])[0]
    
    mostrar_resultado(res,examen1,examen2)
    
def mostrar_resultado(res,examen1,examen2):
    #resultado
    mens = {0:'No aprueba',1:'aprueba'}
    print(f'El estudiante tiene las siguientes notas:\nExamen 1: {examen1}\nExamen 2: {examen2}')
    print(f'Razon por la cual el estudiante {mens[res]}')
    
    
def main():
    clf = pickle.load(open('model/Modelo_svc.sav', 'rb'))
    while True:
        examen1 = np.float(input('Ingrese la nota del examen 1: '))
        examen2 = np.float(input('Ingrese la nota del examen 2: '))
        clasificador(examen1,examen2,clf)

        opc = int(input('Ingrese 1 para coninuar, otro carácter para salir: '))
        if opc!=1:
            print('Adiós')
            break
        
if __name__ == "__main__":
    main()