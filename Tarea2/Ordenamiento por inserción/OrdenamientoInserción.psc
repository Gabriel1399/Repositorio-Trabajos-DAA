Algoritmo OrdenamientoInserción
	dimensionArreglo = 6
	Dimension arr[dimensionArreglo]  
	arr[1] =88
	arr[2] = 67
	arr[3] = 44
	arr[4] = 35
	arr[5] = 30
	arr[6] = 10
	
	limOrdenados = 0
	Definir indComparacion Como Entero
	Definir numPasada Como Entero
	Para  numPasada <- 1 Hasta dimensionArreglo Hacer
		indComparacion = limOrdenados +1		
		
		Mientras indComparacion > 1 y arr[indComparacion] < arr[indComparacion-1]  Hacer
			aux = arr[indComparacion]
			arr[indComparacion] = arr[indComparacion-1]
			arr[indComparacion-1] = aux
			indComparacion = indComparacion -1
		FinMientras
		limOrdenados = limOrdenados + 1
		
	FinPara
	
	Para x<-1 Hasta dimensionArreglo Hacer
		Escribir arr[x]
	FinPara
	
FinAlgoritmo