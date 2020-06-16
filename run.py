from bottle import route, run, template

@route('/say-hello-to/<name>/')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)
