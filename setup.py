from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.split('#')[0].strip() for req in requirements if req.split('#')[0].strip()]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

    
setup(
    name='mlrepo',
    version='0.0.1',
    author='Deeksha',
    author_email='deeksha.jain2008@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
) 