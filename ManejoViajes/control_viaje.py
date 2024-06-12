''' Module that contains the class ControlViaje '''

from datetime import datetime
import json
import logging
import os
from gasto import Gasto
from excepciones import GastoException

class ControlViaje:
    ''' Class that controls the trip '''

    def registrar_gasto(self, viaje, fecha, valor, tipo_pago, tipo_gasto):
        '''
        Registers an expense in a day of the trip
        :param viaje: Trip object
        :param fecha: Date in format 'YYYY-MM-DD'
        :param valor: Expense value
        :param tipo_pago: Payment method
        :param tipo_gasto: Type of expense
        :except: IndexError
        '''
        fecha = datetime.strptime(fecha, '%Y-%m-%d')
        try:
            if fecha < viaje.get_fecha_inicio() or fecha > viaje.get_fecha_final():
                raise GastoException("La fecha ingresada no corresponde a ninguna fecha del viaje")
            dia = self.buscar_dia_segun_fecha(fecha, viaje)
        except ValueError:
            logging.error("El valor de la fecha no es valido")

        try:
            viaje.get_dia_en_lista(dia).add_gasto(Gasto(valor, tipo_pago, tipo_gasto))
        except IndexError:
            logging.error("La fecha ingresada no corresponde a ninguna fecha del viaje")

    def contar_archivos(self):
        """
        Counts the number of files in a directory

        :param directorio: Route of the directory
        :return: Number of files in the directory
        """
        directorio = "ManejoViajes\Informes"
        try:
            elementos = os.listdir(directorio)
            archivos = [elemento for elemento in elementos if os.path.isfile(os.path.join(directorio, elemento))]
            return len(archivos)
        except FileNotFoundError:
            print(f"El directorio {directorio} no existe.")
            return 0
        except PermissionError:
            print(f"No tienes permisos para acceder al directorio {directorio}.")
            return 0

    def generar_reporte_viaje(self, viaje, completo):
        '''
        Generates a report of the trip
        :param viaje: Trip object
        :param completo: Boolean value to generate a complete report
        :return: None, creates a file that has all the info
        '''
        gasto_tarjeta = 0
        gasto_efectivo = 0
        gasto_total = 0
        gastos_por_dia = []
        duracion = viaje.get_fecha_final() - viaje.get_fecha_inicio()

        for i in range(duracion.days + 1):
            dia = viaje.get_dia_en_lista(i)
            if completo or dia.get_presupuesto() != viaje.get_presupuesto_diario():
                for gasto in dia.get_gastos():
                    gasto_total += gasto.get_valor()
                    if gasto.get_tipo_pago().upper() == "TARJETA":
                        gasto_tarjeta += gasto.get_valor()
                    else:
                        gasto_efectivo += gasto.get_valor()
                gastos_por_dia.append({
                    "dia": i + 1,
                    "fecha": dia.get_fecha(),
                    "presupuesto": dia.get_presupuesto(),
                    "gastos_tarjeta": gasto_tarjeta,
                    "gastos_efectivo": gasto_efectivo
                })
                gasto_tarjeta = 0
                gasto_efectivo = 0
            else:
                continue

        gasto_total = gasto_total * viaje.get_destino()

        datos = {
            "fecha_de_inicio": viaje.get_fecha_inicio(),
            "fecha_de_finalizacion": viaje.get_fecha_final(),
            "presupuesto_diario": viaje.get_presupuesto_diario(),
            "total_dias_de_viaje": duracion.days,
            "gasto_total": gasto_total,
            "gastos_por_dia" : gastos_por_dia
        }

        datos["fecha_de_inicio"] = datos["fecha_de_inicio"].isoformat()
        datos["fecha_de_finalizacion"] = datos["fecha_de_finalizacion"].isoformat()

        ruta_directorio = 'ManejoViajes/Informes'  # Cambia esto a la ruta de tu directorio
        nombre_archivo = 'reporte' + str(self.contar_archivos()) + '.json'
        ruta_completa = os.path.join(ruta_directorio, nombre_archivo)
        os.makedirs(ruta_directorio, exist_ok=True)

        with open(ruta_completa, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)


    def buscar_dia_segun_fecha(self, fecha, viaje):
        '''
        Gets the day according to the date 
        :param fecha: Date in format 'YYYY-MM-DD'
        :param viaje: Trip object
        :return: Number of the day in the list of days
        '''
        diferencia_fechas = fecha - viaje.get_fecha_inicio()
        return diferencia_fechas.days
