#!/usr/bin/env python

from distutils.core import setup
import memcache

setup(name="python-memcached",
      version=memcache.__version__,
      description="Pure python memcached client",
      long_description=open("README").read(),
      author="Evan Martin",
      author_email="martine@danga.com",
      maintainer="Tim Perevezentsev",
      maintainer_email="riffm2005@gmail.com",
      url="http://github.com/riffm/python-memcached",
      py_modules=["memcache"],
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Python Software Foundation License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ])

