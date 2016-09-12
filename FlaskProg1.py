from flask import Flask;
app = Flask(__name__)

@app.route('/addition')
def first():
	a=5
	b=6
	sum=a+b
	return str(sum)

if __name__=='__main__':
	app.run()