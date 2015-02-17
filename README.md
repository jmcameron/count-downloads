count-downloads
===============

Process a set of Apache access log files and construct a list of downloads.

By: Jonathan M. Cameron

Created: February 16, 2015


PROGRAMS / FILES:

   - Downloads.py - Base parsing class (uses apachge_log_parser)
   - create_db.py - Create the SQLite3 database (in local file)
   - parselogs - Parse the log files and add new download data into the database
   - countdownloads - Prints out the number of downloads of each file (based on the database)


USAGE:

1. Create the database

     python create_db.py

2. Parse the log files (this could be run as a cron job)

     parselogs --files logdir/*.log*

3. Get the counts

     countdownloads
