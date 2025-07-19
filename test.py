import os
os.system("clear") #Per netejar el terminal.

import math as math #Intoduir la llibreria math.

#Que el usuari introdueix un interval.
#El input serveix per obtenir dades introduits per el usuari.
a = int(input("introdueix un valor a de l'interval\n") )
#Definim el valiable a que es rep al valor que introduix el usuari.
# La barra \n serveix per un slat de línia.

print(f"El valor a és {a}")

b = int (input ("introdueix un valor b de l'interval\n"))
print (f"El valor b és {b}")

print(f"L'interval és {a,b} ")

grau = int(input("Introdueix el grau del polinomi\n"))

coeficients= [] #[] és llista buit.
for i in range (grau,-1,-1): #Desde el grau fins a zero.

    coef = int(input("Introdueix els coeficients\n")) 
    # Variable coef per que el usuari introdueix els coeficients al grau corresponent.
    coeficients.append(coef) 
    #apprens serveix per afegir un element al final.
    #En aquest cas, vol afegir al variable coef que conté tots els elements introduïts per l'usuari.

print(f"Coeficients llegits {coeficients}\n")

def funcio_polinomica(coeficients): # definim una funció amb def i els variables.
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


polinomi = funcio_polinomica (coeficients) # Ara posem el variable polinomi per mostrar la funció
print(f"La funció introduït és f(x) = {polinomi}")

#Substituïr la funció pels valors de l'interval.
def substitució_polinomi(coeficients, x):
    resultat=0
    grau =len(coeficients) -1
    for i, coef in enumerate(coeficients):
        exp = grau-i
        resultat += coef * (x ** exp) 
        #"+= vol dir sumar i guardar el resultat en el mateix variable" que també podem escreiure com resultat = resultat + coef * (x ** exp)


    return resultat

f_a = substitució_polinomi(coeficients, a)
f_b = substitució_polinomi(coeficients, b)
  
print(f"f({a})={f_a}")
print(f"f({b})={f_b}")

if f_a * f_b > 0:
    print("El teorema de Bolzano no es compleix. No hi ha arrel en aquest interval")
elif f_a * f_b < 0:
    print("El teorema de Bolzano si es compleix.Si hi ha arrel en l'interval donat")