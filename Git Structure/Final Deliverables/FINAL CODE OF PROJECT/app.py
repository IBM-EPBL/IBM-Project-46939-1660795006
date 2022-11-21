import ibm_db as db
from flask import Flask, render_template, request, redirect, session, abort
import os
import pathlib
import requests
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from google.oauth2 import id_token
#from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

# Configure Flask app
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# Load .env file
load_dotenv()

# Connect to the Database
HOSTNAME = "815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
PORT_NUMBER = 30367
DATABASE_NAME = "bludb"
USERNAME = "fvd12836"
PASSWORD = "DU6bccmyRvL96jNS"
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_AUTH_CLIENT_ID')

connection_string = "DATABASE={0};HOSTNAME={1};PORT={2};SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID={3};PWD={4};".format(DATABASE_NAME, HOSTNAME, PORT_NUMBER, USERNAME, PASSWORD)



# Frequently used variables
SIGN_UP_PAGE_URL = '/'
LOG_IN_PAGE_URL = '/login'
HOME_PAGE_URL = '/home'
GOOGLE_LOGIN_PAGE_URL = '/google_login'
PROFILE_PAGE_URL = '/profile'
CHANGE_PASSWORD_URL = '/changepwd'

# Google Auth Configuration
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

 
# Helper Function to execute SQL queries
 
   

 

# Helper function to send confirmation mail on sign in
def send_confirmation_mail(user, email):
    message = Mail(
        from_email="nutritionassistant854@gmail.com",
        to_emails=email,
        subject="YAYY!! Your Account was created successfully!",
        html_content= "<strong>Account Created with username {0}</strong>".format(user)
    )
    
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)

# Sign up page
@app.route(SIGN_UP_PAGE_URL, methods=['GET', 'POST'])
def signup():
     
    
    if session.get('user'):
        return redirect(HOME_PAGE_URL)

    if request.method == 'POST':
        
            return redirect(LOG_IN_PAGE_URL)
    return render_template("signup.html")

# Login page
@app.route('/login',methods=['GET', 'POST'])
def login():
 
    
    if request.method =='GET':
        return render_template("login.html")

    if request.method == "POST":

         return render_template("homepage.html")

# Login using Gmail
@app.route(GOOGLE_LOGIN_PAGE_URL , methods=['GET','POST'])
def google_login():
    
    return redirect()

# Configuring user credentials after gmail login
@app.route("/callback")
def callback():
    return redirect(HOME_PAGE_URL)

# Home page
@app.route('/home', methods=['GET', 'POST'])
def homepage():
    
    if request.method == 'GET':
         
        return render_template('homepage.html')

# Profile page
@app.route('/profile', methods=['GET', 'POST'])
def profile():
     
    
    return render_template('profile.html')

#change password
@app.route('/changepwd', methods=['GET', 'POST'])
def changepwd():
    if request.method =='GET':
        return render_template("passwordChange.html") 
     
    if request.method == 'POST':
        
        return render_template('profile.html')

    return render_template('passwordChange.html')


# Logout user
@app.route('/logout')
def logout():
    session['user'] = ''
    return redirect(LOG_IN_PAGE_URL)

# Delete user account
@app.route('/delete')
def delete():
    if not session.get('user'):
        return redirect(LOG_IN_PAGE_URL)

    
    return redirect(SIGN_UP_PAGE_URL)    

# Run the application
if __name__ == '__main__':
    app.run(debug=True)