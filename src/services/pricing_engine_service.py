from src import application

@application.route('/')
def hello():
    return 'Hello World!!!!'
