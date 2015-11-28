from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class utility:
    def authenticate(username, password):
        user = authenticate(username=username, password=password)
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

    def username_present(user_id):
        if User.objects.filter(pk=user_id).exists():
            return True

        return False