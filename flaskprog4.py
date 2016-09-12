from flask import Flask

app = Flask(__name__)


@app.route('/flask4/<name>')

def hello_user(name):
	return 'Hello %s!' % name

if __name__=='__main__':
	app.run(debug = True)
