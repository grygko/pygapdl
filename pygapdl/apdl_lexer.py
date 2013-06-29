"""
    APDL lexer
"""
    
import re

from pygments.lexer import RegexLexer, include, bygroups, using, \
     this, combined, ExtendedRegexLexer
from pygments.token import Error, Punctuation, Literal, Token, \
     Text, Comment, Operator, Keyword, Name, String, Number, Generic
from pygments.util import get_bool_opt


class APDLLexer(RegexLexer):
    name = 'apdl'
    aliases = ['apdl']
    filenames = ['*.mac']

    tokens = {
        'root': [
            (r'!.*', Comment),
            (r'^.+?=[^!\n]+', Text),
            (r'^\*(do|DO|enddo|ENDDO)', String),
            (r'^[\t\* /]*[a-zA-Z0-9 ]+', Keyword),
            (r'^\(.*\).*', String),
            (r',[^!\n]*', Operator),
        ]
    }
