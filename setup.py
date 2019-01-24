"""Setup unladen_swallow."""

from setuptools import setup

setup(
    name="UnladenSwallow",
    version="1.0",
    packages=['unladen_swallow'],
    install_requires=[
        "sphinx",
    ],
    author="Karl Saint Lucy",
    author_email="karl@karlsaintlucy.com",
    description=(
        "This package returns the airspeed velocity of an unladen swallow."
    ),
    license="BSD",
    keywords="monty python unladen swallow airspeed velocity",
    url="https://unladen-swallow.readthedocs.io/en/latest/",
)
