from flask import Flask

app = Flask(__name__)


@app.route('/123')
def hello():
	return 'new route'
app.add_url_rule('/', '123', 123)

if __name__=='__main__':
	app.run()
