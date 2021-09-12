class Tablero:
    
    def __init__(self,reng, colum):
        self.__reng = reng
        self.__colum = colum
        self.__array=[[0 for x in range(self.__colum)] for y in range(self.__reng)]

    def toString(self):
        [print("---",end="") for x in range(self.__colum)]
        print("")
        for ren in self.__array:
            print(ren)
        [print("---",end="") for x in range(self.__colum)]
        print("")

    def getNumRen(self):
        return self.__reng

    def getNumCol(self):
        return self.__colum

    def getItem(self,ren,col):
        return self.__array[ren][col]

    def setItem( self , ren , col , valor):
        self.__array[ren][col]=valor

    def clearing(self, valor=0):
        for ren in range(self.__reng):
            for col in range(self.__colum):
                self.__array[ren][col]=valor



class Celula:

	CELULA_VIVA = 1
	CELULA_MUERTA = 0

	def __init__( self , renglones , columnas , generaciones , poblacion):
		self.largo = columnas
		self.alto = renglones
		self.grid = Tablero( self.alto , self.largo )
		self.grid.clearing( self.CELULA_MUERTA )
		self.generaciones = generaciones

		for celula in poblacion:
			self.grid.setItem( celula[0] , celula[1] , self.CELULA_VIVA )
        

	def imprimeGrid( self ):
		for r in range( self.grid.getNumRen() ):
			for c in range( self.grid.getNumCol() ):
				if self.grid.getItem(r,c) == 0:

					print('░░',end='')
				else:
					print('██',end = '')

			print("")
		print("")

	def getNumReng( self ):
		return self.alto

	def getNumColum( self ):	
		return self.largo

	def setCelulaMuerta( self , ren , col):
		self.grid.setItem( ren , col , self.CELULA_MUERTA )	
  
	def setCelulaViva( self , ren , col ):
		self.grid.setItem( ren , col , self.CELULA_VIVA )	

	def getEstaViva( self , ren , col ):
		return self.grid.getItem( ren , col ) == self.CELULA_VIVA

	def getEstaMuerta( self , ren , col ):
		return self.grid.getItem( ren , col ) == self.CELULA_MUERTA

	def getNumeroVecinosVivos( self , ren , col ): 
		vecinosVivos = 0

		for r in [ ren-1 , ren , ren+1 ]:
			for c in [ col-1 , col , col+1 ]:
				try:
					if self.grid.getItem( r , c ) == self.CELULA_VIVA  and ( r , c ) != ( ren , col ):
						vecinosVivos += 1
				except Exception as x:
					pass
					
		return vecinosVivos


	def siguienteGeneracion( self ): 

		for x in range( self.generaciones ):

			self.imprimeGrid()

			celulasVivas = []
			celulasMuertas = []

			for ren in range( self.alto ):

				for col in range( self.largo ):
					if self.getNumeroVecinosVivos( ren , col ) == 3:
						celulasVivas.append(( ren , col ))

					if self.getNumeroVecinosVivos( ren , col ) == 2 :
						pass

					if self.getNumeroVecinosVivos( ren , col ) < 2 or self.getNumeroVecinosVivos( ren , col ) > 3:
						celulasMuertas.append(( ren , col ))	

			for x in celulasMuertas:
				self.setCelulaMuerta( x[0] , x[1] )
	
			for x in celulasVivas:
				self.setCelulaViva( x[0] , x[1] )


pruebaCelula = Celula( 5 , 5 , 10 , [ (1 , 2) , ( 2 , 2 ) , ( 2 , 1) , ( 2 , 3 ) ] )
pruebaCelula.siguienteGeneracion()