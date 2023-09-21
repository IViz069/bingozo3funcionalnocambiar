from PIL import Image , ImageDraw , ImageFont
from random import randrange
from datetime import datetime
import random
import os
import sys

##### VALIDACION DE ENTRADA DEL PARAMETRO DE NUMERO DE BINGOS #####
if len(sys.argv) > 1:
    
    if sys.argv[1].isdigit() or sys.argv[1].isnumeric():
        numberOfBingosToGenerate = int(sys.argv[1])
        print("GENERANDO BINGOS\n")
    else:
        print("El valor pasado no es un entero.")
        sys.exit()
else:
    print("No se pasó ningún valor en la línea de comandos.")
    sys.exit()

##### FUNCIONES DE UTILIDAD #####
def print_matrix(matrix):
    for x in range(5):
        print(str(matrix[x]))

def guardar_matriz_en_archivo(archivo, matriz, numero_bingo):
    archivo.write(f"bingo{numero_bingo:03}\n\n")
    archivo.write("B\tI\tN\tG\tO\n\n")
    for fila in matriz:
        fila_formateada = [str(x) + "\t" if x != matriz[2][2] else "\t" for x in fila]
        archivo.write("".join(fila_formateada) + "\n")
    archivo.write("-" * 30 + "\n\n")

##### VARIABLES Y ARCHIVOS #####
font = ImageFont.truetype("arial_black.ttf",100)
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y-%H-%M-%S")
os.mkdir('./'+timestampStr)
file = open("./"+timestampStr+"/bingos" + timestampStr + ".txt", "w")

initialHorizontalCoordValue=250#250 is the optimal value
initialVerticalCoordValue=650#250 is the optimal value
increaserHorizontalCoordValue=255
increaserVerticalCoordValue=255
oneDigitNumberHorizontalAdjust = 30

fontColor = (227,107,201)#cambiar este RGB para el cambiar el color de la fuente
centerFontColor = (255,255,0) #color del centro

for c in range(numberOfBingosToGenerate):
    image = Image.open('img/carta.png')

    imageDraw = ImageDraw.Draw(image)
    
    original_matrix = [random.sample(range(i, i + 15), 5) for i in range(1, 76, 15)]
    transposed_matrix = [[fila[i] for fila in original_matrix] for i in range(len(original_matrix[0]))]
    
    print_matrix(transposed_matrix)

    for x in range(5):
        for y in range(5):

            if transposed_matrix[x][y] < 10:
                imageDraw.text((initialHorizontalCoordValue + oneDigitNumberHorizontalAdjust, initialVerticalCoordValue), str(transposed_matrix[x][y]), font=font,fill=fontColor)
            elif x == 2 and y == 2:
                imageDraw.text((initialHorizontalCoordValue, initialVerticalCoordValue), str(""), font=font,fill=centerFontColor)
            else:
                imageDraw.text((initialHorizontalCoordValue, initialVerticalCoordValue), str(transposed_matrix[x][y]), font=font,fill=fontColor)
        
            initialHorizontalCoordValue = initialHorizontalCoordValue + increaserHorizontalCoordValue
        
        initialVerticalCoordValue = initialVerticalCoordValue + increaserVerticalCoordValue
            
        initialHorizontalCoordValue = 250

    initialVerticalCoordValue = 650

    image.save('./'+timestampStr+'/bingo' + str('{:0>3}'.format(c+1))+ '.png')
    
    guardar_matriz_en_archivo(file, transposed_matrix, c+1)

    print("Bingo " + str('{:0>3}'.format(c+1))+ " generado\n")
file.close()