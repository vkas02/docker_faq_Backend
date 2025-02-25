# **Docker Django FAQs**  

This is a **Django-based FAQ system** that allows managing frequently asked questions (**FAQs**). It supports **multiple languages** and provides API endpoints to retrieve and manage FAQs dynamically.  

---

## **🚀 Features**  

✔️ **CRUD Operations** – Manage FAQs (Add, Update, Delete)  
✔️ **Multilingual Support** – Dynamic translation for FAQs  
✔️ **REST API** – Retrieve FAQs via API calls  
✔️ **Admin Dashboard** – Easy FAQ management  
✔️ **Dockerized Deployment** – For seamless setup  

---

## **🛠️ Technologies Used**  

- **Django** – Web framework  
- **Django REST Framework (DRF)** – API development  
- **PostgreSQL** – Database  
- **django-modeltranslation** – Multilingual support  
- **Docker & Docker Compose** – Containerization
-  **Nginx** – Reverse-proxy  

---

## **📌 Setup (with Docker)**  

### **1️⃣ Prerequisites**  

- Python  
- PostgreSQL (Local or AWS RDS)  
- Redis  
- Docker & Docker Compose installed  

### **2️⃣ Clone the Repository**  

```bash
git clone https://github.com/vkas02/docker_faq_Backend.git
cd docker_faq_Backend
```
### 3️⃣ Run with Docker
To start the containers, run
```
docker-compose -f docker-compose.prod.yml up --build
```
This will: 
- Build & run the Django app
- Set up PostgreSQL & Redis


> ⚠️ **NOTE:** The nginx will serve at port 8002 for static files. so 127.0.0.1:8002/ will be the serving page for local development. 

