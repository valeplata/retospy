def es_palindromo(palabra):
    palabra = palabra.lower()
    
    palabra = ''.join(e for e in palabra if e.isalnum())
    
    return palabra == palabra[::-1]

entrada = input("Ingresa una palabra:")

if es_palindromo(entrada):
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")