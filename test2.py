# 1. Llegeix el polinomi des de l'usuari
import math as math
grau = int(input("Introdueix el grau del polinomi:\n "))
coeficients = []

for i in range(grau, -1, -1):
    coef = int(input(f"Introdueix el coeficient de x^{i}: "))
    coeficients.append(coef)

print(f"\nCoeficients llegits: {coeficients}")

# 2. Funció per mostrar el polinomi com a text
def expressio_polinomi(coefs):
    termes = []
    grau = len(coefs) - 1
    for i, coef in enumerate(coefs):
        exp = grau - i
        if coef == 0:
            continue
        signe = ""
        if coef > 0 and i != 0:
            signe = " + "
        elif coef < 0:
            signe = " - "
        valor = abs(coef)
        if exp == 0:
            terme = f"{valor}"
        elif exp == 1:
            terme = f"{valor}x" if valor != 1 else "x"
        else:
            terme = f"{valor}x^{exp}" if valor != 1 else f"x^{exp}"
        termes.append(signe + terme if signe else terme)
    return "".join(termes)

# 3. Funció per calcular f(x)
def f(x):
    resultat = 0
    grau = len(coeficients) - 1
    for i, coef in enumerate(coeficients):
        exp = grau - i
        resultat += coef * (x ** exp)
    return resultat

# 4. Calcular derivada automàticament
def derivada(coefs):
    deriv = []
    grau = len(coefs) - 1
    for i, coef in enumerate(coefs):
        exp = grau - i
        if exp != 0:
            deriv.append(coef * exp)
    return deriv

# 5. Funció per calcular f'(x)
def f_derivada(x):
    resultat = 0
    deriv = derivada(coeficients)
    grau = len(deriv) - 1
    for i, coef in enumerate(deriv):
        exp = grau - i
        resultat += coef * (x ** exp)
    return resultat

# 6. Mostrar les expressions
polinomi = expressio_polinomi(coeficients)
deriv_text = expressio_polinomi(derivada(coeficients))

print(f"\nFunció original:     f(x) = {polinomi}")
print(f"Derivada de f(x):    f'(x) = {deriv_text}")

# 7. Buscar interval on hi ha arrel (Bolzano)
a, b = None, None
for x in range(-100, 100):
    if f(x) * f(x + 1) < 0:
        a, b = x, x + 1
        break

if a is None:
    print("\nNo s'ha trobat cap interval amb arrel.")
    exit()
else:
    print(f"\nInterval amb arrel trobat: [{a}, {b}]")
    print(f"f({a}) = {f(a)}")
    print(f"f({b}) = {f(b)}")

# 8. Newton-Raphson (ús de valor mitjà com a inicial)
x0 = (a + b) / 2
print(f"\n--- Newton-Raphson ---")
print(f"Valor inicial: x0 = {x0}")

tolerancia = 1e-6
max_iteracions = 20
for i in range(max_iteracions):
    fx = f(x0)
    dfx = f_derivada(x0)
    if dfx == 0:
        print("Derivada zero, no es pot continuar.")
        break
    x1 = x0 - fx / dfx
    print(f"Iteració {i+1}: x = {x1}, f(x) = {f(x1)}")
    if abs(x1 - x0) < tolerancia:
        print(f"\nArrel trobada amb precisió: x = {x1}")
        break
    x0 = x1
else:
    print(f"\nNo s'ha aconseguit precisió després de {max_iteracions} iteracions.")
