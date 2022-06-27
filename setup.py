from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gym_management/__init__.py
from gym_management import __version__ as version

setup(
	name="gym_management",
	version=version,
	description="GYM Management",
	author="Nihantra C. Patel",
	author_email="n.patel.serpentcs@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
