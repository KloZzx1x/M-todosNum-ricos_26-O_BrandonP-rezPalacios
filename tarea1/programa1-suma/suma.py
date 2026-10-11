import sys

def sumar(num1=0.1, num2=0.2):
    resultado = num1 + num2
    print(f"Resultado en Python: {resultado:.17g}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            n1 = float(sys.argv[1])
            n2 = float(sys.argv[2])
            sumar(n1, n2)
        except ValueError:
            print("Por favor, ingrese números válidos.")
    else:
        print("Usando valores por defecto:")
        sumar()