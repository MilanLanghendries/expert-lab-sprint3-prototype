from setuptools import setup, find_packages

setup(
    name="cleanpy_advanced",
    version="0.1.0",
    description="An advanced data-cleaning and profiling library.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.3.0",
        "scikit-learn>=0.24.0",
        "numpy>=1.20.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
