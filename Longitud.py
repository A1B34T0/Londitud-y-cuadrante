#Se inicializan variables
cont= 0
temp=0

#Se inicia un ciclo while 
while(cont ==0):
    
    #Se lee una palabra ingresada por el usuario
    palabra = input("Introduce una palabra: ")
    
    #Se guarda la longitud de la palabra en una variable utilizando el metodo len
    temp = len(palabra)
    
    #Si la longitud es menor a 4 se envia el un mensaje indicando que faltan letras
    if(temp<4):
        
        #Si la longitud de la palabra es igual a 1 se envia el primer mensaje
        if(temp==1):
            print(f"Hacen falta letras. Solo tiene {temp} letra")
        
        #Sino se envia el segundo mensaje 
        else:    
            print(f"Hacen falta letras. Solo tiene {temp} letras")
    
    #Si la longitud es mayor a 8 se envia indicando que sobran letras    
    elif (temp>8):
        print(f"Sobran letras. Tiene {temp} letras ")
    
    #Sino se indica que tiene la cantidad correcta de letras    
    else:
        print("Tiene la cantidad de letras correcta")
        
        #Se aumenta el contador en 1
        cont=cont+1
    
