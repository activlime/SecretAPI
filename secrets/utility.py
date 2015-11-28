from django.contrib.auth import authenticate

def authenticate():
    user = authenticate(username='john', password='secret')
    if user is not None:
        # the password verified for the user
        if user.is_active:
            print("User is valid, active and authenticated")
            return True
        else:
            print("The password is valid, but the account has been disabled!")
            return False
            re
    else:
        # the authentication system was unable to verify the username and password
        print("The username and password were incorrect.")
        return False