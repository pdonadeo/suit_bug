# Django Suit Ordering bug

Step to reproduce this bug:
* `$ git clone https://github.com/pdonadeo/suit_bug.git`
* `$ cd suit_bug`
* `$ mkvirtualenv suit_bug`
* `$ pip install --upgrade pip`
* `$ pip install -r requiremets.txt`
* `$ ./manage.py makemigrations`
* `$ ./manage.py migrate`
* `$ ./manage.py collectstatic`
* `$ ./manage.py createsuperuser`
* `$ ./manage.py loaddata my_app/fixtures/data.json`
* `$ ./manage.py runserver`

Now open http://127.0.0.1:8000/admin/ and log in with the supersuser jou just created.
