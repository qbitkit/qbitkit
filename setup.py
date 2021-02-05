from setuptools import find_packages as __findpkg__
from setuptools import setup as __setup__


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__setup__(
    name="qbitkit",
    version="origin",
    author="qbitkit Team",
    author_email="brianlechthaler@protonmail.ch",
    description="Quantum Computing, for Humans.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qbitkit/qbitkit",
    packages=__findpkg__(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
