#!/usr/bin/env python3
"""
Setup script for Jules programming language
"""

from setuptools import setup, find_packages

setup(
    name="jules-language",
    version="0.1.0",
    description="Jules Programming Language - A friendly language for beginners",
    author="Jules Team",
    author_email="jules@example.com",
    url="https://github.com/jules/jules-language",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'jules=jules:main',
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Interpreters",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
) 