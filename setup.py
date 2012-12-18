"""`version` lives on `GitHub <http://github.com/halst/version/>`_."""
from setuptools import setup

from version import __version__


setup(
    name='version',
    version=__version__,
    author='Vladimir Keleshev',
    author_email='vladimir@keleshev.com',
    description='Implementation of semantic version',
    license='MIT',
    keywords='semver semantic version versioning versions',
    url='http://github.com/halst/version',
    py_modules=['version'],
    long_description=__doc__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities'
    ]
)
