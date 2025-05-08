from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_name",
    version="0.0.1",
    author="Zoe Santos",
    author_email="zmmateus2@gmail.com",
    description="My first application of image processing with python language",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_linkhttps://github.com/Zoemateus324/processador-de-imagem"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)