import pytest
from django.urls import reverse
from .models import FAQ


@pytest.mark.django_db
def test_faq_creation():
    faq = FAQ.objects.create(question="What is Django?", answer="A web framework.")
    assert faq.question == "What is Django?"


@pytest.mark.django_db
def test_faq_api(client):
    response = client.get(reverse('faq-list'))
    assert response.status_code == 200
