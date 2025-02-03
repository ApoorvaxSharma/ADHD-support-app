from firebase import firebaseConfig
import pyrebase
from django.conf import settings
from django.http import JsonResponse
from firebase_admin import auth
from django.utils.deprecation import MiddlewareMixin


class FirebaseAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        id_token = request.META.get('HTTP_AUTHORIZATION')
        if id_token:
            try:
                decoded_token = auth.verify_id_token(id_token)
                request.firebase_user = decoded_token
            except:
                request.firebase_user = None
        else:
            request.firebase_user = None


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return JsonResponse({"message": "Login successful", "idToken": user['idToken']})
    except:
        return JsonResponse({"message": "Invalid credentials"}, status=401)
    
def verify_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        return uid
    except:
        return None