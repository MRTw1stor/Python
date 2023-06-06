import sqlite3
from sqlite3 import Error
#  Подключение к базе данных
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

#  Создание таблиц
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred") 
connection = create_connection("SQLite.db")

# create_users_table = """
# CREATE TABLE IF NOT EXISTS users (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT NOT NULL,
#   age INTEGER,
#   city TEXT
# );
# """
# execute_query(connection ,create_users_table)
# create_posts_table = """
# CREATE TABLE IF NOT EXISTS posts(
#   id INTEGER PRIMARY KEY AUTOINCREMENT, 
#   title TEXT NOT NULL, 
#   description TEXT NOT NULL, 
#   user_id INTEGER NOT NULL, 
#   FOREIGN KEY (user_id) REFERENCES users (id)
# );
# """
# execute_query(connection ,create_posts_table)

# create_comments_table = """
# CREATE TABLE IF NOT EXISTS comments (
#   id INTEGER PRIMARY KEY AUTOINCREMENT, 
#   text TEXT NOT NULL, 
#   user_id INTEGER NOT NULL, 
#   post_id INTEGER NOT NULL, 
#   FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
# );
# """
# execute_query(connection, create_comments_table)  
# create_likes_table = """
# CREATE TABLE IF NOT EXISTS likes (
#   id INTEGER PRIMARY KEY AUTOINCREMENT, 
#   user_id INTEGER NOT NULL, 
#   post_id integer NOT NULL, 
#   FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
# );
# """
# execute_query(connection, create_likes_table) 

# create_users = """
# INSERT INTO
#   users (name, age, city)
# VALUES
#   ('James', 25, 'USA'),
#   ('Leila', 32, 'France'),
#   ('Brigitte', 35, 'England'),
#   ('Mike', 40, 'Denmark'),
#   ('Elizabeth', 21, 'Canada');
# """
# execute_query(connection, create_users)   

# create_posts = """
# INSERT INTO
#   posts (title, description, user_id)
# VALUES
#   ("Happy", "I am feeling very happy today", 1),
#   ("Hot Weather", "The weather is very hot today", 2),
#   ("Help", "I need some help with my work", 2),
#   ("Great News", "I am getting married", 1),
#   ("Interesting Game", "It was a fantastic game of tennis", 5),
#   ("Party", "Anyone up for a late-night party today?", 3);
# """

# execute_query(connection, create_posts)  

# create_comments = """
# INSERT INTO
#   comments (text, user_id, post_id)
# VALUES
#   ('Count me in', 1, 6),
#   ('What sort of help?', 5, 3),
#   ('Congrats buddy', 2, 4),
#   ('I was rooting for Nadal though', 4, 5),
#   ('Help with your thesis?', 2, 3),
#   ('Many congratulations', 5, 4);
# """
# execute_query(connection, create_comments)

# create_likes = """
# INSERT INTO
#   likes (user_id, post_id)
# VALUES
#   (1, 6),
#   (2, 3),
#   (1, 5),
#   (5, 4),
#   (2, 4),
#   (4, 2),
#   (3, 6);
# """
# execute_query(connection, create_likes)  

# Функция для извлечения данных 
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        
select_users = "SELECT * from users"
users = execute_read_query(connection, select_users)

for user in users:
    print(user)

print("")
#  Просмотр колонок
cursor = connection.cursor()
cursor.execute(select_users)
cursor.fetchall()

column_names = [description[0] for description in cursor.description]
print(column_names)

