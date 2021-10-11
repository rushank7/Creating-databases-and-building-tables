#!/usr/bin/env python
# coding: utf-8

# In[36]:


pip install psycopg2


# In[37]:


import psycopg2


# In[38]:


try : 
     conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=champ123")
except psycopg2.Error as e:
    print("Error: could not make connection to postgress database")
    print(e)
#Creating a connection to databases    


# In[40]:


# use connection to get a cursor that can be used to execute queries
try: 
    cur = conn.cursor()
except psycopg2.Error as e: 
    print("Error: Could not get curser to the Database")
    print(e)


# In[41]:


#set automatic commit
conn.set_session(autocommit=True)


# In[42]:


#Creating database
try :
     cur.execute("CREATE DATABASE LOLDATABASE")
except psycopg2.Error as e:
    print(e)


# In[43]:


#closing connection to deafaultdatabse and create whole connection to loldatabase created above  
try :
    conn = psycopg2.connect("host=127.0.0.1 dbname=LOLDATABASE user=postgress password=champ123")
except psycopg2.Error as e:
    print("Error: Could not make connection")
    print(e)
    
try: 
    cur = conn.cursor()
except psycopg2.Error as e: 
    print("Error: Could not get curser to the Database")
    print(e)
    
conn.set_session(autocommit=True)


# In[46]:


#create tables
try:
    cur.execute("create table if not exists students (student_id int, name varchar,    age int, gender varchar, subject varchar, marks int);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)


# In[47]:


#Insert 2 rows in table
try: 
    cur.execute("INSERT INTO students (student_id, name, age, gender, subject, marks)                  VALUES (%s, %s, %s, %s, %s, %s)",                  (1, "Raj", 23, "Male", "Python", 85))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO students (student_id, name, age, gender, subject, marks)                   VALUES (%s, %s, %s, %s, %s, %s)",
                  ( 2, "Priya", 22, "Female", "Python", 86))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)


# In[48]:


#validating selected data
try: 
    cur.execute("SELECT * FROM students;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()


# In[49]:


#closung connection
cur.close()
conn.close()

