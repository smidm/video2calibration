#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

# from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='video2calibration',
    version='0.0.0',
    license='MIT',
    description='OpenCV camera calibration from a video',
    long_description=re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.md')),
    long_description_content_type='text/markdown',
    author='Matěj Šmíd',
    author_email='m@matejsmid.cz',
    url='https://github.com/smidm/video2calibration',
    # packages=find_packages('src'),
    # package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities',
    ],
    project_urls={
        # 'Changelog': 'https://github.com/smidm/video2calibration/blob/master/CHANGELOG.md',
        'Issue Tracker': 'https://github.com/smidm/video2calibration/issues',
    },
    # keywords=[
    #     # eg: 'keyword1', 'keyword2', 'keyword3',
    # ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'PyYAML',
        'opencv-python-headless',
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    scripts=[
        'calibrate.py',
        'undistort.py'
    ],
    # entry_points={
    #     'console_scripts': [
    #         'calibrate = video2calibration.cli:main',
    #     ]
    # },
)
