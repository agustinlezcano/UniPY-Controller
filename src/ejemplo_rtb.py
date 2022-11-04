import glob
import serial
import serial.tools.list_ports
import numpy as np
from spatialmath import SE3
import roboticstoolbox as rtb
#Lectura del puerto serial
#puerto = glob.glob('COM*')

puerto = serial.tools.list_ports.comports()
#puerto = serial.Serial.tools.list_ports.comports()
print(puerto)
#, desc, hwid
indice_puerto =input("Número de Puerto: ")
for port in sorted(puerto):
        print("{}".format(port))
        com = str(port).split(" ")[0]
        if com == "COM"+indice_puerto:
            arduino = serial.Serial(com)
            #arduino = serial.Serial(puerto[int (indice_puerto)-1])
print("OK")     #Hasta acá anda bien
puma = rtb.models.DH.Puma560()
#La medida del SE3 es en metros
t = np.arange(0, 2, 0.010)
T0 = SE3(0.6, -0.5, 0.0)
#T1 = SE3(0.4, 0.5, 0.2)
while True:
    texto = arduino.readline()
    texto = texto.decode("ascii")
    textoViejo = "999999999"
    #Esperar un tiempo y si no se actualiza (o son iguales los dos ultimos) dejarlo para el T1
    #definir Time aca 
    if len(texto)>0 and (texto[0]==":"):
        if (texto != textoViejo): 
            print("texto: ",texto)   
            #Convierto la entrada en espacio 3 (decodificar primero)
            T1 = SE3(int(texto[1:4]), int(texto[4:7]), int(texto[7:10])) #Se lee texto[inicio:fin]
            T0 = T1
            textoViejo = texto  
            #Evaluar Jtraj
            #Ts = rtb.tools.trajectory.ctraj(T0, T1, len(t))
            #print(len(Ts))
            #sol = puma.ikine_LM(Ts)       # named tuple of arrays
            #print(sol.q.shape)
            #print(sol.q[1]) #Así se muestran las posiciones de Numpy.ndarray
#Enviar cada posición por TCP/IP al sdk

    #Guardar el último valor de la posición para actualizar
    
    #T1 lo actualizo en un While, viene de Arduino



