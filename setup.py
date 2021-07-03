from distutils.core import setup

setup(name='lowkey',
    version='0.1',
    description='lowkey framework',
    packages=['collabtypes', 'lww', 'network'],
    package_dir={'collabtypes':'../lowkey', 'lww':'../lowkey', 'network':'../lowkey'},
    include_package_data=True,
    install_requires=[])