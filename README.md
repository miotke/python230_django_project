# Python230 Django Project

Repo for the Django project that we are building in the Python230, Python Programming certificate class at the Univeristy of Washington.
The project we're building is a blog application.

### Virtual environment
The virtual environment for this project is stored on my local Mac and is not included in this repo.

Please create a local virtual environment and install the packages inside the `requirements.txt`
* `pip3 install -r requirements.txt`

* Local environment activation
	* `source ~/python_environments/python230_djangoenv/bin/activate`



### Django version
Due to a sqlite3 error I upgraded to Django 2.2.6 which resolved the `no such table: main.auth_user__old` error. This error may be caused by a sqlite 3 version problem and not Django. This project _should_ run in Django 2.1.1
