migrate:
	### Run makemigrations
	@python manage.py makemigrations
	### Run migrate
	@python manage.py migrate

run:
	### Run server
	@python manage.py runserver

backup_venv:
	### Run freeze check list
	@pip freeze
	@@read -p "Do you want to continue [Y/n]? " -n 1 -r; \
	### Run freeze
	@pip freeze > requirements.txt

shell:
	### Run server on shell
	@python manage.py shell