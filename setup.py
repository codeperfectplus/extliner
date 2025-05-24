from setuptools import setup, find_packages

# Read the long description from README.md
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = (
        "A simple command-line tool to count lines in files by extension. "
        "See the documentation for more details."
    )

# Read the list of requirements from requirements.txt
try:
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        requirements = fh.read().splitlines()
except FileNotFoundError:
    requirements = ["tabulate==0.9.0"]

setup(
    name="extliner",
    version="0.0.1",
    author="Deepak Raj",
    author_email="deepak008@live.com",
    description=(
        "A simple command-line tool to count lines in files by extension, "
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codeperfectplus/extliner",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers"
    ],
    project_urls={
        "Documentation": "https://extliner.readthedocs.io/en/latest/",
        "Source": "https://github.com/codeperfectplus/extliner",
        "Tracker": "https://github.com/codeperfectplus/extliner/issues"
    },
    entry_points={
        "console_scripts": [
            "extliner=extliner.cli:main",  # Update path if needed
        ],
    },
    keywords=[
        "line count",
        "file analysis",
        "command line tool",
        "file extension",
        "python",
        "CLI",
        "file processing",
        
    ],
    license="MIT",
)