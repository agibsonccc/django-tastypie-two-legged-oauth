import os
 
from distutils.core import setup
from setuptools import setup, find_packages
def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == "":
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)
 
package_dir = "osqa-context"
 
packages = []
for dirpath, dirnames, filenames in os.walk(package_dir):
    # ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith("."):
            del dirnames[i]
    if "__init__.py" in filenames:
        packages.append(".".join(fullsplit(dirpath)))
 
setup(
    name='django-tastypie-two-legged-oauth',
    version='0.1',
    description='',
    keywords='oauth2.0 port for django tastypie',
    license='GNU LESSER GENERAL PUBLIC LICENSE',
    author='Adam Gibson',
    author_email='andy@mrox.net',
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
    
     install_requires=['django-tastypie>=0.9.11'],
  
)
