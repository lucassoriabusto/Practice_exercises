def fibonacci(n):
    lista_numero = []
    for i in range(n):
        if len(lista_numero) <= 1:  
            lista_numero.append(i) 
        else:
            suma = lista_numero[-1] + lista_numero[-2]
            lista_numero.append(suma)
    print(lista_numero)

n = int(input(f"¿Cuántos números de la secuencia de Fibonacci deseas ver?: "))    
fibonacci(n)