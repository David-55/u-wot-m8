import numpy as np
import imageio
import math
from random import randint

from array import array

#image = imageio.imread("/home/erjomuza/PycharmProjects/untitled/red.jpg")
#print image.mean(axis=0)
#def arrayCuads(z):
#Basicamente le asigna el archivo a una variable.
#filename = open("/home/erjomuza/Downloads/1.mp4", "r")
#ESTO SIRVE PARA VER META DATA SIN EMBARGO PARA LLAMAR UN VIDEO ES MEJOR LA ANTERIOR
#filename = open("/home/erjomuza/Downloads/1.mp4", "r")
#reader = imageio.get_reader(filename, 'ffmpeg')
#Me tira cuantos frames tiene, esto proveniente del metadata
#reader.get_meta_data()['nframes']
#Me tira los frames per second
#reader.get_meta_data()['fps']
#print reader.get_meta_data()
''''for i, im in enumerate(reader):
    print('Mean of frame %i is %1.1f' % (i, im.mean()))'''
#Esto es la definicin de una funcin
def imageVect():
    #Llamo al archivo y lo abro, flag "read"
    filename = open("/home/erjomuza/Downloads/12.divx", "r")
    #Le digo a imageio tome esto e interpretelo con ffmpeg
    reader = imageio.get_reader(filename, 'ffmpeg')
    #variable para saber que tan largo es el archivo, en nuestro caso leeriamos solo un pedazo
    lim = reader.get_meta_data()['nframes']
    #hago un array, de lim columnas y 3 filas cada una
    j = np.ndarray(shape=(lim, 3), dtype=int)
    #For que usa el array j para llenarlo con los valores de la suma de las columnas de cada una de las columnas
    for i in range(0, lim):
        #Estos sum son funciones de numpy, los cuales suma las columnas, las imagenes
        #estan divididas en secciones, pero estas secciones contienen un pixel
        #un pixel se ve de esta forma [Red, Green, Blue]
        j[i] = np.sum(np.sum(reader.get_data(i), axis=0), axis=0)
        # Imprime j, esto es la forma de debug que hago yo
        #print j[i]
        # Parte del debug que se hace, para dividirlo por imagenes
        #print "hola"
    #Devuelva j.
    return j
#A partir de esto voy a llamar a lo demas
def kmean():
    #print c1
    #Centroide 2
    c2 = np.random.random_integers(1000000, high=4000000, size=3)
    #print c2
    #Distancia euclideana

    a=0
    #promedios para utilizar
    promedio1 = 0
    promedio2 = 0
    #Vector de imagenes, llamar solo una vez
    imagenes = imageVect()
    print imagenes
    lim = len(imagenes)
    # Centroide 1
    c1 = imagenes[randint(0, lim)]
    # Centroide 2
    c2 = imagenes[randint(0, lim)]
    print c1
    print c2
    while a==0:
        #Sumas, que van a contener la suma total de las imagenes, para luego promediar y tener nuevos centroides
        #Suficiente espacio en memoria con uint32
        #van a servir para promediar
        s1=1
        s2=1
        hell = euclid(imagenes, c1, c2)
        suma1 = np.ndarray(shape=(1, 3), dtype=int)
        suma2 = np.ndarray(shape=(1, 3), dtype=int)
        for i in range(0, lim):
            if hell[i][2]==0:
                suma1[0][0] += imagenes[i][0]
                suma1[0][1] += imagenes[i][1]
                suma1[0][2] += imagenes[i][2]
                s1=s1+1
            if hell[i][2]==1:
                suma2[0][0] += imagenes[i][0]
                suma2[0][1] += imagenes[i][1]
                suma2[0][2] += imagenes[i][2]
                s2=s2+1
        c1s = np.ndarray(shape=(1, 3), dtype=int)
        c2s = np.ndarray(shape=(1, 3), dtype=int)
        c1s[0][0] = suma1[0][0] / s1
        c1s[0][1] = suma1[0][1] / s1
        c1s[0][2] = suma1[0][2] / s1
        c2s[0][0] = suma2[0][0] / s2
        c2s[0][1] = suma2[0][1] / s2
        c2s[0][2] = suma2[0][2] / s2
        #print suma1
        #print suma2

        '''print "c2"
print c2
print "c1s"
print c1s
print "c2s"
print c2s
print "c1s1"
print c1s[0][0]
print "c10"
print c1[0]'''
        print "iteracion"
        print "modificado"
        print c1s
        print c1

        if c1s[0][0] == c1[0]:
            a=1
        c1[0] = c1s[0][0]
        c1[1] = c1s[0][1]
        c1[2] = c1s[0][2]
        c2[0] = c2s[0][0]
        c2[1] = c2s[0][1]
        c2[2] = c2s[0][2]

def euclid(vect, c1, c2):
    lim = len(vect)
    # Distancia euclideana
    vectDist = np.ndarray(shape=(lim, 3), dtype=int)
    for i in range(0, lim):
        # Este vector se traga las sumas de distancias euclideanas.
        vectDist[i][0] = math.sqrt(
            math.pow((vect[i][0] - c1[0]), 2) + math.pow((vect[i][1] - c1[1]), 2) + math.pow((vect[i][2] - c1[2]), 2))
        vectDist[i][1] = math.sqrt(
            math.pow((vect[i][0] - c2[0]), 2) + math.pow((vect[i][1] - c2[1]), 2) + math.pow((vect[i][2] - c2[2]), 2))
        # La tercera fila del arreglo va a ser la que indique a que
        if (vectDist[i][1] >= vectDist[i][0]):
            vectDist[i][2] = 1
        else:
            vectDist[i][2] = 0
    return vectDist
kmean()
'''t = np.asarray([[[1,1,1],
        [2,2,0],
        [0,3,3]],
        [[1,1,1],
        [0,2,2],
        [0,3,3]],
        [[0,1,1],
        [0,2,2],
        [0,3,3]]])
t[1]=[[0, 0, 0], [0, 0, 0]]
print t[1]'''
#137261871894
#68631791316