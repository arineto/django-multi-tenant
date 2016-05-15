DMIN_PY=$(VIRTUAL_ENV)/bin/django-admin.py
MANAGE_PY=$(VIRTUAL_ENV)/bin/python manage.py
PIP=$(VIRTUAL_ENV)/bin/pip
PY=$(VIRTUAL_ENV)/bin/python

requirements:
	@$(PIP) install -r requirements.txt

createsuperuser:
	@$(MANAGE_PY) createsuperuser

shell:
	@$(MANAGE_PY) shell

clean:
	@find . -name '*.pyc' -exec rm -f {} \;
	@find . -name 'Thumbs.db' -exec rm -f {} \;
	@find . -name '*~' -exec rm -f {} \;

runserver:
	@$(MANAGE_PY) runserver

mig:
	@$(MANAGE_PY) migrate

makemig:
	@$(MANAGE_PY) makemigrations

static:
	@$(MANAGE_PY) collectstatic --clear --noinput

tests:
	@$(MANAGE_PY) test
