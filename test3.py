
import numpy as np #Importar la llibreria numpy per a càlcul numèric.
import math as math


while True: # Bucle per repetir el programa.
    print("Programa per trobar les arrels de les funcions polinòmiques\n")
    # Demanar al usuari el grau del polinomi i els coeficients.
    while True: # Bucle per assegurar que l'usuari introdueix un grau vàlid.
        try:
            grau = int(input(f"Introdueix el grau del polinomi (ha de ser un enter positiu):\n"))
            if grau < 0:
                raise ValueError(f"El grau ha de ser un enter positiu.")# valueError per assegurar que el grau és positiu.
            break
        except ValueError as e:# Capturar l'error si el valor no és un enter positiu.
            print(f"Error: {e}. Torna-ho a intentar.")
    print(f"El grau del polinomi és {grau}") # Mostrar el grau del polinomi.
    coeficients= [] #[] és llista buit. 
    for i in range (grau,-1,-1): # Bucle per demanar els coeficients des del grau més alt fins al grau 0.
        while True: # Bucle per assegurar que l'usuari introdueix un coeficient vàlid.
            try: # Intentar convertir l'entrada a enter.
                coef = int(input("Introdueix els coeficients (ha de ser un enter):\n")) # Demanar el coeficient.
                break 
            except ValueError: # Capturar l'error si el valor no és un enter.
                print(f"Error: El coeficient ha de ser un enter. Torna-ho a intentar.") # Missatge d'error.
        coeficients.append(coef)# Afegir el coeficient a la llista de coeficients.
        #append() serveix per afegir elements a una llista.
    print(f"Coeficients llegits {coeficients}\n") # Mostrar els coeficients llegits.

    def funció_polinòmica(coeficients): # definim una funció amb def i els variables.
        termes= [] 
        grau = len(coeficients) -1 
    #len() severix per saber quants elements hi ha en la llista.
    #Posem al final -1, perquè el grau del polinomi és de més gran a més petit.
        for i, coef in enumerate(coeficients): # 'enumerate' ens permet recórrer la llista i obtenir a la vegada la posició (índex) i el valor de cada element
            coef=coeficients[i]
            exp = grau -i

            if coef == 0:
                continue #Fa que no posi el terme de grau o.

            signe ="" #string buit. Vol dir que si no cal posar signe, es deixa buit, com ara el primer terme del polinomi.
            if coef > 0 and i != 0:
             #Si els coeficients es més gran que 0 i la "i" diferencia de 0, doncs el signe es positiu.
             #La diferencia de 0, significa que no és el primer terme.
                signe= " + "
            elif coef < 0: #Si els coeficients són més petit de 0, doncs és negatiu.
                signe= " - " 
                
            valor = abs(coef)# abs() ens dona el valor absolut del coeficient, per tal de no mostrar el signe negatiu al terme.
            if exp== 0:
                terme = f"{valor}"
            elif exp == 1:
                if valor==1:
                    terme="x"
                else: 
                    terme = f"{valor}x"
            else:
                if valor==1:
                    terme= f"x^{exp}"
                else:
                    terme = f"{valor}x^{exp}"

        # Afegir el terme amb el signe.
            if signe: #si hi ha signe, doncs diem que mostri el signe amb el terme
                termes.append(signe + terme)
            else:# si no hi ha signe, doncs diem que només ens mostri el terme.
                termes.append(terme)

        return "".join(termes) #"join" és juntar els termes.


    # Funcio derivada com a expressió escrita
    def funció_derivada(coeficients):
        derivada_coefs = [] # Llista per emmagatzemar els coeficients de la derivada.
        grau = len(coeficients) - 1 # El grau del polinomi és el nombre d'elements menys 1.
        for i in range(len(coeficients)): # Recorrer els coeficients del polinomi.
            coef = coeficients[i] # Obtenir el coeficient actual.
            exp = grau - i # Calcular l'exponent del terme actual.
            if exp != 0: #Si l'exponent és 0, el terme no contribueix a la derivada.
                derivada_coefs.append(coef * exp) # Calcular el coeficient de la derivada.
        return derivada_coefs

    coef_derivada = funció_derivada(coeficients)

    polinomi = funció_polinòmica(coeficients)
    derivada = funció_polinòmica(funció_derivada(coeficients))

    print(f"La funció introduïda és: f(x) = {polinomi}")
    print(f"La derivada de f(x) és: f'(x) = {derivada}")

    #Funcions numèriques per calcular f(x) i f'(x)

    def f(x):# Funció per calcular el valor del polinomi en un punt x.
        resultat = 0
        grau = len(coeficients) - 1
        for i, coef in enumerate(coeficients):
            exp = grau - i
            resultat += coef * (x ** exp)
        return resultat

    def f_derivada(x):# Funció per calcular el valor de la derivada del polinomi en un punt x.
        resultat = 0
        grau = len(coeficients) - 1
        for i, coef in enumerate(coeficients):
            exp = grau - i
            if exp == 0:
             continue
            resultat += coef * exp * (x ** (exp - 1))
        return resultat

    # Buscar un interval [a, b] on hi hagi arrel (Teorema de Bolzano)
    a = None # Inicialitzem a i b a None per si no trobem cap interval.
    b = None
    arrel_exacte = None # Inicialitzem arrel_exacte a None per si no trobem cap arrel exacta.
    for x in range(-100, 100): #Busquem un interval on hi hagi arrel entre -100 i 100.
        f1 = f(x)# Valor de la funció en x.
        f2 = f(x + 1)# Valor de la funció en x + 1.
        if f1 == 0: # Si f(x) és 0, hem trobat una arrel exacta.
            arrel_exacte = x
            print(f"\nArrel exacta trobada: x = {arrel_exacte}")
            break
        elif f2 == 0: # Si f(x + 1) és 0, hem trobat una arrel exacta.
            arrel_exacte = x + 1
            print(f"\nArrel exacta trobada: x = {arrel_exacte}")
            a = b = arrel_exacte
            break
        elif f1 * f2 < 0:# Si el producte és negatiu, hi ha un canvi de signe i per tant hi ha una arrel.
            a, b = x, x + 1 
            break

    if arrel_exacte is not None: # Si hem trobat una arrel exacta, no cal continuar buscant.
        print(f"\nArrel exacta trobada: x = {arrel_exacte}")
        a = b = arrel_exacte
        print(f"f({a}) = {f(a)}")
        print(f"f({b}) = {f(b)}")

    elif a is not None and b is not None: # Si hem trobat un interval on hi ha arrel.
        print(f"\nInterval trobat on hi ha arrel: [{a}, {b}]")
        print(f"f({a}) = {f(a)}")
        print(f"f({b}) = {f(b)}")

        #Aplicar Newton-Raphson
        x0 = (a + b) / 2 # Punt inicial per al mètode de Newton-Raphson.
        print(f"\nValor inicial x0 = {x0}")
        max_iter = 100 #El màxim de nombre de iteració.
        tol = 1e-8 # Tolerància per a la convergència del mètode de Newton-Raphson.


        for i in range(max_iter): # Bucle per a les iteracions del mètode de Newton-Raphson.
            fx = f(x0) # Calcular el valor de la funció en x0.
            dfx = f_derivada(x0) # Calcular el valor de la derivada en x0.
            if dfx == 0:  # Si la derivada és 0, no podem continuar amb el mètode de Newton-Raphson.
                print("Derivada nul·la. No es pot continuar.")
                break
            x1 = x0 - fx / dfx # Calcular el nou valor de x utilitzant la fórmula de Newton-Raphson.
            print(f"Iteració {i+1}: x = {x1}") # Mostrar el valor de x en cada iteració.
            if abs(x1 - x0) < tol: # Si la diferència entre x1 i x0 és menor que la tolerància, hem trobat una arrel.
                print(f"\nArrel aproximada trobada: x = {x1:.10f}") #".10f" serveix per que ems mostri 10 decimals.
                fx1 = f(x1)
                print(f"f({x1:.10f}) = {fx1:.10f}")
                break
            x0 = x1 

    else:
        print("\nNo s'ha trobat cap interval on hi hagi arrel.")

    # Preguntar a l'usuari si vol provar amb una altra funció.
    resposta = input("\nVols provar amb una altra funció? (s/n): ")
    if resposta.lower() != 's':# Si la resposta no és 's', sortim del bucle.
        print("Fi del programa.")
        break


    