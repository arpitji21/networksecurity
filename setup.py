from setuptools import find_packages,setup

from typing import List

def get_requirements()-> List[str]:
    requiremnt_lst:List[str] = []
    try:
        
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requiremnt = line.strip()

                if requiremnt and requiremnt!='-e .':
                    requiremnt_lst.append(requiremnt)

    except FileNotFoundError:
        print("requirements.txt file is not exist")

    return requiremnt_lst

print(get_requirements())

setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Arpit Jindal",
    author_email="hackhammer404@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements()
)