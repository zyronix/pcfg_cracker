from setuptools import setup, find_packages

setup(
    name='pcfg_cracker',
    version='4.6.0',
    author='Matt Weir',
    author_email='cweir@vt.edu',
    description='A collection of tools to perform research into how humans generate passwords. These can be used to crack password hashes, but also create synthetic passwords (honeywords), or help develop better password strength algorithms',
    install_requires='chardet',
    url="https://github.com/lakiw/pcfg_cracker",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages = find_packages("."),
)