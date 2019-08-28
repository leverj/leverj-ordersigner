import json
import sys
import subprocess
from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

with open('package.json') as f:
    package_json = json.loads(f.read())
version = package_json['version']
name = package_json['name']


def yarn():
    subprocess.run('yarn install --production=true'.split())


class PostDevelopCommand(develop):
    def run(self):
        yarn()
        develop.run(self)


class PostInstallCommand(install):
    def run(self):
        yarn()
        install.run(self)


setup(
    name=name,
    version=version,
    description='Python bridge for Leverj.io Spot Exchange',
    long_description='a python bridge to javascript libraries for Leverj.io Spot Exchange',
    author='leverj',
    url='http://leverj.io',
    license='MIT',
    packages=find_packages(exclude=['tests', 'tests.*']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.0',
    cmdclass={'develop': PostDevelopCommand, 'install': PostInstallCommand},
    install_requires=['setuptools'],
    setup_requires=['nose'],
    extras_require={'dev': ['nose']},
    package_data={f'{name}': ['api.js']},
    data_files=[('', ['package.json', 'yarn.lock'])],
    test_suite='nose.collector',
    entry_points={'console_scripts': [f'run_js={name}:run_js']},
    project_urls={'Source': f'https://github.com/leverj/{name}'}
)
