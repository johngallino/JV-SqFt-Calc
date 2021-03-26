"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['sqftcalc.py']
DATA_FILES = ['quotes.py']
OPTIONS = {'argv_emulation': True, 'iconfile': 'sqftcalc.icns'}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)