#juego de la vida del dia miércoles de laboratorio 21 de mayo
#Pablo Quijivix 1578125

def proxima_generacion(matriz):

    filas=len(matriz)

    colum= len(matriz[0])

    

    new_matriz=[]

    for i in range(filas):

        fila = []

        for j in range(colum):

            fila.append(0)

        new_matriz.append(fila)

   

    for i in range(filas):

        for j in range(colum):

            vecinos= 0

            

            if j > 0:

                if matriz[i][j- 1] == 1:

                    vecinos = vecinos + 1



            if j<colum-1:

                if matriz[i][j+1]==1:

                    vecinos=vecinos+1

            

            

            if matriz[i][j]==1:

                if vecinos==1 or vecinos==2:

                    new_matriz[i][j]=1

                else:

                    new_matriz[i][j]=0

            else:

                if vecinos==1:

                    new_matriz[i][j]=1

                else:

                    new_matriz[i][j]=0



    return new_matriz



def imprimir_tablero(matriz):

    for i in range(len(matriz)):

        for j in range(len(matriz[i])):

            print(matriz[i][j],end=" ")

        print()



matriz = [

    [0,0,0,0,0,1,1,0,0,0],

    [0,1,1,0,0,0,0,0,0,0],

    [0,1,0,0,0,1,1,0,0,0],

    [0,0,0,0,0,0,0,0,0,0],

    [0,0,0,0,0,0,0,0,0,0],

    [0,0,1,1,0,0,0,0,0,0],

    [0,0,1,0,0,0,0,0,0,0],

    [0,0,0,0,0,0,0,0,0,0],

    [0,0,1,0,0,0,0,0,1,0],

    [0,0,0,0,0,0,0,0,0,0],

]



print("Generación 0:")

imprimir_tablero(matriz)



gen_1 = proxima_generacion(matriz)

print("\nGeneración 1:")

imprimir_tablero(gen_1)



gen_2 = proxima_generacion(gen_1)

print("\nGeneración 2:")

imprimir_tablero(gen_2)            

                
