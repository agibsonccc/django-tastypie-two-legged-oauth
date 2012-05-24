import os
 
from distutils.core import setup
from setuptools import setup, find_packages

 

 
setup(
    name='django-tastypie-two-legged-oauth',
    version='0.1',
    description='',
    keywords='osqa question answering context',
    license='GNU LESSER GENERAL PUBLIC LICENSE',
    zip_safe=False,
    author='Adam Gibson',
    author_email='agibson@clevercloudcomputing.com',
    maintainer='Jacob Northey',
    maintainer_email='support@lasalletech.com',
    url='',
   packages=find_packages('src'), # include all packages under src
    package_dir={'':'src'}, # tell distutils packages are under src
    classifiers=[
        'Development Status :: Alpha',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
     install_requires=['django-tastypie>=0.9.11','django-tastypie-two-legged-oauth'],
)
