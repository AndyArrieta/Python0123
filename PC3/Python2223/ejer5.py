##Pregunta 5

##Crear un paquete de programas (módulo) que tenga las siguiente funciones:
#-Una función recursiva de suma de los n primeros números
#-Una función que me permita dividir 2 números.
#-importar esos módulos desde el archivo main.

def sumydiv():
    def nameFile():
            if __name__=='__main__':
                print("\nAPP")
            else:
                print("\nSECUNDARIO")
                
    nameFile()   

    def sumar(n : int  ,repe : int =0 ,RES : int=0):
        if repe <n:
            repe+=1
            RES=RES+repe
            print(RES)
            return sumar(n,repe,RES)
        else:
            print('Resultado: ',RES)
            print('\nFin') 
    #sumar(10)
    def divi(a,b):
        try:
            print('\n<<<DIVISION>>>\n')
            print(f"Dividendo {a} y divisor {b}")
            return print(a/b)
        except Exception as e:
            print(e)
    
    maxi=int(input('\nSumar hasta el numero: '))
    sumar(maxi)
    div=int(input('\nDividendo: '))
    divis=int(input('\nDivisor: '))
    divi(div,divis)
#divi(4,0)

#IMPORTACIÓN EN main.py