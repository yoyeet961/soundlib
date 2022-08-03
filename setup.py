from setuptools import setup, find_packages
import codecs
import os


VERSION = '1.0.0'
DESCRIPTION = 'A bunch of sounds that you can use in your own projects.'
LONG_DESCRIPTION = 'A bunch of sounds that you can use in your own projects. For example - soundlib.beep() to play a beep sound.'

# Setting up
setup(
    name="soundlib",
    version=VERSION,
    author="Defacube",
    author_email="none",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['playsound', 'subprocess', 'sys'],
    keywords=['python', 'sound', 'beep', 'soundlib'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)