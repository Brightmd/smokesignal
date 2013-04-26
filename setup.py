from setuptools import setup, find_packages
version = '0.0.1'

setup(name='smokesignal',
      version=version,
      description=("Simple python event signaling"),
      classifiers=['Development Status :: 1 - Beta',
                   'Intended Audience :: Python Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities'],
      keywords='python event signal signals signaling',
      author='Shaun Duncan',
      author_email='shaun.duncan@gmail.com',
      url='http://www.github.com/shaunduncan/smokesignal/',
      download_url='https://github.com/shaunduncan/smokesignal/downloads',
      license='MIT',
      packages=find_packages(),
      )