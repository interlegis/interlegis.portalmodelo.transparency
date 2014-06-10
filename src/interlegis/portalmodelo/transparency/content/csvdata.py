# -*- coding: utf-8 -*-
from DateTime import DateTime
from interlegis.portalmodelo.transparency.interfaces import ICSVData
from five import grok
from plone.indexer.decorator import indexer
from plone.dexterity.content import Container
from z3c.form.validator import SimpleFieldValidator
from zope.interface import Invalid


class CSVData(Container):

    """Dados formatados como CSV."""

    grok.implements(ICSVData)


class CSVValidator(SimpleFieldValidator):

    def validate(self, value):
        """Garantimos que o tipo do arquivo seja CSV."""
        super(CSVValidator, self).validate(value)
        # valida o tipo de arquivo aqui
        if not value.contentType == 'text/csv':
            raise Invalid(u'Formato de arquivo invalido')


@indexer(ICSVData)
def start_date(obj):
    """Converte start_date to DateTime and set hour to 00:00:00."""
    start_date = ICSVData(obj).date
    # Comeco do dia
    start_date = DateTime('%s 00:00:00' % start_date.strftime('%Y-%m-%d'))
    return start_date


@indexer(ICSVData)
def end_date(obj):
    """Converte end_date to DateTime and set hour to 23:59:59."""
    end_date = ICSVData(obj).date
    # Final do dia
    end_date = DateTime('%s 23:59:59' % end_date.strftime('%Y-%m-%d'))

    return end_date
