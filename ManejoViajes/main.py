import os
from control_viaje import ControlViaje
from paises import Paises
from viaje import Viaje

def limpiar_pantalla():
    os.system('cls')

def main():
    while True:
        print("Manejo de viajes")
        print("1. Ingresar viaje")
        i = input("2. Salir")

        if i == "1":
            control = ControlViaje()
            f_inicio = input("Ingrese la fecha de inicio del viaje (YYYY-MM-DD): ")
            f_final = input("Ingrese la fecha de fin del viaje (YYYY-MM-DD): ")
            presupuesto = input("Ingrese el presupuesto diario: ")
            destino = input("Ingrese el destino: \n1. Colombia \n2. Estados Unidos \n3. Europa\n")
            if destino == "1":
                destino = Paises.COLOMBIA.value
            elif destino == "2":
                destino = Paises.COLOMBIA.estados_unidos
            elif destino == "3":
                destino = Paises.COLOMBIA.europa

            viaje = Viaje(f_inicio, f_final, presupuesto, destino)
            limpiar_pantalla()

            while True:
                print("1. Ingresar gasto")
                print("2. Ver reporte incompleto (solo los dias en los que se hizo un gasto)")
                print("3. Ver reporte completo")
                print("4. Salir")
                i = input("Ingrese la opcion: ")

                if i == "1":
                    fecha = input("Ingrese la fecha del gasto (YYYY-MM-DD): ")
                    valor = input("Ingrese el valor del gasto: ")
                    tipo_pago = input("Ingrese el tipo de pago: \n1. Tarjeta \n2. Efectivo\n")
                    while tipo_pago != "1" and tipo_pago != "2":
                        tipo_pago = input("Ingrese el tipo de pago: \n1. Tarjeta \n2. Efectivo\n")
                    if tipo_pago == "1":
                        tipo_pago = "TARJETA"
                    else:
                        tipo_pago = "EFECTIVO"
                    tipo_gasto = input("Ingrese el tipo de gasto: ")
                    control.registrar_gasto(viaje, fecha, valor, tipo_pago, tipo_gasto)
                elif i == "2":
                    control.generar_reporte_viaje(viaje, False)
                    print("Reporte generado")
                elif i == "3":
                    control.generar_reporte_viaje(viaje, True)
                    print("Reporte generado")
                elif i == "4":
                    break
                limpiar_pantalla()

        elif i == "2":
            print("Adios!")
            break

        limpiar_pantalla()

main()
