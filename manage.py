import os
from flask_script import Manager
from app import blueprint
from app.main import create_app


app = create_app('dev')
app.register_blueprint(blueprint, url_prefix='/api/1')

app.app_context().push()

def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
    #Look up postman test API
    #Look up CORS

app.after_request(add_cors_headers)

manager = Manager(app)

@manager.command
def run():
    app.run()

if __name__ == '__main__':
    manager.run()
