'Requires a user to be logged in before being able to view the member list'

from setuptools import setup

setup(
    name='flaskbb-plugin-private-memberlist',
    packages=['memberlist'],
    version='1.2',
    author='haliphax',
    author_email='haliphax@github.com',
    description='Require login to view the member list',
    url='https://github.com/haliphax/flaskbb-plugin-private-memberlist',
    long_description=__doc__,
    zip_safe=False,
    platforms='any',
    entry_points={'flaskbb_plugins':
                  ['memberlist = memberlist']},
    classifiers=[
        'Environment :: Web Environment',
        'Environment :: Plugins',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
