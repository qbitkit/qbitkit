import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qbitkit", # Replace with your own username
    version="0.0.1",
    author="Brian Lechthaler",
    author_email="brianlechthaler@protonmail.ch",
    description="Easy Quantum Computing Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brianlechthaler/qbitkit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)