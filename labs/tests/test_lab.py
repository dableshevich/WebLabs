import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_login_page(client):
    url = reverse('login')
    response = client.get(url)
    print(response.content.decode())
    assert response.status_code == 301


@pytest.mark.django_db
def test_books_page(client):
    url = reverse('homepage')
    response = client.get(url)
    print(response.content.decode())
    assert response.status_code == 301
