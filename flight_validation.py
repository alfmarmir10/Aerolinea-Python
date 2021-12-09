import random

vuelos = ["Berlin", "Budapest", "Telavit", "Tampa", "Hellsinki", "Roma"]
personas = ["Alejandra", "Ramon", "Mercedez"]
ene = ["Berlin", "Tampa", "Roma"]
feb = ["Telavit", "Hellsinki" , "Budapest"]

registered_flights=[]
def validation(names:list, months:list):
  if len(names) != len(months):
    raise ValueError("La cantidad de valores ingresados no es válida.")
  try:
    x = 0
    for el in names:
      total=0
      if x == 0:
        total = 0
      elif x == 1:
        total = 1000
      else: 
        total = 3000

      flight = ""

      randomIndex = round(random.uniform(0, 2))
      
      if months[x] == "ENE":
        flight = ene[randomIndex]
      elif months[x] == "FEB":
        flight = feb[randomIndex]
      else: 
        total = "NO APLICA"
        flight = "NO HAY VUELOS EN EL MES SELECCIONADO."

      flightObj = {
        "name":el,
        "month":months[x],
        "ticket_total": total,
        "flight": flight
      }
      x += 1
      registered_flights.append(flightObj)
    return registered_flights
  except Exception as e:
    print(e)
    
