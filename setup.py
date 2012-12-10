#!/usr/bin/env python

from setuptools import setup

description = "PagerDuty service API client"

setup(
    name="pd",
    version="0.1",
    author="Brian Elliott",
    author_email="bdelliott@gmail.com",
    description=description,
    long_description=description,
    license="Apache",
    keywords="pagerduty pager duty",
    url="https://www.github.com/bdelliott/pd",
    packages=['pd'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    requires=[
        'requests',
    ],

    entry_points = {
        'console_scripts': [
            'pdack = pd.ack:all',
        ]

    }

)
