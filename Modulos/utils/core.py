
import os
import json
import Modulos.utils.utils as ut
# import Modulos.utils.mensajes as msg
MY_DATABASE = ''

def NewFile(*param):
    with open(MY_DATABASE,"w") as wf:
        json.dump(param[0],wf,indent=4)

def ReadFile():
    with open(MY_DATABASE,"r") as rf:
        return json.load(rf)

def AddData(*param):
    print(param)
    with open(MY_DATABASE,"r+") as rwf:

        data_file=json.load(rwf)
        if (len(param) > 1):
            try:
                # print(param[0], "dddddd", param[1] )
               
                if(bool(data_file.get(param[0]).update(param[1]))):
                    print("se supone que debe actualizar")
                else: 
                    print("no fue correcto")                
            except AttributeError:
                print("entra al error")
            #     data_file.get(param[0]).update({param[1]:param[2]})
            # data_file.update({param[0]:param[1]})
        else:
            print("entra al else")
            data_file.update({param[0]})

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