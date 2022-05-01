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

# +
# default_exp core
# -

# # wcsfile
#
# > Implements `wcsfile.read()` for reading World Coordinate System information from a file

# %load_ext autoreload
# %autoreload 2

#hide
from nbdev.showdoc import *
from fastcore.test import *

#exports
import toml


#exports
def read(wcsfile: str) -> dict: 
    "Read WCS (key,value) pairs from DS9's *.wcs files"
    with open(wcsfile) as stream:
        return toml.loads(_fixups(stream.read()))


# ## Internal functions
#
# These are not part of the API.  

#export
def _fixups(s: str) -> str:
    "Apply fixes to WCS file syntax to make it valid TOML"
    s = s.replace("0.\n", "0.0\n")
    return s


# ## Example of usage
#

wcs = read("testdata/mosaic-1996-HH204-align-robberto.wcs")
wcs

assert wcs["CDELT2"] == 0.0

test_eq(wcs["EQUINOX"], 2000)

# Try a failing test

# +
#test_eq(wcs["CD2_2"], 0.0)
# -

# # Export modules from notebook

from nbdev.export import notebook2script; notebook2script()







