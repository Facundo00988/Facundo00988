print("-------Bienvenido al programa------------")
print("	Nuevas cosas implementadas ")
print("[Mejoras]|[Arreglos]")
#///////////////////////////////////////////////
def Carga_Eventos(eventos):
	semanas=['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
	print("Ingrese [fin] para finalizar terminar la ejecucion...")
	name_event=input("Ingrese el nombre del evento:").lower()
	while name_event != 'fin':
		print("Ingrese a que hora comienza |Por Ejemplo ====>(hh)")
		print("""
		Ejemplos:
		_________________________________________________
		
		HORARIOS QUE PUEDES 
		PONER 
		_________________________________________________
		|	01hs	|	11hs	|	21hs	|
		|	02hs	|	12hs	|	22hs	|
		|	03hs	|	13hs	|	23hs	|
		|	04hs	|	14hs	|	00hs	|
		|	05hs	|	15hs	|		|
		|	06hs	|	16hs	|		|
		|	07hs	|	17hs	|		|
		|	08hs	|	18hs	|		|
		|	09hs	|	19hs	|		|
		|	10hs	|	20hs	|		|
		""")
		hora_inicio=int(input("Ingrese la hora de comienzo:"))
		print("Ingrese a que hora comienza |Por Ejemplo ====>(hh)")
		hora_final=int(input("Ingrese la hora de finalizacion:"))
		print("""---------------------------
		Ingrese un dia de la semanas:
		
		Lunes-Martes-Miercoles-Jueves
		Viernes-Sabados-Domingo
		
		--------------------------------""")
		dia=input("Ingrese un dia de la semana:\n")
		if dia in semanas:
			print("---EVENTO PROGRAMADO---")
			eventos.append([name_event,dia,hora_inicio,hora_final,[]])
		else:
			print("[ERROR] Se han generado un dia inexistente vuelva a intentarlo.")
			dia=input("Ingrese un dia de la semana:\n")
		name_event=input("Ingrese el nombre	del evento:").lower()
	return eventos
#///////////////////////////////////////////////////
def Carga_Personas(eventos):
	print("---Aqui se van a registrar personas para el evento----")
	print("EVENTO PROGRAMADOS2")
	cont=0
	for evento in eventos:
		cont+=1
		print(f"{cont})-Nombre del evento:{evento[0]}- Dia:{evento[1]}- Horario de:{evento[2]}hs|{evento[3]}hs.")
	print("Ingrese un [0] si quiere terminar..")
	opc=int(input("Ingrese un numero de estos eventos para Poder cargar personas..."))
	if opc == 0 or opc > len(eventos):
		print("Opcion no valida... Vuelva a intentarlo")
		opc=int(input("Ingrese un numero de estos para Poder cargar personas..."))
	evento_seleccionado=eventos[opc - 1]
	total=int(input("Cuantas personas desea Cargar:"))
	for x in range(total):
		name=input("Ingrese su nombre:")
		post_name=input("Ingrese su nombre:")
		gmail=input("Ingrese su gmail:")
		evento_seleccionado[4].append([name,post_name,gmail])
	print(".Personas registradas correctamente.")
	return eventos	
#////////////////////////////////////////////////////////
def Mostrar_Personas_Cargadas(eventos):
	print("EVENTOS DISPONIBLES:")
	cont=0
	for evento in eventos:
		cont+=1
		print(f"{cont})- Nombre del evento:{evento[0]}- Dia:{evento[1]}- Hora de inicion{evento[2]}hs|{evento[3]}hs.")
	opc=int(input("Seleccione el numero de evento para ver las personas registradas o [0] para finalizar:"))
	if opc == 0: 
		return eventos 
	if opc < 1 or opc > len(eventos):
		print("Opcion no valida... Seleccione un numero de evento valido")
		return eventos
	evento_seleccionado=eventos[opc - 1]
	for persona in evento_seleccionado[4]:
		print(f"Nombre:{persona[0]} {persona[1]} - Gmail: {persona[2]}")
	return eventos 
#//////////////////////////////////////////////////////////
def Cuantos_Eventos(eventos):
	return len(eventos)
#/////////////////////////////////////////////////////////
def Menu():
	print("""--------- Menu Principal--------------
1) Programar Eventos  
2) Cargar personas al evento
3) Mostrar personas dentro de un evento
4) Cuantos Eventos hay en total
5) Salir 
----------------------------------------
""")
	opcion=int(input("Ingrese una opcion de estas opciones dadas:"))
	return opcion 
eventos=[]
op= Menu()
while op != 5:
	if op == 1:
		
		eventos=Carga_Eventos(eventos)
		print("Eventos Programados")
	elif op == 2:
		Carga_Personas(eventos)
		print("Personas registradas en los eventos")
	elif op == 3:
		Mostrar_Personas_Cargadas(eventos)
	elif op == 4:
		total_eventos=Cuantos_Eventos(eventos)
		print("Total de Eventos Programados:",total_eventos)
	elif op == 5:
		print("Saliendo del Programa.")
		with open('Transferencia_De_Datos.txt','a') as archivo:
			archivo.write("----Datos Cargados hasta ahora....-----")
			archivo.write("Eventos programados:\n")
			for evento in eventos:
				archivo.write(f"Nombre del Evento:{evento[0]} -Dia{evento[1]} - Horario:{evento[2]}hs|{evento[3]}hs.")
				archivo.write("\n-----Personas registrar en cada evento--------\n")
			for evento in eventos:
				archivo.write(f"Personas registradas en el evento:{evento}\n")
				for persona in evento[4]:
					archivo.write(f"Nombre:{persona[0]} {persona[1]} - Gmail {persona[2]}\n")
				archivo.write("\n")
				archivo.close()
	else:
		print("ERROR opcion no valida. Ingrese una opcion del 1 al 5.")
	op= Menu()
print("Programa terminado.")
