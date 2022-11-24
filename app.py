from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
# from flask_mail import Mail,Message

app = Flask(__name__)
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'sule.devashish@gmail.com'
# app.config['MAIL_PASSWORD'] = 'pkjdoanccxiflxsq'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)

client = MongoClient("mongodb+srv://Devashish:Devashish2002@cluster0.wurmd5z.mongodb.net/?retryWrites=true&w=majority")
db = client.BookFlix_db
user_info = db.register_dets

@app.route('/')
def index():
    return render_template('index.html')
     

@app.route('/register.html', methods=('GET', 'POST'))
def register():
    if request.method=='POST':
        firstName = request.form['content1']
        lastName = request.form['content2']
        email = request.form['email']
        password1 = request.form['password1']
        password2 = request.form['password2']
        security_question = request.form['security']
        if password1==password2: 
            user_info.insert_one({
                'first name':firstName, 
                'last name':lastName, 
                'email':email,
                'password':password1,
                'security_question':security_question
            })
            # msg = Message(
            #     "BookFlix - Acknowledgement letter",
            #     sender='joemama@hotline.com',
            #     recipients=[email]
            # )
            # msg.body = "Thank You for creating an account in BookFlix."
            # mail.send(msg)
            return render_template('verified.html')
        else:
            return render_template('register.html')
            
    all_info = user_info.find()
    return render_template('register.html', user_info=all_info)

@app.route('/login.html')
def login():
    if request.method=="GET":
        email = request.form['email']
        password = request.form['password']
        verify_email = request.get('email')
        verify_pass = request.get('password')
        if email == verify_email and password == verify_pass:
            return "Welcome %s"%email
        else:
            return "Data not found..."
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
    

