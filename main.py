# from flask import Flask,render_template,request,redirect
# import os
# import sqlite3 as sql

# currentlocation = os.path.dirname(os.path.abspath(__file__))

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Welcome to NLP project!"

# @app.route("/home")
# def home1():
#     return render_template("index.html")
    
# @app.route("/login")
# def index():
#     return render_template("login.html")

# @app.route("/about")
# def about():
#     return render_template("about.html")

# def retrieveUsers():
# 	con = sql.connect("resume.db")
# 	cur = con.cursor()
# 	cur.execute("SELECT username, password FROM login")
# 	users = cur.fetchall()
# 	con.close()
# 	return users


# @app.route('/login', methods=['POST', 'GET'])
# def login():

#     if request.method=='POST':
#         username = request.form['username']
#         password = request.form['password']
#         users = dbHandler.retrieveUsers()
#     else:
#    		return render_template('index.html')

    # sqlconnection=sqlite3.Connection(currentlocation + "/resume.db")
    # cursor = sqlconnection.cursor()
    # query1 = "SELECT username, password FROM login WHERE username = {user} AND password = {passw}".format(user=user,passw=passw)

    # rows = cursor.execute(query1)
    # rows = rows.fetchall()
    # if len(rows) == 1 :
    #      return render_template("/success")
    # else:
    #      return redirect('/failure')
    # if request.method == 'GET':
    #     return render_template('login.html',form = form)
    
# @app.route('/failure')
# def failure():
#     return '<h1 style="color:green; text-align:center; Not a Registered User </h1>" <div class="main"> <marquee class="marq" Scrolldelay="35" truespeed="true" bgcolor="White" direction="left"  loop=""> Not a registered user </marquee>  </div> <h2 style="color:green; text-align:center; Contact Administrator </h2>" <div class="main"> <marquee class="marq" Scrolldelay="35" truespeed="true" bgcolor="White" direction="left"  loop=""> Contact Administrator </marquee>  </div>'
# @app.route('/success')
# def success():
#     return "success"

# if __name__ == "__main__":
#     app.run(debug=True)




    # user = request.form['username']
    # passw = request.form['password']

    # sqlconnection=sqlite3.Connection(currentlocation + "/resume.db")
    # cursor = sqlconnection.cursor()
    # query1 = "SELECT username, password FROM login WHERE username = {user} AND password = {passw}".format(user=user,passw=passw)

    # rows = cursor.execute(query1)
    # rows = rows.fetchall()
    # if len(rows) == 1 :
    #     return render_template("success.html")
    # else:
    #     return redirect('/failure')



    #____________--------------________xxxxxx________----------___________#


from flask import Flask,render_template,request,redirect,url_for,session
import pymongo
import bcrypt

app = Flask(__name__)

#app.config['MONGODB_NAME']='users'
#app.config['MONGO_URI'] = 'mongodb+srv://user_illiyas:iKSfL7tRgrtijFN2@cluster0.v9zxc.mongodb.net/users?retryWrites=true&w=majority'
client = pymongo.MongoClient('mongodb+srv://user_illiyas:iKSfL7tRgrtijFN2@cluster0.v9zxc.mongodb.net/users?retryWrites=true&w=majority')
db = client.get_database('total_records')
records = db.register
#mongo = PyMongo(app)


@app.route("/", methods=['POST', 'GET'])
def index():
    message = ''
    if "name" in session:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        user = request.form.get("fullname")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user_found = records.find_one({"name": user})
        email_found = records.find_one({"email": email})

        if user_found:
            message = 'There already is a user by that name'
            return render_template('register.html', message=message)
        if email_found:
            message = 'This email already exists in database'
            return render_template('register.html', message=message)
        if password1 != password2:
            message = 'Passwords should match!'
            return render_template('register.html', message=message)

        else:
            hashed = password2
            user_input = {'name': user, 'email': email, 'password': hashed}
            records.insert_one(user_input)

            user_data = records.find_one({"email": email})
            new_email = user_data['email']


            return redirect(url_for("dashboard")) #dashboard
    return render_template('login.html')


@app.route('/logged_in')
def logged_in():
    if "email" in session:
        email = session["email"]
        return render_template('logged_in.html', email=email)
    else:
        return redirect(url_for("login"))

@app.route("/login", methods=["POST", "GET"])
def login():
    message = 'Please login to your account'
    if "name" in session:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        user = request.form.get("Username")
        password = request.form.get("Password")
        email_found = records.find_one({"name": user})

        if email_found  :
            email_val = email_found['name']
            passwordcheck = email_found['password']
        
            if bcrypt.checkpw(password, passwordcheck):
                session["name"] = email_val
                return render_template('dashboard.html')
            else:
                if "name" in session:
                    return render_template('dashboard.html')
                    message = 'Wrong password'
            return render_template('dashboard.html', message=message)
        else:
            message = 'Email not found'
            return render_template('login.html', message=message)
    return render_template('login.html', message=message)

@app.route("/dashboard")
def dashboard():
    

    if "name" in session:
        email = session["name"]
        return render_template("dashboard.html")

    else:
        return render_template("dashboard.html")


@app.route("/result")
def result():
    render_template('result.html')
# @app.route('/login', methods=['POST'])
# def login():
#     users = mongo.db.users
#     login_user = users.find_one({'name': request.form['username']})

#     if login_user:
#         if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
#             session['username'] = request.form['username']
#             return redirect(url_for('index'))

#     return 'Invalid username or password'
# @app.route('/register', methods=['POST', 'GET'])
# def register():
#     if request.method == 'POST':
#         users = mongo.db.users
#         existing_user = users.find_one({'name' : request.form['username']})

#         if existing_user is None:
#             hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
#             users.insert({'name':request.form['username'], 'password': hashpass})
#             session['username'] =  request.form['username']
#             return redirect(url_for('index'))

#         return 'That username already exists!'

#     return render_template('register.html')



if __name__ == "__main__":
    app.secret_key='mysecretkey'
    app.run(debug=True)     