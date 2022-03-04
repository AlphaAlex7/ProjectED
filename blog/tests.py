from unittest import TestCase
from parameterized import parameterized
from django.test import Client
from blog.models import PostModel
list_url = [
    "/posts/",
    "/posts/add/",
    f"/posts/detail/{PostModel.objects.first().id}/"
]

class TestAuth(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.c = Client()
        response = cls.c.post('/account/login/', {'username': 'Oz', 'password': '123456'})
        assert response.status_code == 302

    @parameterized.expand(list_url)
    def test_base(self, url):
        response = self.c.get(url)
        assert response.status_code == 200, f"wrong {url}"

class TestWithOutAuth(TestCase):
    @parameterized.expand(list_url)
    def test_main(self,url):
        pass