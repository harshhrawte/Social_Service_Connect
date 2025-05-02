from flask import Flask, render_template,request,redirect, url_for,session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'donaters'
mysql = MySQL(app)


@app.route('/')
def hello_world():
    return render_template('ssc.html')

@app.route("/donate2", methods=['POST'])
def donate2():
    if request.method == 'POST':
        userDetails = request.form
        Username = userDetails['un']
        ContactNo= userDetails['pn']
        Email= userDetails['em']
        Items = userDetails['psw']
        Address= userDetails['address']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `donate_details`(`Username`, `ContactNo`,`Email`, `Items`, `Address`) VALUES (%s,%s,%s,%s,%s)",(Username,ContactNo,Email,Items,Address))

        mysql.connection.commit()

        cur.close()
        return render_template('ssc.html')


@app.route('/login_process', methods=['GET', 'POST'])
def login_process():
    if request.method == 'POST':
        username = request.form['un']
        password = request.form['psw']

        cur = mysql.connection.cursor()
        cur.execute("SELECT UserName FROM signup WHERE UserName = %s AND Password = %s", (username, password))
        x = cur.fetchone()

        cur.close()
        cur.close()
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM inter")
        data = cur.fetchall()  # Fetch all rows from the result set
        cur.close()
        if x:
            session['UserName'] = x[0]
            return render_template('studentpage.html',x=x,data = data)
        else:
            return 'Invalid username/password'

    return render_template('ssc.html')
@app.route('/ngodonor_page')
def ngodonor_page():
    return render_template('ngodonor.html')

@app.route('/donorr_page')
def donorr_page():
    return render_template('ngodonor.html')

@app.route('/donorsignup_page')
def donorsignup_page():
    return render_template('sign.html')

@app.route('/ngosignup_page')
def ngosignup_page():
    return render_template('ngosignup.html')

@app.route('/sign_page', methods=['GET', 'POST'])
def sign_page():
    return render_template('loggpage.html')

@app.route('/logintohome_page', methods=['GET', 'POST'])
def logintohome_page():
    return render_template('ssc.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/donatee2')
def donatee2():
    return render_template('donatee2.html')

@app.route('/volunteer')
def volunteer():
     return render_template('volunteer.html')

@app.route('/shop')
def shop():
     return render_template('shop.html')

@app.route('/shopp')
def shopp():
     return render_template('shopp.html')




if __name__ == '__main__':
    app.run()
