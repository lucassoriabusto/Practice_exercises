abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cifrado_cesar():
    texto = input("Escribe el texto a cifrar: ").lower().strip()
    texto_cifrado = []
    
    for letra in texto:
        if letra in abecedario:
            posicion = abecedario.index(letra)
            nueva_posicion = (posicion + 3) % len(abecedario)
            texto_cifrado.append(abecedario[nueva_posicion])
    
    print("Texto cifrado:", "".join(texto_cifrado))

cifrado_cesar()