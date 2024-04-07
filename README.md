### Hanja Hero

* Setup project steps:
  (Init database if needed)
```shell
python3 manage.py migrate
python3 manage.py import_question_meta_data home/static/data/question_meta_data.json
python3 manage.py import_question_data home/static/data/question_data.json
python3 manage.py populate_time_limit
python manage.py import_user_data /Users/thaohinnn/Docker/hanjahero/home/static/data/user_data.json
```
* Run project steps:
```shell
python3 manage.py runserver
```

* Run tests:
```shell
python3 manage.py test
```

