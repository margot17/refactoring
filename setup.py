
from setuptools import setup, find_packages

setup(
    name = "Bad Boids",
    version = "0.1",
    description='Simulate flocking birds',
    author='Maria Stasinou',
    author_email='stasinoumar@gmail.com',
    license='MIT',
    packages = find_packages(exclude=['*test']),
    install_requires = ['argparse', 'matplotlib', 'numpy', 'mock', 'nose'],
    entry_points={
        'console_scripts': [
            'badboids=boids:main',
        ],
    },
)

Writing setup.py