from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='morseJapanese',
    version='0.1',
    author="takahiro fukushima",
    author_email="takahiro0626fukushima@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    py_modules=["morseJapanese"],
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
