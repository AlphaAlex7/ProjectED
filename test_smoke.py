import pytest
import django, os
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectED.settings')
django.setup()

from bs4 import BeautifulSoup as bs
from blog.models import PostModel, PostCategory


class TestSmoke:
    host = "http://127.0.0.1:8000"
    pages = [
        f"{host}/account/login/",
        f"{host}/account/registration/",
        f"{host}/posts/",
        f"{host}/posts/cat/{PostCategory.objects.first().id}/",
        f"{host}/posts/detail/{PostModel.objects.first().id}/",
    ]
    pages_auth = pages + [
        f"{host}/posts/add/"
    ]

    @pytest.mark.parametrize("page_url", pages)
    def test_pages_connect(self, page_url):
        response = requests.get(page_url)
        print(response)
        assert response.status_code == 200, f"wrong state {page_url}"
