import unittest 
from src import create_app,db
from src.config import configuration
from src.models.user import User


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config=configuration['testing'])
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()
        db.create_all()
        
    def tearDown(self):
        db.drop_all()
        self.app=None
        self.appctx.pop()
        self.client=None

    def test_user_registration(self):
        data={
            "name":"joe",
            "last_name": "lastname",
            "email": "joe@gmail.com",
            "phone_number": "3156324583",
            "password" : "admin"
            }

        response=self.client.post('/auth/register',json=data)
        assert response.status_code == 201
        response=self.client.get('/auth/register')
        assert response.status_code == 200

    def test_user_registration_email_none(self):
        data={
            "name":"joe",
            "last_name": "lastname",
            "email": "",
            "phone_number": "3156324583",
            "password" : "admin"
            }
        response=self.client.post('/auth/register',json=data)
        assert response.status_code == 409

    def test_user_registration_keys_invalidate(self):
        data={
            "name":"joe",
            "last_name": "lastname",
            "emeil": "aaa@aaa.com",
            "phone_number": "3156324583",
            "password" : "admin"
            }
        
        response=self.client.post('/auth/register',json=data)
        assert response.status_code == 200


    def test_driver_registration(self):
        data={
            "name":"joe",
            "last_name": "lastname",
            "email": "joe@gmail.com",
            "phone_number": "3156324583",
            "password" : "admin"
            },
        response = self.client.post('/driver/register',json=data)
        print(response.status_code)
        assert response.status_code == 200
        response = self.client.get('/driver/register')
        assert response.status_code == 200


    def test_driver_registration_email_none(self):
        data={
            "name":"joe",
            "last_name": "lastname",
            "email": "",
            "phone_number": "3156324583",
            "password" : "admin"
            }
        response=self.client.post('/driver/register',json=data)
        assert response.status_code == 409
     





    