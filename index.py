# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # wcsfile
# > Implements `wcsfile.read()` for reading World Coordinate System information from a file.

# Read World Cooordinate System parameters from a `.wcs` file, such as those written by SAOImageDS9.

# ## Install

# `pip install git+https://github.com/will-henney/wcsfile.git`
#
# It needs to be installed from github since it has not been submitted to PyPI yet.

# ## How to use

# Use `wcsfile.read()` to read a WCS file into a python dict. 

import wcsfile
wcsdict = wcsfile.read("testdata/mosaic-1996-HH204-align-robberto.wcs")
wcsdict

# The dict can be used to initialize a FITS header object.

# +
from astropy.io import fits

hdr = fits.Header(wcsdict)
hdr
# -

# Or it can be used to initialize a WCS object.

# +
from astropy.wcs import WCS

w = WCS(wcsdict)
w
# -

assert w.wcs.lattyp == "DEC"

# ## Python Library Dependencies

# - toml
# - astropy (for usage examples and tests only)
