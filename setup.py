from pathlib import Path
from typing import List
from setuptools import find_packages, setup

Hyphen_dot_e = "-e ."
def get_requirements(filepath:Path)->List[str]:

    with open(filepath, "r") as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if Hyphen_dot_e in requirements:
            requirements.remove(Hyphen_dot_e)
    
    return requirements


setup(
    name = "chicken-disease",
    version= "0.0.1",
    author ="mbali094",
    author_email ="mbalinene094@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)