import pytest
from django.urls import reverse
from .models import FAQ


@pytest.mark.django_db
def test_faq_creation():
    faq = FAQ.objects.create(question="How is it going?", answer="Better than anytime.")
    assert faq.question == "How is it going?"


@pytest.mark.django_db
def test_faq_api(client):
    response = client.get(reverse('faq-list'))
    assert response.status_code == 200
