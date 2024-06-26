import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "text-Summarizer-"
AUTHOR_USER_NAME = "Pratik-0306"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "pratik.borse0306@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author_email=AUTHOR_EMAIL,
    author=AUTHOR_USER_NAME,
    description="A small python package for CNN app",
    Long_description=long_description,
    Long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_URLS={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",      
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)