### 📌 API Endpoints
1️⃣ Fetch All FAQs (with Language Support)
```
GET /api/faqs/?lang=<language_code>
```
- If the translation fails, it defaults to English.
- Example: Get FAQs in Tagalog
```commandline
GET /api/faqs/?lang=tl
```
```commandline
Response:-
[
    {
        "id": 1,
        "question": "Which technologies did I use to build this application?",
        "answer": "<p>This application is built using <strong>Django </strong>for the backend, with a PostgreSQL database for data storage. The frontend integrates a WYSIWYG editor (using django-ckeditor) to allow easy content management. <strong>Redis </strong>is used for caching, and <strong>Google Translate API </strong>handles multi-language support. <strong>Docker </strong>is utilized for containerization, while <strong>Nginx </strong>serves as the web server to manage static file delivery and reverse proxy requests efficiently.</p>",
        "translated_question": "Aling mga teknolohiya ang ginamit ko upang mabuo ang application na ito?",
        "translated_answer": "<p> Ang application na ito ay binuo gamit ang <strong> django </strong> para sa backend, na may isang database ng PostGreSQL para sa imbakan ng data.Ang Frontend ay nagsasama ng isang editor ng WYSIWYG (gamit ang Django-Ckeditor) upang payagan ang madaling pamamahala ng nilalaman.Ang <strong> redis </strong> ay ginagamit para sa caching, at ang <strong> Google Translate API </strong> ay humahawak ng suporta sa multi-wika.Ang <strong> Docker </strong> ay ginagamit para sa lalagyan, habang ang <strong> nginx </strong> ay nagsisilbing web server upang pamahalaan ang paghahatid ng static na file at reverse proxy na mga kahilingan nang mahusay. </p>",
        "created_at": "2025-02-01T16:58:46.805450Z"
    },
    {
        "id": 2,
        "question": "Why did you choose Docker and Nginx in this project?",
        "answer": "<p>Docker allows for easy deployment, scaling, and consistency between environments, making it perfect for production. Nginx acts as a reverse proxy to efficiently serve static files, balance loads, and ensuring that the application performs well in production environments.</p>",
        "translated_question": "Bakit mo pinili ang Docker at Nginx sa proyektong ito?",
        "translated_answer": "Pinapayagan ng <p> Docker para sa madaling pag -deploy, scaling, at pagkakapare -pareho sa pagitan ng mga kapaligiran, na ginagawang perpekto para sa paggawa.Ang Nginx ay kumikilos bilang isang reverse proxy upang mahusay na maghatid ng mga static na file, balanse ng mga naglo -load, at tinitiyak na ang application ay gumaganap nang maayos sa mga kapaligiran ng produksyon. </p>",
        "created_at": "2025-02-01T19:02:01.435648Z"
    },
    {
        "id": 3,
        "question": "Are there plans for further improvements or additional features?",
        "answer": "<p>In the future, I plan to integrate automatic translation updates, allowing FAQs to be periodically updated with the latest translations.&nbsp;</p>\r\n\r\n<p>Adding Authentication system is also a part of scalability.</p>",
        "translated_question": "Mayroon bang mga plano para sa karagdagang mga pagpapabuti o karagdagang mga tampok?",
        "translated_answer": "<p> Sa hinaharap, plano kong isama ang mga awtomatikong pag -update ng pagsasalin, na nagpapahintulot sa mga FAQ na pana -panahong na -update sa pinakabagong mga pagsasalin. & NBSP; </p>\r\n\r\n<p> Pagdaragdag ng sistema ng pagpapatunay ay isang bahagi din ng scalability. </p>",
        "created_at": "2025-02-01T19:03:27.728378Z"
    }
]
```
- Example: Get FAQs in French
```commandline
GET /api/faqs/?lang=fl
```
```commandline
Response:-
[
    {
        "id": 1,
        "question": "Which technologies did I use to build this application?",
        "answer": "<p>This application is built using <strong>Django </strong>for the backend, with a PostgreSQL database for data storage. The frontend integrates a WYSIWYG editor (using django-ckeditor) to allow easy content management. <strong>Redis </strong>is used for caching, and <strong>Google Translate API </strong>handles multi-language support. <strong>Docker </strong>is utilized for containerization, while <strong>Nginx </strong>serves as the web server to manage static file delivery and reverse proxy requests efficiently.</p>",
        "translated_question": "Quelles technologies ai-je utilisé pour créer cette application?",
        "translated_answer": "<p> Cette application est construite à l'aide de <strong> django </strong> pour le backend, avec une base de données PostgreSQL pour le stockage de données.Le frontend intègre un éditeur WYSIWYG (à l'aide de Django-Ckediteur) pour permettre une gestion de contenu facile.<strong> redis </strong> est utilisé pour la mise en cache, et <strong> Google Translate API </strong> gère le support multi-langues.<strong> docker </strong> est utilisé pour la contenerisation, tandis que <strong> nginx </strong> sert de serveur Web à gérer efficacement la livraison de fichiers statiques et les demandes de proxy inverse. </p>",
        "created_at": "2025-02-01T16:58:46.805450Z"
    },
    {
        "id": 2,
        "question": "Why did you choose Docker and Nginx in this project?",
        "answer": "<p>Docker allows for easy deployment, scaling, and consistency between environments, making it perfect for production. Nginx acts as a reverse proxy to efficiently serve static files, balance loads, and ensuring that the application performs well in production environments.</p>",
        "translated_question": "Pourquoi avez-vous choisi Docker et Nginx dans ce projet?",
        "translated_answer": "<p> Docker permet un déploiement, une mise à l'échelle et une cohérence faciles entre les environnements, ce qui le rend parfait pour la production.Nginx agit comme un proxy inverse pour servir efficacement les fichiers statiques, équilibrer les charges et s'assurer que l'application fonctionne bien dans les environnements de production. </p>",
        "created_at": "2025-02-01T19:02:01.435648Z"
    },
    {
        "id": 3,
        "question": "Are there plans for further improvements or additional features?",
        "answer": "<p>In the future, I plan to integrate automatic translation updates, allowing FAQs to be periodically updated with the latest translations.&nbsp;</p>\r\n\r\n<p>Adding Authentication system is also a part of scalability.</p>",
        "translated_question": "Y a-t-il des plans pour d'autres améliorations ou des fonctionnalités supplémentaires?",
        "translated_answer": "<p> À l'avenir, je prévois d'intégrer des mises à jour automatiques de traduction, permettant à la FAQ d'être mise à jour périodiquement avec les dernières traductions. & nbsp; </p>\r\n\r\n<p> L'ajout du système d'authentification fait également partie de l'évolutivité. </p>",
        "created_at": "2025-02-01T19:03:27.728378Z"
    }
]
```
## Pytest Results ##
Here is the result of the tests done-
![Alt Text](images/image1.png)



### 🎯 Future Enhancements
- Add frontend for FAQ management
- Deploy with AWS
- Improve search & filtering options

### **Troubleshooting**
- **Nginx takes time to start**:If shows 500s error after building the container,wait for 30 seconds and refresh the page.
- **Translation fails**: Ensure the Google Translate API key is valid and properly configured.

### 📜 License
This project is open-source and available under the MIT License.

### 🔗 Contact
📧 Email: vkvs02@gmail.com
