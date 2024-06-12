''' Module that contains the class Dia '''

class Dia:
    ''' Class that represents a day of the trip '''

    def __init__(self, fecha, presupuesto):
        self.__fecha = fecha
        self.__presupuesto = int(presupuesto)
        self.__gastos = []

    def get_fecha(self):
        ''' 
        Gets the date of the day 
        :return: Date of the day
        '''
        return self.__fecha

    def get_presupuesto(self):
        '''
        Gets the budget for the day 
        :return: Budget for the day
        '''
        return self.__presupuesto

    def get_gastos(self):
        '''
        Gets the expenses of the day 
        :return: Expenses of the day
        '''
        return self.__gastos

    def add_gasto(self, gasto):
        '''
        Adds an expense to the day 
        :param gasto: Expense object
        '''
        self.__presupuesto -= gasto.get_valor()
        self.__gastos.append(gasto)
