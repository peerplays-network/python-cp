import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="couch_potato",
    version="0.0.1",
    author="PBSA",
    description="python-cp cli for Peerplays",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://peerplays.com",
    packages=[
        "couch_potato"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'couch_potato = couch_potato.cp_local:main',
        ],
    },
    python_requires='>=3.6'
)
