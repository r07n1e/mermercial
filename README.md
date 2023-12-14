# mermercial
A ready to use APIs for e-commerce website.

``` bash
git clone https://github.com/r07n1e/mermercial.git

python -m venv venv

venv\bin\activate (Linux or Mac) 
venv\Scripts\activate.bat (Windows CMD)
venv\Scripts\activate.ps1 (Windows Powershell)

docker-compose up -d

docker-compose exec web python manage.py migrate
```

### Craete Superuser
```bash
docker-compose exec web python manage.py createsuperuser
```

### If need to make migration, execute before migrate
``` bash
docker-compose exec web python manage.py makemigrations
```

### Note
This project is a work in progress. It's for me to learn python django. Don't be critical about it. Thank you
