# Define opciones de supervivencia
reglas ={
 "A": {
  (0,0,0): 0,
  (0,0,1): 1,
  (0,1,0): 1,
  (0,1,1): 1,
  (1,0,0): 1,
  (1,0,1): 0,
  (1,1,0): 0,
  (1,1,1): 0
 },
  "B": {
  (0,0,0): 0,
  (0,0,1): 0,
  (0,1,0): 1,
  (0,1,1): 1,
  (1,0,0): 1,
  (1,0,1): 0,
  (1,1,0): 0,
  (1,1,1): 0
 },
 "C": {
  (0,0,0): 0,
  (0,0,1): 1,
  (0,1,0): 1,
  (0,1,1): 1,
  (1,0,0): 0,
  (1,0,1): 1,
  (1,1,0): 1,
  (1,1,1): 0
 },
 "D": {
  (0,0,0): 0,
  (0,0,1): 1,
  (0,1,0): 1,
  (0,1,1): 1,
  (1,0,0): 0,
  (1,0,1): 1,
  (1,1,0): 1,
  (1,1,1): 0
 },
 "E": {
  (0,0,0): 0,
  (0,0,1): 1,
  (0,1,0): 1,
  (0,1,1): 0,
  (1,0,0): 1,
  (1,0,1): 1,
  (1,1,0): 0,
  (1,1,1): 1
 },
 "F": {
  (0,0,0): 0,
  (0,0,1): 1,
  (0,1,0): 1,
  (0,1,1): 0,
  (1,0,0): 1,
  (1,0,1): 1,
  (1,1,0): 0,
  (1,1,1): 0
 },}

# Comprueba si cada celula sobrevive por pulso
def evaluar (regla, universo, pulso, celula):
	
	# Revision de pulso anterior
	izq = universo[pulso][celula-1]
	med = universo[pulso][celula]
	der = universo[pulso][celula+1]
	indice = (izq, med, der)
	
	# Decide si celula vive o muere
	estado = reglas[regla][indice]
	#print(indice)
	return estado

# Muestra en pantalla la evolucion de las celulas por pulsos
def imprimir(universo, numCelulas, numPulsos):
    for pulso in range(numPulsos+1):
        nuevoPulso = ""
        for celula in range(numCelulas):
            if (universo[pulso][celula]==1):
                universo[pulso][celula] = '█ '
            if (universo[pulso][celula]==0):
                universo[pulso][celula] = '░ '
            nuevoPulso += str(universo[pulso][celula])
        print(nuevoPulso)
        print("\n")

# Crea pulsos nuevos con base en las reglas
def evolucionar(numPulsos, numCelulas, regla, universo, pulso, celula):
        for pulso in range(numPulsos):
            nuevoPulso = []
            nuevoPulso.append(0)
            for celula in range(1,numCelulas-1):				
                nuevaCelula = evaluar(regla, universo, pulso, celula)
                nuevoPulso.append(nuevaCelula)
            nuevoPulso.append(0)
            universo.append(nuevoPulso)

# Ejecuta el Juego	
def juegoDeLaVida1D(nC, nP, r):
	
	# Parametros de entrada
	numCelulas= nC
	numPulsos = nP
	regla = r

	# Inicializacion Normalizacion
	universo=[]
	pulso=[]
	if (numCelulas%2==0):
		numCelulas = numCelulas + 1
	medioUniverso = numCelulas//2
	for celula in range(numCelulas):
		if (celula==medioUniverso):
			pulso.append(1)
		else:
		   pulso.append(0)
	universo.append(pulso)

    # Evolucionar la célula
	evolucionar(numPulsos, numCelulas, regla, universo, pulso, celula)

	# Mostrar resultados
	imprimir(universo, numCelulas, numPulsos)

# Ejecuta el juego para todas las reglas
def principal():
    modelos = ["A", "B", "C", "D", "E", "F"]
    for m in modelos:
        juegoDeLaVida1D(21,6,m)
        print("\n")

principal()
