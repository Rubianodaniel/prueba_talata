from src import create_app
from src.config import configuration

app = create_app(configuration["development"])


if __name__ == '__main__':
    app.run()
