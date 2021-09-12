class Tablero:
    
    def __init__(self,renglones, columnas):
        self.__renglones = renglones
        self.__columnas = columnas

        self.__array=[[0 for x in range(self.__columnas)] for y in range(self.__renglones)]

    def to_string(self):
        [print("---",end="") for x in range(self.__columnas)]
        print("")
        for reng in self.__array:
            print(reng)
        [print("---",end="") for x in range(self.__columnas)]
        print("")

    def getNumeroRenglones(self):
        return self.__renglones

    def getNumeroColumnas(self):
        return self.__columnas

    def getItem(self,reng,colum):
        return self.__array[reng][colum]

    def setItem( self , reng , colum , valor ):
        self.__array[reng][colum]=valor

    def limpiarTablero(self, valor=0):
        for reng in range(self.__renglones):
            for colum in range(self.__columnas):
                self.__array[reng][colum]=valor


class JuegoDeLaVida:

	CELULA_VIVA = 1
	CELULA_MUERTA = 0

	def __init__( self , rens , cols , generaciones , poblacion ):
		self.largo = cols
		self.alto = rens
		self.grid =Tablero( self.alto , self.largo )
		self.grid.limpiarTablero( self.CELULA_MUERTA )
		self.generaciones = generaciones

		for celula in poblacion:
			self.grid.set_item( celula[0] , celula[1] , self.CELULA_VIVA )
        

	def imprime_grid( self ):
		for r in range( self.grid.get_num_rows() ):
			for c in range( self.grid.get_num_cols() ):
				if self.grid.get_item(r,c) == 0:

					print('░░',end='')
				else:
					print('██',end = '')

			print("")
		print("")

	def get_num_rows( self ):
		return self.alto

	def get_num_cols( self ):	
		return self.largo

	def set_celula_muerta( self , row , col):
		self.grid.set_item( row , col , self.CELULA_MUERTA )	
  
	def set_celula_viva( self , row , col ):
		self.grid.set_item( row , col , self.CELULA_VIVA )	

	def get_is_viva( self , row , col ):
		return self.grid.get_item( row , col ) == self.CELULA_VIVA

	def get_is_muerta( self , row , col ):
		return self.grid.get_item( row , col ) == self.CELULA_MUERTA

	def get_numero_vecinos_vivos( self , row , col ): 
		vecinos_vivos = 0

		for r in [ row-1 , row , row+1 ]:
			for c in [ col-1 , col , col+1 ]:
				try:
					if self.grid.get_item( r , c ) == self.CELULA_VIVA  and ( r , c ) != ( row , col ):
						vecinos_vivos += 1
				except Exception as x:
					pass
					
		return vecinos_vivos


	def evolucionar( self ): 

		for x in range( self.generaciones ):

			self.imprime_grid()

			celulas_vivas = []
			celulas_muertas = []

			for row in range( self.alto ):

				for col in range( self.largo ):
					if self.get_numero_vecinos_vivos( row , col ) == 3:
						celulas_vivas.append(( row , col ))

					if self.get_numero_vecinos_vivos( row , col ) == 2 :
						pass

					if self.get_numero_vecinos_vivos( row , col ) < 2 or self.get_numero_vecinos_vivos( row , col ) > 3:
						celulas_muertas.append(( row , col ))	

			for x in celulas_muertas:
				self.set_celula_muerta( x[0] , x[1] )
	
			for x in celulas_vivas:
				self.set_celula_viva( x[0] , x[1] )


resultado_final = JuegoDeLaVida( 7 , 7 , 10 , [ (1 , 2) , ( 2 , 2 ) , ( 2 , 1) , ( 2 , 3 ) ] )
resultado_final.evolucionar()