#import jwt, datetime, os
import os
#from flask_mysqldb import MySQL
from flask import Flask, render_template, request


app = Flask(__name__)
#mysql = MySQL(app)

# config
app.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
app.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
app.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")


@app.route('/')
def home():
    return render_template('index.html')


#@app.route('/login', methods=["POST"])
#def login():
#    auth = request.authorization
#    if not auth:
#        return "missing credentials", 401
#
#    cur = mysql.connection.cursor()
#    res = cur.execute(
#       "SELECT email,password FROM user WHERE email=%s", (auth.username,auth.password)
#    )


#@app.route('register')
#def register():
#    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
