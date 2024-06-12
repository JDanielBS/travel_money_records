''' Module to get currency conversion values from different countries '''

from enum import Enum
import logging
import requests

class Paises(Enum):
    ''' Class to get currency conversion values from different countries '''

    COLOMBIA = 1

    @staticmethod
    def obtener_valor_desde_api():
        '''
        Gets a random value between 3500 and 4500 from the API
        :return: random value between 3500 and 4500
        :except: requests.exceptions.HTTPError, requests.exceptions.RequestException, 
                 ValueError, KeyError
        '''

        url = "https://csrng.net/csrng/csrng.php?min=3500&max=4500"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            if isinstance(data, list) and len(data) > 0:
                return data[0]['random']
            else:
                logging.warning("La respuesta no contiene los datos esperados")
                return None
        except requests.exceptions.HTTPError as http_err:
            logging.error("Error HTTP: %s", http_err)
            return None
        except requests.exceptions.RequestException as req_err:
            logging.error("Error de solicitud: %s", req_err)
            return None
        except ValueError:
            logging.error("Error al analizar la respuesta JSON")
            return None
        except KeyError:
            return None

    @property
    def estados_unidos(self):
        '''
        Estados Unidos currency value 
        :return: Estados Unidos currency value if its not None, otherwise 0
        '''
        valor = Paises.obtener_valor_desde_api()
        if valor is not None:
            return valor
        return 0

    @property
    def europa(self):
        '''
        Europa currency value 
        :return: Europa currency value if its not None, otherwise 0
        '''
        valor = Paises.obtener_valor_desde_api()
        if valor is not None:
            return valor + 200
        return 0
