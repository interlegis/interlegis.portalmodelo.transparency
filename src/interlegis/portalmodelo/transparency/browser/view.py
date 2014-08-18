# -*- coding: utf-8 -*-
from five import grok
from interlegis.portalmodelo.transparency import rows
from interlegis.portalmodelo.transparency.interfaces import ICSVData

import StringIO

grok.templatedir('templates')


class View (grok.View):

    """CSVData View"""

    grok.context(ICSVData)

    def _file(self):
        """Return context file to be handled."""
        file_data = self.context.file
        return file_data

    def _file_data(self):
        """Return the data in the file."""
        file_data = self._file()
        return file_data.data

    def filename(self):
        """Return content type."""
        file_data = self._file()
        return file_data.filename

    def doc_type(self):
        """Return content type."""
        return 'text/csv'

    def period(self):
        """Return period of this info."""
        start_date = self.context.start_date
        end_date = self.context.end_date
        if not (start_date and end_date):
            return None
        start_date = start_date.strftime('%d/%m/%Y')
        end_date = end_date.strftime('%d/%m/%Y')
        return u'{0} até {1}'.format(start_date, end_date)

    def display_size(self):
        """Return content type."""
        file_data = self._file_data()
        bytes_ = len(file_data)
        if bytes_ > 1024:
            unit = 'Kb'
            data = bytes_ / 1024.0
            display_size = '{0:.1f} {1}'.format(data, unit)
        else:
            unit = 'bytes'
            data = bytes_
            display_size = '{0} {1}'.format(data, unit)
        return display_size

    def number_of_records(self):
        """Returns the number of lines in the file."""
        file_data = self._file_data()
        eol = '\n'
        if '\r\n' in file_data:
            eol = '\r\n'
        lines = file_data.split(eol)
        # Header should not be counted
        return len(lines) - 1

    def table(self):
        """Returns the table with all data."""
        file_data = self._file_data()
        csv = StringIO.StringIO(file_data)
        my_table = rows.import_from_csv(csv)
        data = my_table.export_to_html()
        # Add class to the table
        data = data.replace('<table>', '<table class="listing">')
        return data
