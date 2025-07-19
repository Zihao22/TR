import os
os.system("clear") #Per netejar el terminal.

import math as math #Intoduir la llibreria math.

print("Programa per trobar les arrels de les funcions polinòmiques\n")

grau = int(input("Introdueix el grau del polinomi\n"))

coeficients= [] #[] és llista buit.
for i in range (grau,-1,-1): #Desde el grau fins a zero.

    coef = int(input("Introdueix els coeficients\n")) 
    # Variable coef per que el usuari introdueix els coeficients al grau corresponent.
    coeficients.append(coef) 
    #apprens serveix per afegir un element al final.
    #En aquest cas, vol afegir al variable coef que conté tots els elements introduïts per l'usuari.

print(f"Coeficients llegits {coeficients}\n")

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

        valor = abs(coef)
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
        if signe: #si hi ha signe, dons diem que mostri el signe amb el terme
            termes.append(signe + terme)
        else:# si no hi ha signe, doncs només ens mostri el terme.
            termes.append(terme)

    return "".join(termes) #"Join" és juntar els termes.


# Funcio derivada com a expressio escrita

def funció_derivada(coeficients):
    derivada_coefs = []
    grau = len(coeficients) - 1
    for i in range(len(coeficients)):
        coef = coeficients[i]
        exp = grau - i
        if exp != 0:
            derivada_coefs.append(coef * exp)
    return derivada_coefs

coef_derivada = funció_derivada(coeficients)

polinomi = funció_polinòmica(coeficients)
derivada = funció_polinòmica(funció_derivada(coeficients))

print(f"La funció introduïda és: f(x) = {polinomi}")
print(f"La derivada de f(x) és: f'(x) = {derivada}")

#Funcions numèriques per calcular f(x) i f'(x)

def f(x):
    resultat = 0
    grau = len(coeficients) - 1
    for i, coef in enumerate(coeficients):
        exp = grau - i
        resultat += coef * (x ** exp)
    return resultat

def f_derivada(x):
    resultat = 0
    grau = len(coeficients) - 1
    for i, coef in enumerate(coeficients):
        exp = grau - i
        if exp == 0:
            continue
        resultat += coef * exp * (x ** (exp - 1))
    return resultat

# Buscar un interval [a, b] on hi hagi arrel (Teorema de Bolzano)
a = None
b = None
for x in range(-100, 100):
    f1 = f(x)
    f2 = f(x + 1)
    if f1 * f2 < 0:
        a, b = x, x + 1
        break

if a is None:
    print("\nNo s'ha trobat cap interval amb arrel entre -100 i 100.")
else:
    print(f"\nInterval trobat on hi ha arrel: [{a}, {b}]")
    print(f"f({a}) = {f(a)}")
    print(f"f({b}) = {f(b)}")

    #Aplicar Newton-Raphson
    x0 = (a + b) / 2
    print(f"\nValor inicial x0 = {x0}")
    max_iter = 100 #El màxim de nombre de iteració.
    tol = 1e-4  # quant d’aprop volem estar de l’arrel

    for i in range(max_iter):
        fx = f(x0)
        dfx = f_derivada(x0)
        if dfx == 0:
            print("Derivada nul·la. No es pot continuar.")
            break
        x1 = x0 - fx / dfx
        print(f"Iteració {i+1}: x = {x1}")
        if abs(x1 - x0) < tol:
            print(f"\nArrel aproximada trobada: x = {x1:.8f}") #".8f" serveix per que ems mostri 8 decimals.
            break
        x0 = x1
    else:
        print("\nNo s'ha aconseguit trobar una arrel amb la tolerància indicada.")
