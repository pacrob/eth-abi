#!/usr/bin/env python
from setuptools import (
    find_packages,
    setup,
)

HYPOTHESIS_REQUIREMENT = "hypothesis>=6.22.0,<6.108.7"

extras_require = {
    "dev": [
        "build>=0.9.0",
        "bump_my_version>=0.19.0",
        "ipython",
        "mypy==1.10.0",
        "pre-commit>=3.4.0",
        "tox>=4.0.0",
        "twine",
        "wheel",
    ],
    "docs": [
        "sphinx>=6.0.0",
        "sphinx-autobuild>=2021.3.14",
        "sphinx_rtd_theme>=1.0.0",
        "towncrier>=24,<25",
    ],
    "test": [
        "pytest>=7.0.0",
        "pytest-timeout>=2.0.0",
        "pytest-xdist>=2.4.0",
        "pytest-pythonpath>=0.7.1",
        "eth-hash[pycryptodome]",
        HYPOTHESIS_REQUIREMENT,
    ],
    "tools": [
        HYPOTHESIS_REQUIREMENT,
    ],
}

extras_require["dev"] = (
    extras_require["dev"] + extras_require["docs"] + extras_require["test"]
)


with open("./README.md") as readme:
    long_description = readme.read()


setup(
    name="eth_abi",
    # *IMPORTANT*: Don't manually change the version here. See Contributing docs for the release process.
    version="5.1.0",
    description="""eth_abi: Python utilities for working with Ethereum ABI definitions, especially encoding and decoding""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="The Ethereum Foundation",
    author_email="snakecharmers@ethereum.org",
    url="https://github.com/ethereum/eth-abi",
    include_package_data=True,
    install_requires=[
        "eth-utils>=2.0.0",
        "eth-typing>=3.0.0",
        "parsimonious>=0.10.0,<0.11.0",
    ],
    python_requires=">=3.8, <4",
    extras_require=extras_require,
    py_modules=["eth_abi"],
    license="MIT",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["scripts", "scripts.*", "tests", "tests.*"]),
    package_data={"eth_abi": ["py.typed"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)
