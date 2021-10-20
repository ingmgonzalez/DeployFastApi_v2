# importar librerias de flash 
# from types import MethodDescriptorType
# import joblib
from flask import Flask, request
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return 'Deploy ML'

# Crear funcion para predecir 
@app.route('/predecir', methods=['POST'])
def prediccion():
    json = request.get_json(force=True)
    xin = json['Datos']
    xin = np.asarray(xin)
    xin = xin.reshape(1,13)
    # print("Servicio post")
    yout = model.predict(xin)
    print(yout)
    mensaje = ''
    for y_out in yout:
        mensaje = mensaje + 'El paciente ' + labels[y_out] + ' tiene una enfermedad cardiaca\n'
    
    return mensaje

@app.route('/saludo',methods=['POST'])
def saludo():
    json = request.get_json(force=True)
    nombre = json['nombre']
    apellido = json['apellido']
    return 'Hola ' + nombre + ' ' + apellido


# Cargar modelo
pkl_filename = 'RF_heart_v2.pkl'
with open(pkl_filename, 'rb') as file:
    model = pickle.load(file)
    
labels = ['No', 'SI'] # Etiquetas de datos

if __name__ == '__main__':
    app.run()