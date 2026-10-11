def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Entrada inválida. Por favor, escriba un número.")

def calculadora():
    while True:
        print("\n--- Calculadora Básica ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = input("Elija una opción (1-5): ")
        
        if opcion == '5':
            print("Saliendo de la calculadora...")
            break
            
        if opcion not in ['1', '2', '3', '4']:
            print("Opción inválida. Intente de nuevo.")
            continue
            
        num1 = pedir_numero("Ingrese el primer número: ")
        num2 = pedir_numero("Ingrese el segundo número: ")
        
        if opcion == '1':
            print(f"Resultado: {num1 + num2}")
        elif opcion == '2':
            print(f"Resultado: {num1 - num2}")
        elif opcion == '3':
            print(f"Resultado: {num1 * num2}")
        elif opcion == '4':
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
            else:
                print(f"Resultado: {num1 / num2}")

if __name__ == "__main__":
    calculadora()