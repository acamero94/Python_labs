import numpy as np;

def imprimir_matriz(charar,tamano):
    for i in range(tamano):
        for j in range(tamano):
            print(charar[i][j].decode(), "\t", end='')
        print("\n");

def imprimir_matriz_ex(tamano):
    for i in range(tamano):
        for j in range(tamano):
            msj=str(i)+","+str(j)
            print(msj, "\t", end='')
        print("\n");

def girar_matriz(charar,tamano,sentido):
    n_matriz=np.chararray((tamano,tamano))
    if sentido==2:
        #Antihorario
        auxj = tamano - 1
        for i in range(tamano):
            auxi = tamano - 1
            for j in range(tamano):
                n_matriz[i][auxi]=charar[auxi][auxj]
                auxi-=1
            auxj-=1
    else:
        # Horario
        auxj = tamano - 1
        for i in range(tamano):
            auxi = tamano - 1
            for j in range(tamano):
                n_matriz[i][j] = charar[auxi][i]
                auxi -= 1
            auxj -= 1
    return n_matriz

Rta=int(input("Cipher Turning Grille.\n\n1. Cipher\n2. Decipher\n\nRta: "))

if Rta==1:
    #Cifrar
    #Solicitar Datos
    Texto = input("Please introduce the text to cipher: ");
    Texto1 = Texto
    #Texto="jim attacksatdawn"
    Texto = Texto.upper().strip().replace(" ", "");
    tamano=int(input("Please introduce the reticle size: "))
    #tamano=4
    Reticula = np.chararray((tamano, tamano));
    Reticula[:]="*"


    print("The reticle is compounded by a series of positions of the form i,j from 0 to n-1 being n the size of the reticle, please enter the coordinates i,j you want to drill\n")

    while True:

        print("Enter the position to add the hole\n")
        imprimir_matriz_ex(tamano)
        i=int(input("Position i: "))
        j=int(input("Position j: "))
        Reticula[i][j]="O"
        print("Actual reticle\n")
        imprimir_matriz(Reticula, tamano)

        rta2=int(input("¿Do you want to add another hole?\n1. Si\n2. No\n\nRta: "))
        if rta2==1:
            continue
        else:
            break;

    imprimir_matriz(Reticula, tamano)

    rta2 = int(input("¿In what way do you want to cipher?\n1. Clockwise direction\n2. Counterclockwise direction\n\nRta: "))
    m_res=np.chararray((tamano,tamano));

    aux=0
    for k in range(4):
        for i in range(tamano):
            for j in range(tamano):
                if Reticula[i][j]==b'O':
                    m_res[i][j]=Texto[aux]
                    aux += 1
        Reticula = girar_matriz(Reticula, tamano, rta2)
    print("\nMatrix result\n")
    imprimir_matriz(m_res,tamano)

    print("\nText Cipher:\n")
    for i in range(tamano):
        for j in range(tamano):
            print(m_res[i][j].decode()," ",end="")
        print("\t",end="")
    print("\n")
    print("\nText original: \n")    
    print(Texto1)


else:
    #Descifrar
    # Solicitar Datos
    Texto = input("Please introduce the text to decipher: ");
    #Texto="JKTD SAAT WIAM CNAT"
    Texto = Texto.upper().strip().replace(" ", "");

    tamano = int(input("Please introduce the reticle size: "))
    #tamano=4

    Reticula = np.chararray((tamano, tamano));
    Reticula[:] = "*"


    print("The reticle is compounded by a series of positions of the form i,j from 0 to n-1 being n the size of the reticle, please enter the coordinates i,j you want to drill\n")

    while True:

        print("Enter the position to add the hole\n")
        imprimir_matriz_ex(tamano)
        i = int(input("Position i: "))
        j = int(input("Position j: "))
        Reticula[i][j] = "O"
        print("Actual reticle\n")
        imprimir_matriz(Reticula, tamano)

        rta2 = int(input("¿Do you want to add another hole?\n1. Si\n2. No\n\nRta: "))
        if rta2 == 1:
            continue
        else:
            break;
            """
    Reticula[0][0] = "O"
    Reticula[0][3] = "O"
    Reticula[0][5] = "O"
    Reticula[1][2] = "O"
    Reticula[1][8] = "O"
    Reticula[2][1] = "O"
    Reticula[2][6] = "O"
    Reticula[3][2] = "O"
    Reticula[3][4] = "O"
    Reticula[3][7] = "O"
    Reticula[4][4] = "O"
    Reticula[4][6] = "O"
    Reticula[4][8] = "O"
    Reticula[5][3] = "O"
    Reticula[5][7] = "O"
    Reticula[6][0] = "O"
    Reticula[6][5] = "O"
    Reticula[7][1] = "O"
    Reticula[7][4] = "O"
    Reticula[7][8] = "O"
    Reticula[8][2] = "O"
    """
    

    m_ciph=np.chararray((tamano,tamano))
    aux=0

    for i in range(tamano):
        for j in range(tamano):
            try:
                m_ciph[i][j]=Texto[aux]
                aux+=1
            except:
                m_ciph[i][j]="_"

    print("Reticle\n")
    imprimir_matriz(Reticula, tamano)
    print("\nMatrix the text cipher\n")
    imprimir_matriz(m_ciph, tamano)

    rta2 = int(input("¿In what way do you want to decipher?\n1. Clockwise direction\n2. Counterclockwise direction\n\nRta: "))
    m_res = np.chararray((tamano, tamano));

    Descifrado=""
    for k in range(4):
        for i in range(tamano):
            for j in range(tamano):
                if Reticula[i][j] == b'O':
                    Descifrado+=m_ciph[i][j].decode()
                    #aux += 1
        Reticula = girar_matriz(Reticula, tamano, rta2)
    print("\nText decipher\n",Descifrado)
