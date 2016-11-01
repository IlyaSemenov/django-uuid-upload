"""Store Django uploaded files as UUID files or inside UUID directories"""
from setuptools import setup, find_packages


setup(
	name='django-uuid-upload',
	version='0.0.1',
	url='https://github.com/IlyaSemenov/django-uuid-upload',
	license='BSD',
	author='Ilya Semenov',
	author_email='ilya@semenov.co',
	description=__doc__,
	long_description=open('README.rst').read(),
	packages=find_packages(),
	install_requires=['Django>=1.7'],
	classifiers=[],
)
