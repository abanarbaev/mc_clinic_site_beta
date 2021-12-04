#-create venv
#py -m venv djcmsvenv

#-activate venv djcmsvenv
#djcmsvenv\Scripts\activate

#pip install --upgrade pip

#pip install mysqlclient
		#- для сервера reg.ru
		#CFLAGS="-std=c99" pip install mysqlclient


		"""
		mysql -u root -p
		*92800047

		1# mysql -u u1494237_djcms_u -p ZYQUy6zx7RNs3MR -h хост_или_IP_сервера_MySQL
		2# mysql -u u1494237_djcms_u -h хост_или_IP_сервера_MySQL -p
		
		1# CREATE DATABASE u1494237_djcms_mc02;
		2# mysqladmin create u1494237_djcms_mc02;

		1# 	CREATE USER 'u1494237_djcms_u'@'хост_или_IP_машины' IDENTIFIED BY 'ZYQUy6zx7RNs3MR';

		2# 	CREATE USER 'u1494237_djcms_u'@'%' IDENTIFIED BY 'ZYQUy6zx7RNs3MR';
			CREATE USER 'u1494237_djcms_u'@'localhost' IDENTIFIED BY 'ZYQUy6zx7RNs3MR';

		1# 	GRANT ALL PRIVILEGES ON u1494237_djcms_mc02.* TO 'u1494237_djcms_u'@'%';
			GRANT ALL PRIVILEGES ON u1494237_djcms_mc02.* TO 'u1494237_djcms_u'@'localhost';

		1# FLUSH PRIVILEGES;




		
		"""

#pip install djangocms-installer

#mkdir mc02-project
#cd mc02-project

#djangocms mc02
	#pip install pytz  - if ERROR

#cd mc02

#python manage.py runserver

#http://localhost:8000/

					"""
					vim mc02-project/mc02/settings.py

					ALLOWED_HOSTS = ['travma-spb.ru, 'www.travma-spb.ru', 'medicareclinic.ru', 'www.medicareclinic.ru']

					DATABASES = {
					    'default': {
					        'CONN_MAX_AGE': 0,
					        'ENGINE': 'django.db.backends.mysql',
					        'HOST': 'localhost',
					        'NAME': 'u1494237_djcms_mc02',
					        'PASSWORD': 'ZYQUy6zx7RNs3MR',
					        'PORT': '',
					        'USER': 'u1494237_djcms_u'
					    }
					}

					STATIC_ROOT='static/'

					:wq

					

					-создать passenger_wsgi.py

					# -*- coding: utf-8 -*-
					import os, sys
					sys.path.insert(0, '/var/www/u1494237/data/www/travma-spb.ru/mc02-project/')
					sys.path.insert(1, '/var/www/u1494237/data/djcmsvenv/lib/python3.9/site-packages/')
					os.environ['DJANGO_SETTINGS_MODULE'] = 'mc02.settings'
					from django.core.wsgi import get_wsgi_application
					application = get_wsgi_application()


					"""

# python manage.py collectstatic

# python manage.py migrate

# python manage.py createsuperuser --username=adminjr --email=adilet.anarbaev@ya.ru



