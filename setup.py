"""
Setup script
"""
from distutils.core import setup

setup(
    name='changepy',
    version='0.1',
    description='Changepoint detection on time series, in Python',
    author='Rui Gil',
    author_email='ruipgil@gmail.com',
    url='https://github.com/ruipgil/changepy',
    packages=['distutils', 'distutils.command'],
    download_url='https://github.com/ruipgil/changepy/archive/master.zip',
    keywords=['changepoint', 'timeseries', 'time', 'series', 'math', 'stats', 'probabilities'],
    classifiers=[],
    install_requires=['numpy']
)
