from setuptools import setup

APP_NAME = 'Gravity falls'
APP = ['converter_planet.py']
DATA_FILES = [('image', ['img/*.png'])]
OPTIONS = {'argv_emulation': True}

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)