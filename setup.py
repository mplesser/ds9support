from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="azcam-ds9",
    version="21.2.1",
    description="azcam extension for SAO's ds9 image display tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Michael Lesser",
    author_email="mlesser@arizona.edu",
    keywords="",
    packages=find_packages(),
    zip_safe=False,
    url="https://mplesser.github.io/azcam/",
    install_requires=["azcam"],
)
