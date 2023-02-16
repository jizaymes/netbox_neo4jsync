from setuptools import find_packages, setup

setup(
    name='netbox-neo4jsync',
    version='0.1',
    description='Tools to synchronize data from Netbox into Neo4j',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)