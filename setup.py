from setuptools import find_packages as __findpkg__
from setuptools import setup as __setup__
from subprocess import run as __run__
from os import linesep as __ls__


def __cmd_runner__(cmd=None):
    cmd_result = __run__(cmd,
                         capture_output=True)
    stdout_raw = cmd_result.stdout
    return stdout_raw
def __process_stdout__(stdout=None):
    stdout_str = str(stdout.decode('utf-8'))
    stdout_fix = stdout_str.strip(__ls__)
    return stdout_fix
def __get_branch_name__(self=None):
    git_cmd = ["git", "rev-parse",
               "--abbrev-ref", "HEAD"]
    stdout_raw = __cmd_runner__(git_cmd)
    stdout_fixed = __process_stdout__(stdout_raw)
    return stdout_fixed



with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__setup__(
    name="qbitkit",
    version=__get_branch_name__(),
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
