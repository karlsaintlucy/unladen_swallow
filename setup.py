"""Setup unladen_swallow."""

from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="UnladenSwallow",
    version="0.2",
    packages=['unladen_swallow'],
    install_requires=[
        "Sphinx"
    ],
    author="Karl Saint Lucy",
    author_email="karl@karlsaintlucy.com",
    description=(
        "This package returns the airspeed velocity of an unladen swallow."
    ),
    long_description=long_description,
    license="BSD",
    keywords="monty python unladen swallow airspeed velocity",
    url="https://unladen-swallow.readthedocs.io/en/latest/",
)
