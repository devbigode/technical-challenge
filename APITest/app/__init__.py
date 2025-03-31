from flask import Flask
from flask_cors import CORS
from app.routes.search import search_route

app = Flask(__name__)

CORS(app)

app.register_blueprint(search_route)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
