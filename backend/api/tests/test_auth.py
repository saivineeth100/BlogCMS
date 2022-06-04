



from .setup import TestSetup

class AuthViewsTests(TestSetup):

    def setUp(self):
        return super().setUp()

    def test_Login_Emptydata(self):
        res = self.client.post(self.login_url)
        self.assertEqual(res.status_code, 400)
    
    def test_Login_Wrongdata(self):
        data = {"username": "saivineeth", "password":"testwrongpassword"}
        res = self.client.post(self.login_url,data)
        self.assertEqual(res.status_code, 401)
    
    def test_login_SuperAdmin_user(self):
        data = {"username": "saivineeth", "password":"demo@123"}
        res = self.client.post(self.login_url,data)
        self.assertEqual(res.status_code, 200)

    def test_login_Admin_user(self):
        data = {"username": "adminuser", "password":"test@123"}
        res = self.client.post(self.login_url,data)
        self.assertEqual(res.status_code, 200)

    def test_login_reader_user(self):
        data = {"username": "reader", "password":"test@123"}
        res = self.client.post(self.login_url,data)
        self.assertEqual(res.status_code, 200)