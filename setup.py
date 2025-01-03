from setuptools import find_packages, setup

setup(
    name="tundra",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "tundra=tundra:tundra",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI tool for managing permissions and roles",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/tundra-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
)
