import os
from django.core.wsgi import get_wsgi_application
from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask, request, Response
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env'))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asciigenerator.settings')

# Initialize Django
application = get_wsgi_application()

# Create a Flask app and wrap the Django WSGI application
app = Flask(__name__)
app.wsgi_app = ProxyFix(application, x_proto=1, x_host=1)

# Route all requests to the Django WSGI application
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def catch_all(path=""):
    response = Response()
    return app.wsgi_app(request.environ, response.start_response)

if __name__ == '__main__':
    app.run()
