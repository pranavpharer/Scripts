from setuptools import setup,find_packages

setup(name='Script_World',
      version='1',
      packages=find_packages(),
      install_requires=['gym>=0.2.3',
                        'networkx==2.5.1']
) 