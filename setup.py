from setuptools import setup

setup(
    name='nose-growl',
    version='0.0.1',
    py_modules=['growl'],
    install_requires=['gntp', 'nose'],
    entry_points = {
        'nose.plugins': [
            'growl = growl:NoseGrowl'
        ]
    }
)
