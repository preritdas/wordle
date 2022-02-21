from setuptools import setup, find_packages

VERSION = "1.8.1"
DESCRIPTION = (
    "The popular word game recreated in Python, deployable with custom answers."
)

def getReadMe():
    with open("README.md", "r") as f:
        return f.read()

# Setting up
setup(
    name="wordle-python",
    version=VERSION,
    author="Prerit Das",
    author_email="<preritdas@gmail.com>",
    description=DESCRIPTION,
    long_description=getReadMe(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["requests==2.27.1"],
    keywords=["python", "games", "wordle", "english", "word games"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
