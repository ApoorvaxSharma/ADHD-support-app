import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate("C:\Users\APOORVA SHARMA\OneDrive\Documents\ADHD_Support_App\adhd_support\adhd-support-app-aa1962a8c2fb.json")
firebase_admin.initialize_app(cred)

 
authe = firebase.auth()
database=firebase.database()

