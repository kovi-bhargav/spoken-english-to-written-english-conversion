import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
	  name = 'spoken2written',
      packages = ['spoken2written'],
      version='0.1',
      license=open('LICENSE.txt').read(),
      description='Convert Spoken English given as text to Written English ',
      author='Kovi Bhargav',
      author_email='bhargavchowdaryk26@gmail.com',
      url='https://github.com/kovi-bhargav/spoken-english-to-written-english-conversion',
      classifiers = [
     					 'Intended Audience :: Developers',
      					'Programming Language :: Python'
  				],
	  long_description=open_file('README.rst').read()

     )
