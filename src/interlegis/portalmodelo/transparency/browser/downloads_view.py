# -*- coding: utf-8 -*-
from five import grok
from interlegis.portalmodelo.transparency.config import EXTENSIONS_TYPES
from interlegis.portalmodelo.transparency.interfaces import ICSVData
from Products.Five.browser import BrowserView
from zope.component import getMultiAdapter

import rows


class DownloadCSVView(BrowserView):
    """Process the table with all data as CSV file.
    """
    grok.context(ICSVData)

    def __call__(self):
        view = getMultiAdapter((self.context, self.request), name='view')
        table = view.table()
        filename = "%s.csv" % view.filename_prefix()
        data = rows.export_to_csv(table)
        self.request.response.setHeader('Content-Type', '"%s"' % EXTENSIONS_TYPES.get('csv'))
        self.request.response.setHeader('Content-Disposition', 'attachment; filename="%s"' % filename)
        return data


class DownloadJSONView(BrowserView):
    """Process the table with all data as JSON file.
    """
    grok.context(ICSVData)

    def __call__(self):
        view = getMultiAdapter((self.context, self.request), name='view')
        table = view.table()
        filename = "%s.json" % view.filename_prefix()
        data = rows.export_to_json(table)
        self.request.response.setHeader('Content-Type', '"%s"' % EXTENSIONS_TYPES.get('json'))
        self.request.response.setHeader('Content-Disposition', 'attachment; filename="%s"' % filename)
        return data


class DownloadXLSView(BrowserView):
    """Process the table with all data as XLS file.
    """
    grok.context(ICSVData)

    def __call__(self):
        view = getMultiAdapter((self.context, self.request), name='view')
        table = view.table()
        filename = "%s.xls" % view.filename_prefix()
        data = rows.export_to_html(table)
        self.request.response.setHeader('Content-Type', '"%s"' % EXTENSIONS_TYPES.get('xls'))
        self.request.response.setHeader('Content-Disposition', 'attachment; filename="%s"' % filename)
        return data


class DownloadHTMLView(BrowserView):
    """Process the table with all data as HTML file.
    """
    grok.context(ICSVData)

    def __call__(self):
        view = getMultiAdapter((self.context, self.request), name='view')
        table = view.table()
        filename = "%s.html" % view.filename_prefix()
        data = rows.export_to_html(table)
        self.request.response.setHeader('Content-Type', '"%s"' % EXTENSIONS_TYPES.get('html'))
        self.request.response.setHeader('Content-Disposition', 'attachment; filename="%s"' % filename)
        return data


class DownloadTXTView(BrowserView):
    """Process the table with all data as TXT file.
    """
    grok.context(ICSVData)

    def __call__(self):
        view = getMultiAdapter((self.context, self.request), name='view')
        table = view.table()
        filename = "%s.txt" % view.filename_prefix()
        data = rows.export_to_txt(table)
        self.request.response.setHeader('Content-Type', '"%s"' % EXTENSIONS_TYPES.get('text'))
        self.request.response.setHeader('Content-Disposition', 'attachment; filename="%s"' % filename)
        return data
