from flask import Flask, render_template, url_for  #install flask, and render_template, which will allow for html files to be read, url_for allows stylesheets to be linked
from flask_sqlalchemy import SQLAlchemy #import something for databases?

app = Flask(__name__) #References this file, so app.py? apparently it always works no matter what so, just run with it?
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  #Tells the app where the database is located. Number of slashes indicated the type of path, sqlite is a database thing? test.db is the database in which everything will be stored
db = SQLAlchemy(app) #Initialize (start pretty much) our database

#Making a model for out database?
class Todo
 
@app.route('/') #Routes something to a webpage so that flask knows where we going. The webpage is specified inside of the ()
def index():  #Immediately put the function you want to run on the opeing of the page
 return "Hello, world! ......"  #The return is what will appear on screen, whether that be a string, HTML code, or another file 

@app.route('/template')
def template():
    return render_template('index.html') #This will render a template on the page. If we didn't name the template folder "templates" i think we would have to specify where this file was coming from, but its just easier to name the folder templates




if __name__ == "__main__": #Tells flask to actually run
    app.run(debug=True) #debug=True will display any errors on the webpage




#run by typing python3 app.py into the terminal 
#Find the running port, make it public, and open it in a new page
#Interestingly enough, it appears as though this makes live changes.
#Typing in the URL in browser wrong results in the ol 404, so don't