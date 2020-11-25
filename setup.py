import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="couch_potato",
    version="0.0.1",
    author="Peerplays Community",
    description="python-cp cli for Peerplays",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://peerplays.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
