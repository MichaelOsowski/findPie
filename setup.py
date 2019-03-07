from setuptools import setup

setup(
    name='PieFinder',
    version='1.0',
    packages=['yourapplication'],
    include_package_data=True,
    zip_safe=True,
    install_requires=['Flask']
)