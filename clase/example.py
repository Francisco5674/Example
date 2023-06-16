nombre = "Pancho"
edad = 65
sexo = "hombre"

# control de flujo por edad
if edad <= 18:
    print("eres menor de edad")
elif 18 < edad <= 60:
    print("eres adulto joven")

#  loop 

mylist = [1, 2, 3, 4, 5, 2.0, "hola mundo"]

pancho_hungry = 10

while pancho_hungry > 0:
   print(f"pancho le faltan {pancho_hungry} para estar satisfecho")
   pancho_hungry -= 1
   
def suma(a):
  resultado = 0
  for number in a:
     resultado = resultado + number
  print(resultado)

vector_1 = [1, 2, 3, 4, 5, 2.0]

suma(vector_1)