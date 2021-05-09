from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name='hal',
	version='0.0.1',
	description='',
	py_modules=["HAL-CA1006"],
	package_dir={'': 'src'},
	long_description=long_description,
	long_description_content_type="text/markdown",
	classifiers=[
		"Development Status :: 3 - Alpha",
		"License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
	],
	url="https://github.com/bradkeifer/HAL-CA1006",
	author="Brad Keifer",
	author_email="bradkeifer@icloud.com",
)
