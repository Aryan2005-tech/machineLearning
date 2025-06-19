import sqlite3
con=sqlite3.connect("first.db")
cursor=con.cursor()
cursor.execute('''
create table if not exists student(
               id integer primary key,
               name text
               )
''')
con.commit()
cursor.execute('''
insert into student(id,name) values(21,"aryan")
              
''')
cursor.execute('''
insert into student(id,name) values(19,"aryan")
              
''')
con.commit()
cursor.execute('select * from student')
rows=cursor.fetchall()
for row in rows:
    print(row)




