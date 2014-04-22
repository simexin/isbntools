# -*- coding: utf-8 -*-

from .helpers import normalize_space, titlecase
from .exceptions import NotValidMetadataError

# For now you cannot add custom fields!
FIELDS = ('ISBN-13', 'Title', 'Authors', 'Publisher', 'Year', 'Language')


class Metadata(object):
    """
    Class for metadata objects
    """

    def __init__(self, record=None):
        """
        Initializer
        """
        self._content = None
        self._set_empty()
        if record:
            self._content.update((k, v) for k, v in record.items())
            if not self._validate():
                self._set_empty()
                raise NotValidMetadataError()
            self.clean()

    @staticmethod
    def fields():
        """
        Return a list of fields (names/headers/keys) of value
        """
        return list(FIELDS)

    def clean(self, broom=normalize_space, filtre=()):
        """
        Clean fields of value
        """
        self._content.update((k, broom(v)) for k, v
                             in self._content.items()
                             if k != 'Authors' and k not in filtre)
        if 'Authors' not in filtre:
            self._content['Authors'] = [broom(i) for i in
                                        self._content['Authors']]
        if self._content['Language'].lower() in ('en', 'eng', 'english'):
            self._content['Title'] = titlecase(self._content['Title'])

    @property
    def value(self):
        """
        Get value
        """
        return self._content

    @value.setter
    def value(self, record):
        """
        Sets value
        """
        self._content.update((k, v) for k, v in record.items())
        if not self._validate():
            self._set_empty()
            raise NotValidMetadataError()
        self.clean()

    @value.deleter
    def value(self):
        """
        Deletes value
        """
        self._set_empty()

    def merge(self, record, overwrite=(), overrule=lambda x: x == ''):
        """
        Merge the record with value
        """
        # by default do nothing
        self._content.update((k, v) for k, v in record.items()
                             if k in overwrite and not overrule(v) or
                             self._content[k] == '')
        if not self._validate():
            self._set_empty()
            raise NotValidMetadataError()
        self.clean()

    def _validate(self):
        """
        Validates value
        """
        # 'minimal' check
        for k in self._content:
            if not type(self._content[k]) is unicode:
                if k != 'Authors':
                    return False
        if not type(self._content['Authors']) is list:
            return False
        return True

    def _set_empty(self):
        """
        Sets an empty value record
        """
        self._content = dict.fromkeys(list(FIELDS), u'')
        self._content['Authors'] = [u'']


def stdmeta(records):
    """
    Function API to the class
    """
    dt = Metadata(records)
    return dt.value
