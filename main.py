"""
vuelos = ["Berlin", "Budapest", "Telavit", "Tampa", "Hellsinki", "Roma"]
personas = ["Alejandra", "Ramon", "Mercedez"]
enero = ["Berlin", Tampa", "Roma"]
febrero = ["Telavit", "Hellsinki" , "Budapest"]

Escribe un programa que reciba como input el nombre de una persona en la lista
personas y un mes del año
Ten en cuenta que en la Aerolinea Viva solo salen vuelos los dos primeros meses del año
donde dan un descuenta inimaginable del 100%
pero solo se lo dan a la primer persona en comprar el tiquete en el día
la segunda persona debera pagar 1000 dolares
y la tercera 3000 dolares
el programa debe retornar  una lista de diccionarios con el nombre de la persona, el valor de su tiquete,
y uno de los destinos que salgan en el mes indicado

"""

from flight_validation import validation

name = input("""
Ingresa los nombres separados por un guión (-), por favor
""")

print("Bienvendo "+name+".")
flightMonth = input("""
¿En qué mes deseas volar? Ingresa los meses separados por un guión (-), por favor
ENE,FEB,MAR,ABR,MAY,JUN,JUL,AGO,SEP,OCT,NOV,DIC
""")

print(".................................")

namesToArray = name.split("-");
flightsMonthsToArray = flightMonth.split("-");

registeredFlights = validation(namesToArray, flightsMonthsToArray)

for el in registeredFlights:
  print(f"""
    Persona {registeredFlights.index(el)+1}:
      Nombre: {el["name"]}
      Mes: {el["month"]}
      Total: {el["ticket_total"]}
      Destino: {el["flight"]}
  """)