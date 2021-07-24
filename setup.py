from setuptools import setup, find_packages

with open("README.txt", "r") as fh:
	long_description = fh.read()

setup(

    name='robotframework-nageshtestlib',
    version='0.7',
    description='Robotframework library for excel xlsx file format',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/nageshbn1974/test-mylib',
    author='Nagesh B N',
    author_email='nagesh.nagaraja@gmail.com',
    packages=find_packages(),
    install_requires=['openpyxl']
    
)
