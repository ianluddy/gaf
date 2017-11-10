from setuptools import setup

setup(
    name='gaf',
    version='1.0',
    long_description=__doc__,
    packages=['gaf'],
    url='ianluddy@gmail.com',
    author_email='ianluddy@gmail.com',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "flask",
        "flask_autodoc",
        "flask_pymongo",
        "crontab",
        "requests",
        "unittest2"
    ],
    entry_points={
        'console_scripts': [
            'gaf = gaf:run',
        ]
    }
)