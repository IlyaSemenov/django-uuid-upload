django-uuid-upload
==================

Library for Django that automatically stores uploaded files as ``mydir/{uuid}.jpg`` or ``mydir/{uuid}/original.jpg``.


Installation
============

::

        pip install django-uuid-upload


Usage
=====

.. code:: python

	from django.db import models
	from django_uuid_upload import upload_to_uuid

	class Post(models.Model):
		# Store uploaded files as posts/{uuid}.jpg
		image = models.ImageField(upload_to=upload_to_uuid('posts'))
		
		# Or, store uploaded files as posts/{uuid}/original.jpg
		image = models.ImageField(upload_to=upload_to_uuid('posts', make_dir=True))