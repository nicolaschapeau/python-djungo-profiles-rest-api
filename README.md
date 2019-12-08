Learning djungo...


vagrant up -> install virtual server image
vagrant ssh -> connect to server via ssh
    exit -> exit server connection

cd /vagrant -> navigate into syncronised folder of server

python -m venv ~:env -> create python env in /env
source ~/env/bin/activate -> activate python env
    deactivate -> exit python env

pip install -r requirements.txt -> install python/django dependancies

python manage.py runserver 0.0.0.0:8000 -> run server on port 8000


python manage.py makemigrations profiles_api -> create migrations for profiles_api
python manage.py migrate -> execute all migrations