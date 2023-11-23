# mermercial

``` bash
git clone https://github.com/r07n1e/mermercial.git

python -m venv venv

venv\bin\activate (Linux or Mac) 
venv\Scripts\activate.bat (Windows CMD)
venv\Scripts\activate.ps1 (Windows Powershell)

docker-compose up -d

docker-compose exec web python manage.py migrate
```

### If need to make migration, execute before migrate
``` bash
docker-compose exec web python manage.py makemigrations
```