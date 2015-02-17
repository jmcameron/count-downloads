"""
Parse Apache access log files and construct a list of unique downloads

By: Jonathan M. Cameron

Copyright (c) 2015 Jonathan M. Cameron
License: http://www.gnu.org/licenses/gpl-2.0.html GNU/GPL

"""
import re
import apache_log_parser


class downloads:
    """
    The downloads class

    >>> from pprint import pformat
    >>> d = downloads([r'.*/([a-zA-Z0-9-_\.]+\.zip)'])
    >>> str = '192.185.83.208 - - [16/Feb/2015:06:43:55 +0000] '
    >>> str += '"GET /mysite/downloads/test.zip HTTP/1.1" 200 605815 "-" "-"'
    >>> data = d.parse(str)

    >>> print pformat(data)
    {'filename': 'test.zip',
     'remote_host': '192.185.83.208',
     'remote_logname': '-',
     'remote_user': '-',
     'request_first_line': 'GET /mysite/downloads/test.zip HTTP/1.1',
     'request_http_ver': '1.1',
     'request_method': 'GET',
     'request_url': '/mysite/downloads/test.zip',
     'response_bytes_clf': '605815',
     'status': '200',
     'time_received': '[16/Feb/2015:06:43:55 +0000]',
     'time_received_datetimeobj': datetime.datetime(2015, 2, 16, 6, 43, 55),
     'time_received_isoformat': '2015-02-16T06:43:55'}

    """

    def __init__(self, patterns):
        """
        @param log_filenames: list of log files
        @param patterns: list of regular expressions for download filenames to glean
        """

        self._patterns = []
        self._downloads = {}

        for p in patterns:
            self._patterns.append(re.compile(p))

        self._line_parser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %s %b")


    def parse(self, line):
        data = self._line_parser(line)
        data['filename'] = None
        for p in self._patterns:
            m = p.match(data['request_url'])
            if m:
                data['filename'] = m.group(1)
                break   # Accept the first match
        return data


if __name__ == "__main__":
    import doctest
    doctest.testmod()
