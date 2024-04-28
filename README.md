### Hanja Hero

* Setup project steps:
  (Init database if needed)
```shell
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py import_question_meta_data home/static/data/question_meta_data_topik2.json
python3 manage.py import_question_data home/static/data/question_data_topik2.json
python3 manage.py import_question_meta_data home/static/data/question_meta_data_topik1.json
python3 manage.py import_question_data home/static/data/question_data_topik1.json
python3 manage.py populate_time_limit
python3 manage.py import_user_data home/static/data/user_data.json
python3 manage.py update_total_scores  
python manage.py assign_test_types
```
* Run project steps:
```shell
python3 manage.py runserver
```

* Run tests:
```shell
python3 manage.py test
```

