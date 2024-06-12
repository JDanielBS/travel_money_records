''' Test module for the viaje and gasto modules '''

from unittest import TestCase
from ManejoViajes.paises import Paises
from ManejoViajes.control_viaje import ControlViaje
from ManejoViajes.viaje import Viaje
from ManejoViajes.excepciones import GastoException

class TestGastos(TestCase):
    ''' Test class for viaje and gasto '''

    def test_adicionar_gastos_generar_reporte(self):
        ''' Test to add expenses and generate a report '''
        control = ControlViaje()
        viaje = Viaje("2024-6-11", "2024-7-11", 2000, Paises.COLOMBIA.estados_unidos)
        control.registrar_gasto(viaje, "2024-6-20", 200, "TARJETA", "Alimentacion")
        control.registrar_gasto(viaje, "2024-6-20", 500, "TARJETA", "Alojamiento")
        control.registrar_gasto(viaje, "2024-7-11", 200, "EFECTIVO", "Alimentacion")
        control.generar_reporte_viaje(viaje, False)

    def test_adicionar_gastos_mayores_generar_reporte(self):
        ''' Test to add a expense greater than the daily budget and generate a report '''
        control = ControlViaje()
        viaje = Viaje("2024-6-11", "2024-7-11", 2000000, Paises.COLOMBIA.value)
        control.registrar_gasto(viaje, "2024-6-20", 2000000, "TARJETA", "Alimentacion")
        control.registrar_gasto(viaje, "2024-6-20", 1500000, "TARJETA", "Alojamiento")
        control.registrar_gasto(viaje, "2024-7-11", 2000000, "EFECTIVO", "Alimentacion")
        control.generar_reporte_viaje(viaje, False)

    def test_adicionar_gasto_fecha_fuera_limites(self):
        ''' Test to add an expense with a date off limits '''
        control = ControlViaje()
        viaje = Viaje("2024-6-11", "2024-7-11", 2000, Paises.COLOMBIA.estados_unidos)
        with self.assertRaises(GastoException):
            control.registrar_gasto(viaje, "2024-7-15", 200, "EFECTIVO", "Alimentacion")
