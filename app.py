from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://Devashish:Devashish2002@cluster0.wurmd5z.mongodb.net/?retryWrites=true&w=majority")
db = client.BookFlix_db
register = db.register

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        firstName = request.form['content1']
        lastName = request.form['content2']
        email = request.form['email']
        register.insert_one({
            'first name':firstName, 
            'last name':lastName, 
            'email':email
        })
        return redirect(url_for('index'))
    all_info = register.find()
    return render_template('index.html', register=all_info)

if __name__ == "__main__":
    app.run(debug=True)
    

