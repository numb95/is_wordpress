# Copyright (c) 2019 amirhossein
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import setuptools
import os
thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="is_wordpress",
    version="0.0.1",
    author="AmirHossein Goodarzi",
    author_email="amir@goodarzi.net",
    description="A simple (or useless) Program to check if a website is based on wordpress or not and if it's on wordpress which version does it use.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/numb95/is_wordpress",
    download_url='https://github.com/numb95/is_wordpress/archive/0.0.1.tar.gz',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
        entry_points = {
        'console_scripts': ['is_wordpress=is_wordpress.cli:main'],
    },install_requires=install_requires,
)