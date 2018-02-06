import re

from graphene import ObjectType
from textblob import Word

def to_camel_case(name):
    return ''.join(x.capitalize() or '_' for x in name.split('_'))


def to_underscore(name):
    s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()


def to_singular(word):
    return str(Word(word).singularize())


def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z


def ClassFactory(name, fields, BaseClass=ObjectType):
    """
    https://stackoverflow.com/a/15247892/9041712
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key not in argnames:
                raise TypeError("Argument %s not valid for %s"
                    % (key, self.__class__.__name__))
            setattr(self, key, value)
        BaseClass.__init__(self, name[:-len("Class")])
    newclass = type(name, (BaseClass,), merge_two_dicts({"__init__": __init__}, fields))
    return newclass

