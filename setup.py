import os
from setuptools import setup

# Utility function to cat in a file (used for the README)
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "yotta",
    version = "0.0.5",
    author = "James Crosby",
    author_email = "James.Crosby@arm.com",
    description = ("Re-usable components for embedded software."),
    license = "Proprietary",
    keywords = "embedded package module dependency management",
    url = "about:blank",
    packages=['yotta', os.path.join('yotta','lib')],
    long_description=read('readme.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: Proprietary",
        "Environment :: Console",
    ],
    entry_points={
        "console_scripts": [
            "yotta=yotta:main",
               "yt=yotta:main",
        ],
    },
    test_suite = 'test',
    install_requires=['semantic_version', 'watchdog', 'restkit', 'PyGithub', 'colorama']
)
