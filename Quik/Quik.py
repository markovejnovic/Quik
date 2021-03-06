# -*- coding: utf-8 -*-
"""Quik is a module which is intended to speed up the writing of blogs

Quik uses a system of replacing "quik-commands" into other formats. At the
moment, only HTML output is supported.

All quik-commands are denominated by curly braces.
When discussing these commands, the value between the curly braces ({TM}) is
called the key, and its transformation (™) is called the value.

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
    return parse_singulars(input_str)


"""
Singular-related functions
"""
SUPPORTED_SINGULARS = {
    'TM': '&trade;',
    'R': '&reg;'
}


def get_singulars():
    """Returns the parsable singulars

    Returns:
        dict: The parsable singulars dictionary
    """
    return SUPPORTED_SINGULARS


def set_singulars(sing_dict):
    """Sets the parsable singulars

    Args:
        sing_dict (dict): The new parsable singulars dictionary
    """
    if type(sing_dict) is dict:
        global SUPPORTED_SINGULARS

        for key, value in sing_dict.iteritems():
            if (not isinstance(key, basestring) or not
                    isinstance(value, basestring)):
                raise AttributeError(
                    "set_singulars does not accept non-strings.")

        SUPPORTED_SINGULARS = sing_dict
    else:
        raise AttributeError("set_singulars() requires a dict.")


def add_singular_definition(key, value):
    """Adds a new singular definition to the parsable singulars dictionary

    Args:
        key (str): The singular key
        value (str): The singular value
    """
    SUPPORTED_SINGULARS[key] = value


def parse_singulars(input_str):
    """Parses only the singulars in an html form

    Args:
        input_str (str): The string to parse

    Returns:
        str: An html parsed string
    """

    for key, value in SUPPORTED_SINGULARS.iteritems():
        input_str = input_str.replace('{' + key + '}', value)

    return input_str


def parse_sections(input_str):
    """Parses the sections in the input string to html format
    
    This function will parse all of the sections '{sec}' into html format.
    This format will appear as:
        <div class="quik-section">
            Content
        </div>
    Optionally, if the section has a name ('{sec name}') a <h2> will be created
    inside the div, before the content.

    Args:
        input_str (str): The input string

    Returns:
        str: An html parsed string
    """
    first_sec = True
    output = ""
    split_strings = input_str.splitlines()
    for i, line in enumerate(split_strings):
        line = line.lstrip()
        if "{sec}" in line:
            if not first_sec:
                output += '</div>'
            output += '<div class="quik-section">'
            first_sec = False
        elif "{sec " in line:
            if not first_sec:
                output += '</div>'
            output += '<div class="quik-section">'
            first_sec = False
            output += '<h2 class="quik-section-title">'
            output += re.match(r'{sec (.*)}', line).group(1)
            output += '</h2>'
        else:
            output += line

        if i + 1 == len(split_strings):
            if not first_sec:
                output += '</div>'

    return output


def parse_containers(input_str):
    """Parses only the singulars in an html form

    Args:
        input_str (str): The string to parse

    Returns:
        str: An html parsed string
    """
    return parse_sections(input_str)
