
from src import create_app
from src.config import configuration

#### comando para servir en windows
#### waitress-serve --listen=127.0.0.1:5000 wsgi:app 

app = create_app(configuration["development"])

if __name__ == '__main__':
    app.run()
