import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client

from . import strings

# Create your tests here.
class SecretTestCase(TestCase):
    def setUp(self):
        self.username = "admin"
        self.password = "password"
        self.email = "activelime@yahoo.com"
        self.description = "hello"

        #check initial is zero
        self.assertEqual(User.objects.count(), 0)

        #add inital user
        self.user = User.objects.create_user(username=self.username, password=self.password, email=self.email)

        #check initial is zero
        self.assertEqual(self.user.secret_set.count(), 0)

        #add initial secret
        self.secret = self.user.secret_set.create(description=self.description)

    #added secret in setup, check if it was added
    def test_add_secret(self):
        #check if user is added
        self.assertTrue(User.objects.filter(pk=self.user.id).exists())
        self.assertEqual(User.objects.count(), 1)

        #check if secret exists in database
        self.assertTrue(self.user.secret_set.filter(pk=self.secret.id).exists())
        self.assertEqual(self.user.secret_set.count(), 1)

        secret = self.user.secret_set.get(pk=self.secret.id)
        self.assertEqual(secret.id, self.secret.id)
        self.assertEqual(self.secret.user_id, self.user.id)
        self.assertEqual(self.secret.description, self.description)

    #check if secret description changed
    def test_change_secret(self):
        description = "jason loves"
        secret = self.user.secret_set.get(pk=self.secret.id)
        secret.description = description
        secret.save()

        #check if description changed
        self.assertEqual(secret.description, description)

    #check if deleted secret
    def test_delete_secret(self):
        secret = self.user.secret_set.filter(pk=self.secret.id)
        secret.delete()

        #check if the object exists
        self.assertFalse(self.user.secret_set.filter(pk=self.secret.id).exists())

        #check count is zero
        self.assertEqual(self.user.secret_set.count(), 0)

    #add multiple secrets check
    def test_add_many_secret(self):
        description1 = "hello1"
        description2 = "hello2"
        self.user.secret_set.create(description=description1)
        self.user.secret_set.create(description=description2)

        #check if added to databse
        self.assertEqual(self.user.secret_set.count(), 3)

        #check if they exist in database
        self.assertTrue(self.user.secret_set.filter(description=description1).exists())
        self.assertTrue(self.user.secret_set.filter(description=description2).exists())

# Create your tests here.
# must delete middleware redirecting to https
# this is for the production environment
class ClientTestCase(TestCase):
    def setUp(self):
        #test client
        self.c = Client()

        self.USERNAME =  "username"
        self.PASSWORD = "password"
        self.USER = "user"
        self.SUCCESS = "success"
        self.DESCRIPTION = "description"
        self.TOKEN = "token"

        self.username = "admin"
        self.password = "password"
        self.email = "activelime@yahoo.com"

        self.secretsurl = '/secrets/'
        self.newtokenurl = '/secrets/token/new.json'
        self.tokenurl = '/secrets/token'
        self.token = None
        self.dict = {}

        #check initial is zero
        self.assertEqual(User.objects.count(), 0)

        #add inital user
        self.user = User.objects.create_user(username=self.username, password=self.password, email=self.email)

        #check initial is zero
        self.assertEqual(self.user.secret_set.count(), 0)

    def test_get_token(self):
        dict = {}
        dict[self.USERNAME] = self.username
        dict[self.PASSWORD] = self.password
        response = self.c.post(self.newtokenurl, dict)
        str_response = response.content.decode('utf-8')
        d = json.loads(str_response)
        self.assertTrue(d[self.SUCCESS])
        self.assertEqual(d[self.USER], self.user.id)

    def test_post_secret(self):
        user, token = self.getToken()

        dict = {}
        description = "hellomynameisandrew"
        dict[self.DESCRIPTION] = description
        url = self.secretsurl + self.authenticateuserurl(user, token)
        response = self.c.post(url, dict)
        str_response = response.content.decode('utf-8')
        d = json.loads(str_response)
        self.assertTrue(d[self.SUCCESS])

    def test_get_secret(self):
        user, token = self.getToken()

        secret_id, description = self.postSecret()
        print(str(secret_id))
        print(description)
        url = self.secretsurl + str(secret_id) + self.authenticateuserurl(user, token)
        response = self.c.get(url)
        print(response)
        print(response.content)
        str_response = response.content.decode('utf-8')
        print(str_response)
        d = json.loads(str_response)
        self.assertTrue(d[self.SUCCESS])
        self.assertEqual(d[self.DESCRIPTION], description)
        self.assertEqual(secret_id, d[strings.ID])

    def authenticateuserurl(self, user_id, token):
        return "?user=" + str(user_id) + "&token=" + token

    def getToken(self):
        dict = {}
        dict[self.USERNAME] = self.username
        dict[self.PASSWORD] = self.password
        response = self.c.post(self.newtokenurl, dict)
        str_response = response.content.decode('utf-8')
        d = json.loads(str_response)
        return d[self.USER], d[self.TOKEN]

    def postSecret(self):
        user, token = self.getToken()
        dict = {}
        description = "hellomynameisandrew"
        dict[self.DESCRIPTION] = description
        url = self.secretsurl + self.authenticateuserurl(user, token)
        response = self.c.post(url, dict)
        str_response = response.content.decode('utf-8')
        d = json.loads(str_response)
        return d[strings.ID], description







