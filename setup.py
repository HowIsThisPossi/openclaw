from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="openclaw",
    version="0.1.0",
    author="HowIsThisPossi",
    description="A powerful command-line tool for managing and organizing your projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HowIsThisPossi/openclaw",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "click>=8.0.0",
        "requests>=2.28.0",
    ],
    entry_points={
        "console_scripts": [
            "openclaw=openclaw.cli:main",
        ],
    },
)
