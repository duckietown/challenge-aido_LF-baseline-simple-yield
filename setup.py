from setuptools import setup, find_packages


def get_version(filename):
    import ast

    version = None
    with open(filename) as f:
        for line in f:
            if line.startswith("__version__"):
                version = ast.parse(line).body[0].value.s
                break
        else:
            raise ValueError("No version found in %r." % filename)
    if version is None:
        raise ValueError(filename)
    return version


line = "daffy"
install_requires = [
    f"duckietown-world-{line}",
    f"aido-agents-{line}",
    "PyContracts3",
    f"aido-protocols-{line}",
    "zuper-commons-z6",
    "PyYAML",
    "numpy",
]

module = "gtduckie"
package = "gtduckie"
src = "src"

version = get_version(filename=f"src/{module}/__init__.py")

setup(
    name=package,
    package_dir={"": src},
    packages=find_packages("src"),
    version=version,
    zip_safe=False,
    install_requires=install_requires,
)
