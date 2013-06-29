"""
    Pygments highlighter for APDL
"""

from setuptools import setup

entry_points={
      'pygments.lexers': ['release = pygapdl.apdl_lexer:APDLLexer', ]
}

setup(
    name         = 'pygapdl',
    version      = '0.1',
    packages     = ['pygapdl'],
    install_requires = ['Pygments'],
    description  = __doc__,
    author       = "gk",
    entry_points = entry_points
) 
