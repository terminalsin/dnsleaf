from setuptools import setup, find_packages

setup(
    name="dnsleaf",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "click>=7.1.2",
        "aiohttp>=3.7.4"
    ],
    entry_points={
        "console_scripts": [
            "dnsleaf=dnsleaf.cli.main:main",
        ],
    },
    author="terminalsin",
    author_email="shanyujuneja@gmail.com",
    description="A library for flushing DNS caches across multiple providers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/terminalsin/dnsleaf",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
