from flask import *
#import Template
app = Flask(__name__)

@app.route('/admin/')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
   print "Here inside the condition"
      return render_template('res.html')
   else:
      return redirect('logout.html')

if __name__ == '__main__':
   app.run(debug = True)