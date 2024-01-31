from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_kanak/__init__.py
from custom_kanak import __version__ as version

setup(
	name="custom_kanak",
	version=version,
	description="Some Extar Customisation",
	author="Kanak Infosystems LLP",
	author_email="sales@kanakinfosystems.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
