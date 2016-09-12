from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin/')
def admin_info():
	return 'Hello Admin'

@app.route('/guest/<guest>')
def guest_info(guest):
	return 'Hello Guest %s!!!'%guest


@app.route('/user/<name>')
def hello_user(name):
   if name == 'admin':
      return 'hello admin'
   else:
      return 'hello guest'+" "+str(name)

if __name__=='__main__':

	app.run(debug = True)