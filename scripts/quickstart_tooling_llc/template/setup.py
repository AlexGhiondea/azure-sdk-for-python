#!/usr/bin/env python

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------


import os
import re

from setuptools import setup, find_packages


# Change the PACKAGE_NAME only to change folder and different name
PACKAGE_NAME = "{{ package_name }}"
PACKAGE_PPRINT_NAME = "{{ package_pprint_name }}"

# a-b-c => a/b/c
package_folder_path = PACKAGE_NAME.replace("-", "/")


# Version extraction inspired from 'requests'
with open(os.path.join(package_folder_path, "_version.py"), "r") as fd:
    version = re.search(
        r'^VERSION\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
    ).group(1)

if not version:
    raise RuntimeError("Cannot find version information")

setup(
    name=PACKAGE_NAME,
    version=version,
    description="Microsoft {} Client Library for Python".format(PACKAGE_PPRINT_NAME),
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    license="MIT License",
    author="Microsoft Corporation",
    author_email="azpysdkhelp@microsoft.com",
    url="https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/{{ folder_parent }}/{{ package_name }}",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
    zip_safe=False,
    packages=find_packages(
        exclude=[
            # Exclude packages that will be covered by PEP420 or nspkg
            "azure",
            "azure.{{ folder_second }}",
        ]
    ),
    install_requires=[
        "azure-core<2.0.0,>=1.19.1",
        "msrest>=0.6.21",
        'six>=1.11.0',
    ],
    extras_require={
        ":python_version<'3.0'": ["futures", "{{ folder_first }}-{{ folder_second }}-nspkg"],
        ":python_version<'3.5'": ["typing"],
    },
)
