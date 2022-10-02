from setuptools import setup, find_packages
from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    This function will be returning requirements.txt file data.
    """
    with open(REQUIREMENT_FILE_NAME) as rf:
        return rf.readlines().remove("-e .")

#declaring variables for setup function
setup(
    name="housing-predictor",
    version="0.0.2",
    author="Ajay",
    description="",
    packages=find_packages(),# ["housing"],
    install_requires=get_requirements_list()
)