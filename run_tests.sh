#!/bin/bash
# Unit tests
echo 'Running unit tests...'
python2 -m unittest discover
echo 'Unit tests done.'

# PEP8 code style tests
echo 'Running PEP8 code style tests...'
pycodestyle Quik/ test/
echo 'PEP8 code style tests done.'
