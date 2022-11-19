from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://Devashish:Devashish2002@cluster0.wurmd5z.mongodb.net/?retryWrites=true&w=majority")
db = client.BookFlix_db
register_dets = db.register_dets

@app.route('/')
def index():
    return render_template('index.html')
     

@app.route('/register.html', methods=('GET', 'POST'))
def register():
    if request.method=='POST':
        firstName = request.form['content1']
        lastName = request.form['content2']
        email = request.form['email']
        password = request.form['password']
        register_dets.insert_one({
            'first name':firstName, 
            'last name':lastName, 
            'email':email,
            'password':password
        })
        return render_template('verified.html')
    all_info = register_dets.find()
    return render_template('register.html', register_dets=all_info)

@app.route('/login.html')
def login():
    
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
    

