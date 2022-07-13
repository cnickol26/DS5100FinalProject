from setuptools import setup

setup(
    name = 'DS5100FinalProject',
    version = '0.1.0',
    author = 'Connor Nickol',
    author_email = 'can2hr@virginia.edu',
    packages = ['DS5100FinalProject'],
    url = 'https://github.com/cnickol26/DS5100FinalProject',
    license = 'MIT',
    description = 'A package for montecarlo simulation',
    install_requires = [
        "pandas",
        "numpy",
        "matplotlib,
    ],
)