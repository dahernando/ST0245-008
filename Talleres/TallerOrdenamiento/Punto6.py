
TuplaDeInventos = [(70,"vision hecha audio"),(80,"Avances de la realidad virtual"),(75,"Rueda Inteligente"),(65,"Satélite con Luz")]
TuplaDeInventos.sort(key=lambda invento: invento[0])
print("Inventos ordenados segun su puntaje")
print(TuplaDeInventos)
print("Inventos ordenados segun el nombre")
TuplaDeInventos.sort(key=lambda invento: invento[1])
print(TuplaDeInventos)

