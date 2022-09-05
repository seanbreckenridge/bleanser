import io
from setuptools import setup, find_namespace_packages

# Use the README.md content for the long description:
with io.open("README.md", encoding="utf-8") as fo:
    long_description = fo.read()

pkg = "bleanser_sean"
setup(
    name=pkg,
    version="0.1.0",
    url="https://github.com/seanbreckenridge/bleanser",
    author="Sean Breckenridge",
    author_email="seanbrecke@gmail.com",
    description="my bleanser modules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_namespace_packages("src"),
    package_data={pkg: ["py.typed"]},
    package_dir={"": "src"},
    install_requires=[],
    python_requires=">=3.8",
    keywords="data",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
