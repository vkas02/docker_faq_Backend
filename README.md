# docker_faq_Backend initialized

# FAQ Management System

This is a Django-based FAQ system that allows us to manage frequently asked questions (FAQs). The system supports multiple languages for FAQs and provides API endpoints to retrieve and manage them.

## Features

- We can manage FAQs (add, update, delete).
- Multilingual support for FAQ content (translations are stored and served dynamically).
- API to retrieve FAQs and their translations based on the user's language.
- Admin interface for easy management of FAQs.

## Technologies Used

- Django 3.x
- Django REST Framework
- PostgreSQL (for the database)
- `django-modeltranslation` for multilingual support
- Docker (for containerization)

## Setup
Ensure you have Docker and Docker Compose installed.Ensure you have Docker and Docker Compose installed. In the project root directory, run the following command to start your containers:

`docker-compose -f docker-compose.prod.yml up --build`


### Prerequisites

- Python 3.x
- PostgreSQL database (can be local or hosted on AWS RDS)
- `django-modeltranslation` for multilingual support
- Redis (optional, for caching)

### 1. Clone the Repository

Clone the project from your Git repository:

```bash
git clone <repository-url>
cd <your-project-directory>
