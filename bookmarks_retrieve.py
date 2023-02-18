import os
import json
import sqlite3
import dropbox
from dropbox.exceptions import AuthError

# Set the path to the output bookmark file
bookmark_file_path = '/path/to/output/bookmarks.json'

# Set Dropbox access token
dbx = dropbox.Dropbox('YOUR_DROPBOX_ACCESS_TOKEN')

# List of browsers to extract bookmarks from
browsers = ['Google Chrome', 'Mozilla Firefox', 'Microsoft Edge']

# Function to read bookmarks from Chrome
def read_chrome_bookmarks():
    bookmarks = {}
    try:
        # Get the path to the Chrome bookmarks database
        chrome_path = os.path.expanduser('~') + '/AppData/Local/Google/Chrome/User Data/Default/Bookmarks'
        conn = sqlite3.connect(chrome_path)
        c = conn.cursor()
        c.execute('SELECT name, url FROM bookmarks')
        rows = c.fetchall()
        for row in rows:
            bookmarks[row[0]] = row[1]
        conn.close()
    except Exception as e:
        print(f'Error reading Chrome bookmarks: {e}')
    return bookmarks

# Function to read bookmarks from Firefox
def read_firefox_bookmarks():
    bookmarks = {}
    try:
        # Get the path to the Firefox bookmarks database
        firefox_path = os.path.expanduser('~') + '/AppData/Roaming/Mozilla/Firefox/Profiles/'
        profiles = [f.path for f in os.scandir(firefox_path) if f.is_dir()]
        for profile in profiles:
            bookmarks_path = os.path.join(profile, 'places.sqlite')
            conn = sqlite3.connect(bookmarks_path)
            c = conn.cursor()
            c.execute('SELECT moz_bookmarks.title, moz_places.url FROM moz_bookmarks JOIN moz_places ON moz_bookmarks.fk = moz_places.id')
            rows = c.fetchall()
            for row in rows:
                bookmarks[row[0]] = row[1]
            conn.close()
    except Exception as e:
        print(f'Error reading Firefox bookmarks: {e}')
    return bookmarks

# Function to read bookmarks from Edge
def read_edge_bookmarks():
    bookmarks = {}
    try:
        # Get the path to the Edge bookmarks database
        edge_path = os.path.expanduser('~') + '/AppData/Local/Microsoft/Edge/User Data/Default/DataStore/IndexedDB/https___www.microsoftedgeinsider.com_0.indexeddb.leveldb/'
        conn = sqlite3.connect(os.path.join(edge_path, '000003.ldb'))
        c = conn.cursor()
        c.execute('SELECT key, value FROM object_data')
        rows = c.fetchall()
        for row in rows:
            try:
                bookmark = json.loads(row[1])
                if bookmark['name'] and bookmark['url']:
                    bookmarks[bookmark['name']] = bookmark['url']
            except:
                pass
        conn.close()
    except Exception as e:
        print(f'Error reading Edge bookmarks: {e}')
    return bookmarks

# Function to write bookmarks to a JSON file
def write_bookmarks(bookmarks):
    with open(bookmark_file_path, 'w') as f:
        json.dump(bookmarks, f)

# Function to merge bookmarks from multiple browsers
def merge_bookmarks():
    bookmarks = {}
    for browser in browsers:
        if browser == 'Google Chrome':
            bookmarks.update(read_chrome_bookmarks())
        elif browser == 'Mozilla Firefox':
            bookmarks.update(read_firefox_bookmarks())
        elif browser == 'Microsoft Edge':
            bookmarks.update(read_edge_bookmarks())
    return bookmarks

# Merge bookmarks from all browsers
all_bookmarks = merge_bookmarks