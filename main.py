
from src import create_app
from src.config import configuration

app = create_app(configuration["production"])


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=80)
