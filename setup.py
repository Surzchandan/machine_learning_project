from setuptools import setup
from typing import List


#Declaring variables for setup functions
PROJECT_NAME="HOUSING-PREDICTOR"
VERSION="0.0.1"
AUTHOR="Suraj-chandan"
DESCRIPTION="Housing price predictor ML Project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:

    """ 
    Description: This function

    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
packages=PACKAGES,
install_reuires=get_requirements_list()
)


