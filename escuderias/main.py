from Escuderia import Escuderia

escuderias=[]

contador=1

numeroEscuderias=int(input('digite el numero de escuderias: '))

while contador <=  numeroEscuderias:
   contador = contador + 1
   escuderia = Escuderia()

   print(f'OTRA ESCUDERIA')
   escuderia.nombre=input("digite nombre de la escuderia: ")
   escuderia.casaMotor=input("digite nombre de la  casa Motor: ")
   escuderia.pilotoPrincipal.nombre=input("digite nombre del primer piloto: ")
   escuderia.pilotoPrincipal.salarioAnual=input(f"digite el salario de {escuderia.pilotoPrincipal.nombre}: ")
   escuderia.pilotoPrincipal.fechaNacimiento=input(f"digita la fecha de nacimiento de {escuderia.pilotoPrincipal.nombre}: ")
   escuderia.pilotoPrincipal.pais=input(f"digite el pais de {escuderia.pilotoPrincipal.nombre}: ")
   escuderia.piloto2.nombre=input("digite nombre del segundo piloto: ")
   escuderia.piloto2.salarioAnual=input(f"digite salario de {escuderia.piloto2.nombre}:")
   escuderia.piloto2.fechaNacimiento=input(f"digite fecha de nacimiento de {escuderia.piloto2.nombre}:")
   escuderia.piloto2.pais=input(f"digite pais de {escuderia.piloto2.nombre}:")
   escuderia.costos=int(input(f"digite valor de los costos de {escuderia.nombre}:"))
   
   escuderias.append(escuderia)
   
#RECORRIENDO LA LISTA DE ESCUDERIA
for escuderia in escuderias:   
   costoMayor = escuderia.costo
   nombreEscuderiaMasCara = None
   
   if escuderia.costos > costoMayor:
      costoMayor=escuderia.costos
      nombreEscuderiaMasCara=escuderia.nombre

      print(f'La escuderia {escuderia.nombre} tiene costos mas elevados: {escuderia.costos}')

