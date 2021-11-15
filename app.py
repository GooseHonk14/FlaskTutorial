from flask import Flask, render_template, url_for, request, redirect  #install flask, and render_template, which will allow for html files to be read, url_for allows stylesheets to be linked, Request allows for things to be requested from the webpage, redirect allows us to send the user to the updated webpage
from flask_sqlalchemy import SQLAlchemy #import something for databases?
from datetime import datetime #Allows for the date to be imported

app = Flask(__name__) #References this file, so app.py? apparently it always works no matter what so, just run with it?
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  #Tells the app where the database is located. Number of slashes indicated the type of path, sqlite is a database thing? test.db is the database in which everything will be stored
db = SQLAlchemy(app) #Initialize (start pretty much) our database

#Making a model for out database?
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)  #References the id of each entry via integer
    content = db.Column(db.String(200), nullable=False) #What will appear inside of the box
    date_created = db.Column(db.DateTime, default=datetime.utcnow) #Stores the date and time of when the task was created
    #!SET UP DATA BASE (1)

    def __repr__(self):
        return '<Task %s>' % self.id


 
@app.route('/') #Routes something to a webpage so that flask knows where we going. The webpage is specified inside of the ()
def index():  #Immediately put the function you want to run on the opeing of the page
 return "Hello, world! ......"  #The return is what will appear on screen, whether that be a string, HTML code, or another file 

@app.route('/template', methods=['POST', 'GET'])  #Methods tag allows for the website to do more things, in this case POST allows us to send data to the database
def template():
    if request.method == 'POST':  #REQUEST needs an import, remember that
        task_content = request.form['content']  #This is setting a variable equal to what is inputed into the form with id 'content', found in index.html
        new_task = Todo(content=task_content) #Creates a new task variable that is equal to the model we made in class Todo

        try:
            db.session.add(new_task) #Adds new task to the database
            db.session.commit() #Saves the new task to the database
            return redirect('https://5000-purple-mongoose-i5x1ay3m.ws-us18.gitpod.io/template') #Sends the information to the desired webpage, in this case, template
                    #####THIS NEEDS TO BE CHANGED TO MATCH THE CURRENT URL BECAUSE GITPOD SUCKS AND IT REDIRECTS TO LOCALHOST:5000
        except:
            return "There was an issue adding your task."

    else: #This else will always run, since when the tab was originally loaded POST was false, and then after the button was pressed and the TRUE was run, POST will be false again.
        tasks = Todo.query.order_by(Todo.date_created).all()  #This takes all the tasks in the database and orders them by date_created.
                                                     #^The all selector grabs all the things in the database, you could use first and it would only grab the first item and put it into the variable.
        return render_template('index.html', tasks=tasks) #This will render a template on the page. If we didn't name the template folder "templates" i think we would have to specify where this file was coming from, but its just easier to name the folder templates
        #^Put the render template here so that  #Tasks=tasks just updates that into the webpage
        # if nothing is happening, then it will just display the webpage



@app.route('/delete/<int:id>') #Making a new page for deleting things, url with <something> has a variable "something" in it. Since we want the variable to be an integer we put int:id.
def delete(id): #Passing in id from the url
     task_to_delete = Todo.query.get_or_404(id) #Getting something from the database, if it doesn't exist it will 404
     try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('https://5000-purple-mongoose-i5x1ay3m.ws-us18.gitpod.io/template')  
     except:
         return "There was a problem deleting your task."



if __name__ == "__main__": #Tells flask to actually run
    app.run(debug=True) #debug=True will display any errors on the webpage




#run by typing python3 app.py into the terminal 
#Find the running port, make it public, and open it in a new page
#Interestingly enough, it appears as though this makes live changes.
#Typing in the URL in browser wrong results in the ol 404, so don't