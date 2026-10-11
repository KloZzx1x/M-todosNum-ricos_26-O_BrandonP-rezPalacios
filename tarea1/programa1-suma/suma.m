arg_list = argv ();

if length(arg_list) == 2
  num1 = str2double(arg_list{1});
  num2 = str2double(arg_list{2});
else
  printf("Usando valores por defecto:\n");
  num1 = 0.1;
  num2 = 0.2;
endif

resultado = num1 + num2;
printf("Resultado en Octave: %.17g\n", resultado);