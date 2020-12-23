CPPFLAGS = -I include
P_CMD = python
F_CMD = manage.py

s_venv:
	### activate source
	@. venv/bin/activate

migrate: $(F_CMD)
	### Run makemigrations
	@$(P_CMD) $< makemigrations
	### Run migrate
	@${P_CMD} $< $@

run: $(F_CMD) s_venv
	### Run server
	@${P_CMD} $< $@server

backup_venv:
	### Run freeze check list
	@pip freeze
	@@read -p "Do you want to continue [Y/n]? " -n 1 -r; \
	### Run freeze
	@test -d requirements.txt || pip freeze > requirements.txt . echo "xxx"

shell: $(F_CMD)
	### Run server on shell
	@$(P_CMD) $< $@

test:
	if [ "0" != "0" ]; then 
		echo "okok"
	fi;

docker_up:
	@docker-compose up