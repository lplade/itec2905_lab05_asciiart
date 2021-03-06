from setuptools import setup

setup(
    name="AsciiArt",
    version="0.3",
    description="ASCII art from images",
    author="lplade",
    packages=["asciiart"],
    install_requires=[
        "pillow",
        "requests"
    ]
)
