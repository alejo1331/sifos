migrate:
	docker-compose run web python manage.py makemigrations --settings=sifos.settings
	docker-compose run web python manage.py migrate auth --settings=sifos.settings
	docker-compose run web python manage.py migrate --settings=sifos.settings

requirements:
	docker-compose run web pip install -r requirements.txt

statics_dev:
	docker-compose run web python manage.py collectstatic --no-input --settings=sifos.settings

statics:
	docker-compose run web python manage.py collectstatic --no-input --settings=sifos.settings

superuser:
	docker-compose run web python manage.py createsuperuser --settings=sifos.settings

clean:
	rm -rf */migrations/00**.py
	find . -name "*.pyc" -exec rm -rf  -- {} +
	find . -name "*__pycache__" -exec rm -rf  -- {} +

testfixture:
	docker-compose run web python manage.py loaddata test

test:
	docker-compose run web python manage.py test

run:
	docker-compose run web python manage.py runserver 0.0.0.0:8000 --settings=sifos.settings

delete-all:
	docker-compose down -v
	sudo rm -rf .pgdata/

