from setuptools import find_packages,setup
from typing import List


def get_requirements()->list[str]:
    requirements_list=list[str]=[]
    return requirements_list#return list of strings

setup(
    name='sensor',
    version="0.0.1",
    author="praneeth",
    author_email="praneethapkr1218@gmail.com",
    packages=find_packages(),
    isntall_requires=get_requirements(),
)