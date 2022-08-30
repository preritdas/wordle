from setuptools import setup, find_packages

VERSION = "2.3.31"
DESCRIPTION = (
    "The popular word game recreated in Python, deployable with custom answers."
)

def get_read_me():
    with open("README.md", "r") as f:
        return f.read()

# Setting up
setup(
    name="wordle-python",
    version=VERSION,
    author="Prerit Das",
    author_email="<preritdas@gmail.com>",
    description=DESCRIPTION,
    long_description=get_read_me(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=["python", "games", "wordle", "english", "word games"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
