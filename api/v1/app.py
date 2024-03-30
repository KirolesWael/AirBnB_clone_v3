#/usr/bin/python3


from flask import Flask, Blueprint, jsonify
from api.v1.views import app_views 
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_appcontext(code):
    """teardown_appcontext"""
    storage.close()

@app.errorhandler(404)
def page_not_found():
    """"Page not found"""
    status = {"error": "Not found"}
    return jsonify(status), 404
    
if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')))