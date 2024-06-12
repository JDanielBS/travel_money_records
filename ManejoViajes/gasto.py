''' Module that contains the class Gasto '''

class Gasto:

    ''' Class that represents an expense made by the user '''

    def __init__(self, valor, tipo_pago, tipo_gasto):
        self.__valor = int(valor)
        self.__tipo_pago = tipo_pago
        self.__tipo_gasto = tipo_gasto

    def get_valor(self):
        '''
        Gets the value of the expense 
        :return: Value of the expense
        '''
        return self.__valor

    def get_tipo_pago(self):
        '''
        Gets the payment method 
        :return: Payment method
        '''
        return self.__tipo_pago

    def get_tipo_gasto(self):
        '''Gets the type of expense 
        :return: Type of expense
        '''
        return self.__tipo_gasto
