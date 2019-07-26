import os
import sys
from setuptools import setup, find_packages

install_requires = [
    
]

if sys.version_info[:2] < (3, 5):
    raise RuntimeError("Python version >=3.5 required.")

version_py = os.path.join(os.path.dirname(
    __file__), 'scnn', 'version.py')
version = open(version_py).read().strip().split(
    '=')[-1].replace('"', '').strip()

readme = open('README.md').read()

setup(name='scnn',
      version=version,
      description='scnn',
      author='',
      author_email='',
      packages=find_packages(),
      license='MIT License',
      install_requires=install_requires,
      test_suite='nose2.collector.collector',
      long_description=readme,
      long_description_content_type='text/markdown',
      url='https://github.com/KrishnaswamyLab/scnn',
      download_url="https://github.com/KrishnaswamyLab/scnn/archive/v{}.tar.gz".format(
          version),
      keywords=['big-data',
                'deep-learning',
                'computational-biology'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Framework :: Jupyter',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
      ]
      )
