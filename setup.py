
import setuptools

setuptools.setup(
    name='mydataflow',
    version='0.0.1',
    author='Vinodkumar M',
    author_email='smvinodkumar910@gmail.com',
    description='Mydataflow to run jobs in GCP',
    install_requires=['apache-beam==2.35.0',],
    package_data={'mydataflow.resources': ['*.json']},
    include_package_data=True,
    packages=setuptools.find_packages(),
    )