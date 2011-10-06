from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='tg2.signals',
      version=version,
      description="Adds AMQP consumer middleware to TurboGears",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='amqp, turbogears, tg2, middleware, qpid',
      author='Greg Jurman',
      author_email='gdj2214@rit.edu',
      url='https://github.com/gregjurman/tg2.signals.git',
      namespace_packages = ['tg2'],
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        # -*- Extra requirements: -*-
        "TurboGears2 >= 2.1",
        'sqlalchemy',
        'transaction',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
