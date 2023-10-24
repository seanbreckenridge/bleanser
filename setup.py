from setuptools import setup, find_namespace_packages


def main() -> None:
    pkg = "bleanser_sean"
    setup(
        name=pkg,
        packages=find_namespace_packages("src"),
        package_data={pkg: ["py.typed"]},
        package_dir={"": "src"},
    )


if __name__ == "__main__":
    main()
