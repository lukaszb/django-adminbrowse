from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
setup(
    name = "django-adminbrowse",
    version = "0.1.1",
    packages = ['adminbrowse'],
    include_package_data = True,
    author = "Brian Beck",
    author_email = "exogen@gmail.com",
    description = "Add related object links and other useful info to the "
                  "Django admin interface",
    license = "MIT",
    keywords = "django admin changelist",
    url = "https://github.com/exogen/django-adminbrowse"
)

