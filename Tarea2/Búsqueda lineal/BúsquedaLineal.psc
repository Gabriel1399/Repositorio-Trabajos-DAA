Proceso BúsquedaLineal
	
	dimensionArreglo = 6
	numeroBuscar = 10
	exito <- Falso
	Definir posicion Como Entero
	i <-1
	Dimension arr[dimensionArreglo]  
	arr[1] =10
	arr[2] = 30
	arr[3] = 35
	arr[4] = 44
	arr[5] = 67
	arr[6] = 88
	
	Mientras no exito y i < dimensionArreglo Hacer
		Si numeroBuscar = arr[i] Entonces
			encontro <- Verdadero
			posicion <- i
		FinSi
		i <- i+1
	FinMientras
	
	Si encontro Entonces
		Escribir "El dato a buscar se encuentra en la posición ", posicion, " del arreglo"
	Sino
		Escribir "El dato a buscar no se encuentra en el arreglo"	
	FinSi
	
	
FinProceso