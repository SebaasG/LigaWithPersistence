
import os
import json
import modules.utils.utils as ut
# import Modulos.utils.mensajes as msg
MY_DATABASE = ''

def NewFile(*param):
    with open(MY_DATABASE,"w") as wf:
        json.dump(param[0],wf,indent=4)

def ReadFile():
    with open(MY_DATABASE,"r") as rf:
        return json.load(rf)


def AddData(*params):
    data = list(params)
    try:
        with open(data[0], 'r') as file:
            dataExist = json.load(file)
    except FileNotFoundError:
        dataExist = {}
    
    # Actualiza los datos existentes con los nuevos datos
    dataExist.update(data[1])
    
    with open(params[0], 'w') as file:
        json.dump(dataExist, file, indent=4)


def checkFile(*param):
    data = list(param)
    if(os.path.isfile(MY_DATABASE)):
        if(len(param)):
            data[0].update(ReadFile())
    else:
        if(len(param)):
            NewFile(data[0])

def delData(*param):
    decision = bool(input('Desea borrar la informacion, Presione cualquier tecla para (Si) Enter(No)'))
    if decision:
        data = list(param)
        if ut.validateResponse(msg.msgDelet):
            camperBorrar= data[2].get(data[0]).pop(data[1])
            NewFile(data[2])
    else:
        print('No se elimino la informacion')