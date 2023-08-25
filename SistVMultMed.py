from datetime import date

def validarEntero(valorE):
  while True:
    try:
      valorEntradaE = int(input(valorE))
      return valorEntradaE
    except ValueError:
      print("\nDebe ingresar únicamente VALORES NUMÉRICOS ENTEROS.\n\n¡Inténtelo nuevamente!")

def validarFlotante(valorF):
  while True:
    try:
      valorEntradaF = float(input(valorF)) 
      return valorEntradaF
    except ValueError:
      print("\nDebe ingresar únicamente VALORES NUMÉRICOS ENTEROS O DECIMALES (Con puntos).\n\n¡Inténtelo nuevamente!")

def validarLetra(valorL):
  while True:
    valorEntradaL = input(valorL)
    confirmacion = valorEntradaL.isalpha()
    if confirmacion == True:
      return valorEntradaL
      break
    if confirmacion == False:
      print("\nDebe ingresar únicamente LETRAS sin espacios,ni números, ni caractéres especiales.\n\n¡Inténtelo nuevamente!")

def validarFecha():
  while True:
    try:
      dia = int(input("\nIngrese el día (en números) en que se realizó la prueba: "))
      mes = int(input("\nIngrese el mes (en números) en que se realizó la prueba: "))
      año = int(input("\nIngrese el año (en números) en que se realizó la prueba: "))
      fechaDate = date(año,mes,dia)
      fechaVal = fechaDate.strftime("%Y/%m/%d")
      return fechaVal
    except ValueError:
      print("\nLos valores que ha ingresado en la fecha no son válidos.\n\nPor favor intente nuevamente...")

class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
    
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.__lista_caninos = {}
        self.__lista_felinos = {}
    
    def verificarExiste(self,historia):
        if historia in self.__lista_caninos or historia in self.__lista_felinos:
            return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verNumeroMascotas(self):
        return len(self.__lista_caninos)+len(self.__lista_felinos)
    
    def ingresarMascota(self,historia,tipo,mascota):
        if tipo == 1: #Felinos
            self.__lista_felinos[historia] = mascota
        if tipo == 2: #Caninos
            self.__lista_caninos[historia] = mascota
   

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for mascotadic in [self.__lista_caninos, self.__lista_felinos]:
            if historia in mascotadic:
                mascota = mascotadic[historia]
                return mascota.verFecha()
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for mascotadic in [self.__lista_caninos, self.__lista_felinos]:
            if historia in mascotadic:
                mascota = mascotadic[historia]
                return mascota.verLista_Medicamentos()
        return None
    
    def eliminarMascota(self, historia):
        for mascotadic in [self.__lista_caninos,self.__lista_felinos]:
            if historia in mascotadic:
                if historia in self.__lista_caninos:
                    self.__lista_caninos.pop(historia)  #opcion con el pop
                elif historia in self.__lista_felinos:
                    self.__lista_felinos.pop(historia)
                return True  #eliminado con exito
        return False 

    def eliminarMedicamentosMascota(self, historia):
            for mascotadic in [self.__lista_caninos, self.__lista_felinos]:
                if historia in mascotadic:
                    mascota = mascotadic[historia]
                    medicamentos_asignados = mascota.verLista_Medicamentos()
                    if medicamentos_asignados:
                        mascota.asignarLista_Medicamentos([])  # Eliminar la lista de medicamentos asignados
                        print(f"Se han eliminado todos los medicamentos asignados a la mascota con historia '{historia}'.")
                        return True
                    else:
                        print(f"No se encontraron medicamentos asignados a la mascota con historia '{historia}'.")
                        return False
            return False
def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=validarEntero('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Eliminar los medicamentos de una mascota
                       \n7- Salir
                       \nUsted ingresó la opción: ''' )
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=validarEntero("Ingrese la historia clínica de la mascota: ")
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=validarLetra("Ingrese el nombre de la mascota: ")
                while True:
                    tipo=validarEntero("Ingrese: (1) Si es un felino o (2) Si es canino: ")
                    if tipo == 1:
                        tipo = "Felino"
                        t = 1
                        break
                    elif tipo == 2:
                        tipo = "Canino"
                        t = 2
                        break
                    else:
                        print("\nIngrese una opción válida...")

                peso=validarFlotante("Ingrese el peso de la mascota: ")
                fecha=validarFecha()
                nm=validarEntero("Ingrese cantidad de medicamentos: ")
                lista_med=[]
                listapersonal = []
                for i in range(0,nm):
                    nombre_medicamentos = validarLetra("Ingrese el nombre del medicamento: ")
                    if nombre_medicamentos in listapersonal:
                        print("\nNo es posible ingresar el mismo medicamento dos veces...Intente ingresarlos nuevamente...")
                        continue
                    listapersonal.append(nombre_medicamentos)
                    dosis = validarEntero("Ingrese la dosis: ")
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(historia,t,mas)

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = validarEntero("Ingrese la historia clínica de la mascota: ")
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = validarEntero("Ingrese la historia clínica de la mascota: ")
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = validarEntero("Ingrese la historia clínica de la mascota: ")
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")

        elif menu==6:
            histE = validarEntero("Ingrese la historia clínica de la mascota: ")
            resultado_operacion = servicio_hospitalario.eliminarMedicamentosMascota(histE)

        elif menu==7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

