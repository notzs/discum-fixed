from setuptools import setup
setup(name='discum-fixed',      
description='discum but fixed',      
long_description=long_description,      
version='0.2.0',      
url='https://github.com/notzs/discum-fixed',      
author='notzs',      
license='Apache2',      

classifiers=[
'Development Status :: 4 - Beta',          
'Intended Audience :: System Administrators',          
'License :: OSI Approved :: Apache Software License',          
'Programming Language :: Python :: 3'],      
packages=['discum-fixed'],      
install_requires=[          
    'PyYAML>=3.11',          
    'sh>=1.11'      
    ],      
    entry_points={          
        'console_scripts': ['encrypt=discum-fixed.main:run']})
