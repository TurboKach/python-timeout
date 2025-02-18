from setuptools import setup

setup(
    name='python-timeout',
    packages=['timeout'],
    install_requires=['python-printr'],
    version='3.8',
    description='Random timeout between minimum and maximum values',
    url='https://github.com/xjxckk/python-timeout/',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
