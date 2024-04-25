from setuptools import setup, find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(filename:str)-> List[str]: 
    '''
    This function reads the requirements.txt file and returns a list of requirements.
    '''
    requirements = []
    with open(filename, 'r') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


setup(
    name = "testproj",
    version = "0.1",
    author = "Gowtham",
    author_email = "gowtham26g@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'),
)