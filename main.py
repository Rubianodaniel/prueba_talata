from src import create_app
from src.config import configuration

""" para probar la app en modo development cambie el valor de configuracion
por development o testing"""

app = create_app(configuration["production"])


if __name__ == '__main__':
    app.run()
