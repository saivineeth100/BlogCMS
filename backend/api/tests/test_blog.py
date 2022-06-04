from http import client
import json


from django.urls import reverse


from .setup import TestSetup
from blog.models import BlogStatuses


class BlogViewsTests(TestSetup):

    def setUp(self):
        self.postscrudurl = reverse(viewname="blogcrud")
        return super().setUp()

    def test_create_post_as_superadmin(self):
        # Login as SuperAdmin
        data = {"username": "saivineeth", "password": "demo@123"}
        Login(self.client, data, self.login_url)
        blogpostdata = {"title": "Test dsf", "slug": "test-slugxcszdfdsfgfh",
                        "content": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum",
                        "status": "Published"
                        }
        res = self.client.post(self.postscrudurl, blogpostdata)
        status = json.loads(res.content).get("status")
        self.assertEqual(res.status_code, 201)
        self.assertEqual(status, BlogStatuses.PUBLISHED)

   # creating post as admin automatically sets published to review
    def test_create_post_as_admin(self):
        # Login as SuperAdmin
        data = {"username": "adminuser", "password": "test@123"}
        Login(self.client, data, self.login_url)
        blogpostdata = {"title": "Test dsf", "slug": "test-slugxcszdfdsfgfh",
                        "content": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum",
                        }
        res = self.client.post(self.postscrudurl, blogpostdata)
        status = json.loads(res.content).get("status")
        self.assertEqual(res.status_code, 201)
        self.assertEqual(status, BlogStatuses.INTIALREVIEW)



def Login(client, data, loginurl):
    authres = client.post(loginurl, data)
    tokens = json.loads(authres.content).get("tokens")
    acesstoken = tokens.get("access")
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {acesstoken}')
