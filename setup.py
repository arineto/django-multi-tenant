import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-multi-tenant',
    version='0.1',
    include_package_data=True,
    license='MIT',
    description='A simple Django app to help creating Multi-Tenant apps.',
    long_description=README,
    url='https://www.github.com/arineto/django-multi-tenant/',
    author='Arimatea Neto',
    author_email='arineto30@gmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Framework :: Django',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages=[
        'multi_tenant',
    ],
    install_requires=[
        'Django >= 1.9.0',
        'django-braces',
    ],
    zip_safe=False,
)
