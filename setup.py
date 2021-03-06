#!/usr/bin/env python

# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import absolute_import, division, print_function

#
# Standard imports
#
import glob
import os
import sys

#
# setuptools' sdist command ignores MANIFEST.in
#
from distutils.command.sdist import sdist as DistutilsSdist
from setuptools import setup, find_packages
from setuptools.command.install import install as InstallCommand
import py.KITCAT.versioning as ver

class Install(InstallCommand):
    """ Customized setuptools install command which uses pip. """
    def run(self, *args, **kwargs):
        import pip
        pip.main(['install', '.'])
        InstallCommand.run(self, *args, **kwargs)

#
# Begin setup
#
setup_keywords = dict()

#
# THESE SETTINGS NEED TO BE CHANGED FOR EVERY PRODUCT.
#
setup_keywords['name'] = 'KITCAT'
setup_keywords['description'] = 'Kd-tree Implementation for Two-point Correlation AlgoriThm'
setup_keywords['author'] = 'Tri Nguyen, Tolga Yapici'
setup_keywords['author_email'] = 'tnguy51@u.rochester.edu, tyapici@ur.rochester.edu'
setup_keywords['license'] = 'BSD'
setup_keywords['url'] = 'https://github.com/DESI-UR/KITCAT'
setup_keywords['version'] = ver.get_version(out_type='string')
setup_keywords['requires'] = ['Python (>=3.5)']
setup_keywords['zip_safe'] = False
setup_keywords['use_2to3'] = False
setup_keywords['packages'] = find_packages('py')
setup_keywords['package_dir'] = {'': 'py'}
setup_keywords['provides'] = [setup_keywords['name']]
setup_keywords['install_requires'] = []
for line in open("requirements.txt", "r"):
    #package_name, package_version = line.split(">=")
    #if package_name != "scikit-learn":
    #    setup_keywords['requires'].append('{} (>={})'.format(package_name.strip(), package_version.strip()))
    #else:
    setup_keywords['install_requires'].append("{}".format(line))
setup_keywords['cmdclass'] = {'install': Install,}

#
# END OF SETTINGS THAT NEED TO BE CHANGED.
#

# Set other keywords for the setup function.  These are automated, & should
# be left alone unless you are an expert.
#
# Treat everything in bin/ except *.rst as a script to be installed.
#
if os.path.isdir('bin'):
    setup_keywords['scripts'] = [fname for fname in glob.glob(os.path.join('bin', '*'))
        if not os.path.basename(fname).endswith('.rst')]

# Run setup command.
#
setup(**setup_keywords)
