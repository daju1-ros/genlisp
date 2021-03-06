#!/usr/bin/env python

from setuptools import setup
import sys
from xml.etree.ElementTree import ElementTree

try:
    root = ElementTree(None, 'stack.xml')
    version = root.findtext('version')
except Exception, e:
    print >> sys.stderr, 'Could not extract version from your stack.xml:\n%s' % e
    sys.exit(-1)

sys.path.insert(0, 'src')

setup(name = 'genlisp',
      version = version,
      packages = ['genlisp'],
      package_dir = {'': 'src'},
      install_requires = ['genmsg'],
      scripts = ['scripts/gen_lisp.py'],
      author = "Bhaskara Marthi",
      author_email = "bhaskara@willowgarage.com",
      url = "http://www.ros.org/wiki/genlisp",
      download_url = "http://pr.willowgarage.com/downloads/genlisp/",
      keywords = ["ROS"],
      classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License" ],
      description = "ROS msg/srv Lisp generation",
      long_description = """\
Library and scripts for generating ROS message data structures in LISP.
""",
      license = "BSD"
      )
