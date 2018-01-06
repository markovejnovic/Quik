# -*- coding: utf-8 -*-
"""Quik is a module which is intended to speed up the writing of blogs

Quik uses a system of replacing "quik-commands" into other formats. At the
moment, only HTML output is supported.

All quik-commands are denominated by curly braces.

The two key terms in quik are:
    Singulars,
    Containers

Singulars are quik-commands which are replaced into single strings. For
example:
    {TM} -> ™

Containers are quik-commands which are replaced into container-like structures.
For example:
    {sec} -> <div class="quik-section">Content of section</div>
"""

import re

def html_parse(input_str):
    """Does all of the parsing into html form

    Args:
        input_str (str): The string to parse

    Returns:
	str: An html parsed string
    """
    return html_parse_singulars(input_str)

def html_parse_singulars(input_str):
    """Parses only the singulars in an html form
    
    Args:
	input_str (str): The string to parse

    Returns:
	str: An html parsed string
    """
    SUPPORTED_SINGULARS = {
	'TM': '&trade;',
        'R': '&reg;'
    }

    for key, value in SUPPORTED_SINGULARS.iteritems():
        input_str = input_str.replace('{' + key + '}', value)

    return input_str

