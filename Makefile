clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . | grep -E "__pycache__|.pytest_cache|.pyc|.DS_Store$$" | xargs rm -rf

migrate:
	#Primeira vez  export PYTHONPATH=/home/anderson/Dados/Dev/Python/PyCRUD
	#flask db init
	@export PYTHONPATH="/home/anderson/Dados/Dev/Python/PyCRUD" && python src/alembic/manager.py db migrate

upgrade:
	@export PYTHONPATH="/home/anderson/Dados/Dev/Python/PyCRUD" && python src/alembic/manager.py db upgrade

docker:
	@echo "---- Building & Up Container ----"
	@docker-compose down
	@docker-compose build
	@docker-compose up -d

dockerdown:
	@docker-compose down

setup:
	@echo "---- Installing Python dependencies ----"
	@pip3 install -r requirements.txt --upgrade

test:
	@pytest --verbose --disable-pytest-warnings --color=yes tests/

run:
	python src/app.py
