from flask_frozen import Freezer
from app import app
freezer = Freezer(app)

if __name__ == '__main__':
    app.config.update(FREEZER_RELATIVE_URLS=True)
    freezer.freeze()
