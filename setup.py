from setuptools import setup, find_packages

__version__ = None
with open('src/sgtkcmd/version.py') as f:
    exec(f.read())

setup(
    name="sgtkcmd",
    version=__version__,
    author="Bohdon Sayre",
    author_email="bohdon@gmail.com",
    description="Command line tools for working with ShotGrid Toolkit.",
    keywords="sgtk shotgrid toolkit command-line build upload package tool",

    package_dir={'': 'src'},
    packages=find_packages('src'),

    install_requires=[
        'pyyaml>=3.0',
    ],

    entry_points={
        'console_scripts': [
            'sgtkcmd = sgtkcmd.__main__:main',
        ]
    }

)
