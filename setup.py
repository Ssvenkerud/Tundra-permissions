from setuptools import setup

setup(
    name='tundra',
    version='0.1.0',
    py_modules=['tundra'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'tundra = tundra:cli',
        ],
    },
)
