from setuptools import find_packages,setup
from typing import List

hypen_e_dot ='-e.'
def get_requirements(file_path:str)->List[str]:
    get_requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    if hypen_e_dot in requirements:
        requirements.remove(hypen_e_dot)
    return requirements

setup(
    name='fault detection',
    version = '0.0.1',
    author = 'imran',
    author_email='dhamangetejas@gmail.com',
    install_reuirements =get_requirements('requirements.txt'),
    packages=find_packages()

)

#just update