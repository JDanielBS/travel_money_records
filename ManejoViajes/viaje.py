''' Module that contains the class Viaje '''

from datetime import datetime, timedelta
from dia import Dia


class Viaje:
    ''' Class that represents a trip'''

    def __init__(self, fecha_inicio, fecha_final, presupuesto_diario, destino):
        self.__fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        self.__fecha_final = datetime.strptime(fecha_final, '%Y-%m-%d')
        self.__presupuesto_diario = int(presupuesto_diario)
        self.__destino = destino
        self.__dias_viaje = self.crear_dias_viaje(fecha_inicio, fecha_final)

    def crear_dias_viaje(self, dia_inicio, dia_fin):
        """
        Generates a list of all dates between two given dates (including both).

        :param dia_inicio: Start date in format 'YYYY-MM-DD'
        :param dia_fin: End date in format 'YYYY-MM-DD'
        :return: List of Dia type objects
        """
        fecha_inicio = datetime.strptime(dia_inicio, '%Y-%m-%d')
        fecha_fin = datetime.strptime(dia_fin, '%Y-%m-%d')
        lista_dias = []
        fecha_temporal = fecha_inicio

        while fecha_temporal <= fecha_fin:
            lista_dias.append(Dia(fecha_temporal.strftime('%Y-%m-%d'), self.get_presupuesto_diario()))
            fecha_temporal += timedelta(days=1)

        return lista_dias


    def get_dia_en_lista(self, dia) -> Dia:
        '''
        Gets the day from the list of days 
        :param dia: Date in format 'YYYY-MM-DD'
        :return: Dia object
        '''
        return self.__dias_viaje[dia]

    def get_fecha_inicio(self):
        ''' 
        Gets the start date of the trip 
        :return: Start date of the trip
        '''
        return self.__fecha_inicio

    def get_fecha_final(self):
        ''' 
        Gets the end date of the trip 
        :return: End date of the trip
        '''
        return self.__fecha_final

    def get_presupuesto_diario(self):
        '''
        Gets the daily budget for the trip
        :return: Daily budget for the trip
        '''
        return self.__presupuesto_diario

    def get_destino(self):
        '''
        Gets the destination of the trip
        :return: Destination of the trip
        '''
        return self.__destino
