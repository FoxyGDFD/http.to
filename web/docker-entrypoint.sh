echo "Making migrations"
python3 manage.py makemigrations

echo "Applying migrations"
python3 manage.py migrate

echo "Creating superuser from compose ENV vars"
python3 manage.py createsuperuser --noinput --email admin@ad.min

echo "Starting development server"
python3 manage.py runserver 0.0.0.0:8000

