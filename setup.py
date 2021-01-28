import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qbitkit",
    version="origin",
    author="qbitkit Team",
    author_email="brianlechthaler@protonmail.ch",
    description="Quantum Computing, for Humans.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qbitkit/qbitkit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
