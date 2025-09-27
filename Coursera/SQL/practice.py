import sqlite3

# conn = sqlite3.connect('emaildb.sqlite')
# cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Counts')

# cur.execute('''
# CREATE TABLE Counts (email TEXT, count INTEGER)''')


# fname = input('Enter file name: ')
# if (len(fname) < 1): fname = 'mbox.txt'
# fh = open(fname)
# for line in fh:
#     if not line.startswith('From: '): continue
#     pieces = line.split()
#     email = pieces[1]
#     cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('''INSERT INTO Counts (email, count)
#                 VALUES (?, 1)''', (email,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
#                     (email,))
#     conn.commit()

# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])

# cur.close()



import sqlite3

# Connect to database (or create if it doesn't exist)
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Clear out old data
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Prompt for file name
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'

fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    domain = email.split('@')[1]  # Extract domain
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))

# Commit changes once at the end (for speed)
conn.commit()

# Print top 10 orgs (optional)
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(row[0], row[1])

cur.close()
