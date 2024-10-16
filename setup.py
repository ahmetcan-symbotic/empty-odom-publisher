"""This is a module docstring."""

from setuptools import find_packages, setup

package_name = "dummyodom"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="root",
    maintainer_email="root@todo.todo",
    description="TODO: Package description",
    license="TODO: License declaration",
    entry_points={
        "console_scripts": ["dummyodom_node = dummy_odom.publisher_node:main"],
    },
)
