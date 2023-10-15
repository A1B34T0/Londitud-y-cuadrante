#Se inicializan las variable cont
cont=0

#Se inicializa una lista
coordenadas= "Eje X","Eje Y","Cuadrante I","Cuadrante II","Cuadrante III","Cuadrante IV"

#Se genera un ciclo while
while cont==0:
    
    #Se inicia un try
    try:
        #Se piden piden los valores de las coordenadas por consola y se almacenan en las variables
        x=int (input("Ingrese la coordenada X: "))
        y=int (input("Ingrese la coordenada Y: "))
    
    #En caso de surgir una excepcion se envia el mensaje de valor invalido   
    except:
        print("Ingrese un valor valido")
    
    #Si ambas coordenadas son igual a 0 se le pide al usuario ingresar otras coordenadas    
    if x==0 and y==0:
        print("Ingrese coordenadas distintas al origen")
    
    else:
        #termina el ciclo
        cont=cont+1
#Si la cooordenada Y es 0 manda la ubicacion correspondiente       
if y==0:
    print (coordenadas[0])
    
#Si la coordenada X es 0 se manda la ubicacion en Y    
elif x==0:
    print(coordenadas[1])
    
#Se manda la ubicacion del cuadrante cuando ambas coordenadas son positivas
elif x>0 and y>0:
    print(coordenadas[2])
    
#Se improme la ubicacion del cuadrante cuando Y es positivo y X negativo
if x<0 and y>0:
    print(coordenadas[3])

#Se improme la ubicacion del cuadrante cuando las coordenadas son negativas
if x<0 and y<0:
    print(coordenadas[4])
    
#Se improme la ubicacion del cuadrante cuando Y es negativo y X positivo
if x>0 and y<0:
    print(coordenadas[5])
