"""
Create the downloads database file

By: Jonathan M. Cameron

Copyright (c) 2015 Jonathan M. Cameron
License: http://www.gnu.org/licenses/gpl-2.0.html GNU/GPL
"""

import sqlite3
 
conn = sqlite3.connect("downloads.db")
 
cursor = conn.cursor()
 
# create a table
cursor.execute("""CREATE TABLE downloads
                  (key TEXT, 
                   filename TEXT, 
                   host TEXT, 
                   time TEXT, 
                   size INTEGER,
                   UNIQUE(key))
               """)

# NOTE: the UNIQUE(key) is used to prevent duplicate insertions

conn.close()
