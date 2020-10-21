"""Package setup."""
import io
import re
from setuptools import setup

__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
    io.open("kickeststats/__init__.py", encoding="utf_8_sig").read()
).group(1)

REQUIRED = [req.strip() for req in open('requirements.txt').readlines()]

setup(
    name="kickeststats",
    version=__version__,
    author="Riccardo Vilardi, Matteo Manica",
    packages=[
        "kickeststats", "kickeststats.helpers",
        "kickeststats.tests"
    ],
    long_description=open("README.md").read(),
    package_data={
        "kickeststats": [
            "py.typed",
            "resources/tests/players.jsonl",
            "resources/drivers/chromedriver"
        ]
    },
    install_requires=REQUIRED,
    scripts=["bin/kickeststats-download-data"]
)
