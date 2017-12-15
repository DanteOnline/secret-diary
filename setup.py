import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='secret-diary',
    version='0.2',
    #packages=find_packages('secretdiary'),
    packages=find_packages(),
    include_package_data=True,
    license='GNU General Public License v3.0', 
    description='Secret diary',
    long_description=README,
    url='https://github.com/DanteOnline/secret-diary',
    author='DanteOnline',
    author_email='iamdanteonline@gmail.com',
    keywords = ['diary', 'encrypt', 'secret'],
    classifiers = [],
    install_requires=['pycryptodome', 'pycryptodomex'],
    entry_points={
        'console_scripts': [
            'secret_diary = secretdiary.main:main',
        ]
    },
)