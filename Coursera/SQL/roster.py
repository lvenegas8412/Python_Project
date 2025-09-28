import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER PRIMARY KEY,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER PRIMARY KEY,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0]
    title = entry[1]
    role = entry[2]

    # print((name, title))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, entry[2] ) )
    


query = '''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;
'''

# # SELECT User.name, Course.title, Member.role 
# FROM User 
# JOIN Member ON User.id = Member.user_id 
# JOIN Course ON Member.course_id = Course.id
# ORDER BY User.name DESC, Course.title DESC, Member.role DESC 
# LIMIT 2;
print("\nTop 2 results:")
for row in cur.execute(query):
    print(row)
conn.commit
conn.close()


# import json
# import sqlite3

# conn = sqlite3.connect('rosterdb.sqlite')
# cur = conn.cursor()

# # Do some setup
# cur.executescript('''
# DROP TABLE IF EXISTS User;
# DROP TABLE IF EXISTS Member;
# DROP TABLE IF EXISTS Course;

# CREATE TABLE User (
#     id     INTEGER PRIMARY KEY,
#     name   TEXT UNIQUE
# );

# CREATE TABLE Course (
#     id     INTEGER PRIMARY KEY,
#     title  TEXT UNIQUE
# );

# CREATE TABLE Member (
#     user_id     INTEGER,
#     course_id   INTEGER,
#     role        INTEGER,
#     PRIMARY KEY (user_id, course_id)
# )
# ''')

# fname = input('Enter file name: ')
# if len(fname) < 1:
#     fname = 'roster_data.json'

# # Load JSON data
# with open(fname) as f:
#     json_data = json.load(f)

# # Insert data into tables
# for entry in json_data:
#     name = entry[0]
#     title = entry[1]
#     role = entry[2]

#     cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
#     cur.execute('SELECT id FROM User WHERE name = ?', (name,))
#     user_id = cur.fetchone()[0]

#     cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
#     cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
#     course_id = cur.fetchone()[0]

#     cur.execute('''
#         INSERT OR REPLACE INTO Member (user_id, course_id, role)
#         VALUES (?, ?, ?)
#     ''', (user_id, course_id, role))

# # Run the final query
# query = '''
# SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
#     User JOIN Member JOIN Course 
#     ON User.id = Member.user_id AND Member.course_id = Course.id
#     ORDER BY X LIMIT 1;
# '''

# print("\nTop 2 results:")
# for row in cur.execute(query):
#     print(row)

# conn.commit()
# conn.close()
