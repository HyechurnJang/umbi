import os
from setuptools import setup

def read(fname): return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='umbi',
    version='0.1.0',
    license='Apache 2.0',
    author='Hyechurn Jang',
    author_email='hyjang@cisco.com',
    url='https://github.com/HyechurnJang/umbi',
    description='Cisco Umbrella Investigate CLI',
    long_description=read('README'),
    packages=['umbi'],
    install_requires=['jzlib', 'requests'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ]
)
