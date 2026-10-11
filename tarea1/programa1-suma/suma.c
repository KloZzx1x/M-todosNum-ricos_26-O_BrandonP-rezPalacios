#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    double num1 = 0.1;
    double num2 = 0.2;

    if (argc == 3) {
        num1 = atof(argv[1]);
        num2 = atof(argv[2]);
    } else {
        printf("Usando valores por defecto:\n");
    }

    double resultado = num1 + num2;
    printf("Resultado en C: %.17g\n", resultado);

    return 0;
}