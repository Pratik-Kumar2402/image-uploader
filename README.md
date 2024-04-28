# Image Blog Post

Image uploader is a vital component of many web applications, enabling users to seamlessly upload images to the platform. It serves various purposes across diverse domains, including social media, e-commerce, content management systems, and more. Typically integrated into forms, image uploaders facilitate the submission of visual content, enhancing user engagement and interaction.




## Run Locally

Clone the project

```bash
  git clone https://github.com/Pratik-Kumar2402/image-uploader.git
```

Make sure Python is installed on the PC

- https://www.python.org/downloads/

Go to the project directory

```bash
  cd image-uploader
```

Install dependencies

```bash
  pip install django
  pip install pillow
```

Setting up environment

```bash
  python manage.py makemigrations
  python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```

For creating superuser for managing database

```bash
  python manage.py createsuperuser
```

- Give name as 'admin' or whatever you like
- Give email or leave it blank(optional)
- Give password of your choice or for simplicity let it be 'admin'

Then go to server and typing in /admin after the localhost,
example: 
```bash
  http://127.0.0.1:8000/admin/
```
