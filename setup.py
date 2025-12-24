from setuptools import find_packages, setup
from typing import List

def get_requirements(filepath: str)->List:
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    return requirements
    

setup(
    name = "ML Project with deployment on Cloud",
    version = "0.0.1",
    author = "ShivajiM",
    author_email = "maneshiva92@gmail.com",
    packages=find_packages(),
    install_requires = ['pandas', 'numpy', 'seaborn']
)