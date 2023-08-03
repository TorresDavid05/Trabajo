def calcular_fibonacci(n):
    fibonacci = [0, 1]  # Inicializar la secuencia con los dos primeros términos: 0 y 1
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])  # Sumar los dos últimos términos y agregar el resultado a la secuencia
    return fibonacci

def calcular_suma_fibonacci(fibonacci):
    return sum(fibonacci)

if __name__ == "__main__":
    try:
        n = int(input("Ingrese el número de términos de la secuencia de Fibonacci que desea mostrar: "))

        if n < 1:
            print("Por favor, ingrese un número válido (mayor o igual a 1).")
        else:
            fibonacci = calcular_fibonacci(n)
            suma_fibonacci = calcular_suma_fibonacci(fibonacci)

            print("La secuencia de Fibonacci es:")
            print(fibonacci)
            print(f"La suma de los {n} términos de la secuencia de Fibonacci es: {suma_fibonacci}")
    except ValueError:
        print("Por favor, ingrese un número válido.")
