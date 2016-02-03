import os
import io
from setuptools import setup

dir = os.path.dirname(__file__)

with io.open(os.path.join(dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='py3_wordsmith',
    version='1.1.1',
    description='API for Wordsmith',
    long_description=long_description,
    url='https://github.com/xACruceSalus/py3_wordsmith',
    author=['Zack Cooper', 'John Hegele'],
    author_email='zackjcooper@gmail.com'
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: MIT License'
        ],
    install_requires=[],
    keywords='wordsmith api',
    packages=['py3_Wordsmith'],
)
