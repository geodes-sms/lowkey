from distutils.core import setup

setup(name='lowkey',
    version='0.1',
    description='lowkey framework',
    author='Istvan David',
    author_email='david.istvan.mail@gmail.com',
    url='https://www.python.org/sigs/distutils-sig/',
    packages=['collabtypes', 'lww', 'network'],
    package_dir={'collabtypes':'../lowkey', 'lww':'../lowkey', 'network':'../lowkey'},
    include_package_data=True,
    install_requires=[],
    license='GNU General Public License v3.0'
)