import psycopg2
'''Sanjar Shakhiddinov'''
'''1-masala'''
# host = 'localhost'
# user = 'postgres'
# password = '123'
# database = 'n42'
# port = 5432
# conn = psycopg2.connect(host=host,
#                         database=database,
#                         user=user,
#                         password=password,
#                         port=port
#                         )
# cur = conn.cursor()

# def create_product_table():
#     cur.execute('''CREATE TABLE IF NOT EXISTS Product 
#                    (id SERIAL PRIMARY KEY,
#                     name TEXT NOT NULL,
#                     price NUMERIC NOT NULL,
#                     color TEXT NOT NULL,
#                     image TEXT NOT NULL);''')
#     conn.commit()

# def insert_product(name, price, color, image):
#     cur.execute("INSERT INTO Product (name, price, color, image) VALUES (%s, %s, %s, %s)",
#                 (name, price, color, image))
#     conn.commit()
'''2-masala'''
# def select_all_products():
#     cur.execute("SELECT * FROM Product")
#     rows = cur.fetchall()
#     return rows

# def update_product(product_id, name, price, color, image):
#     cur.execute("UPDATE Product SET name = %s, price = %s, color = %s, image = %s WHERE id = %s",
#                 (name, price, color, image, product_id))
#     conn.commit()

# def delete_product(product_id):
#     cur.execute("DELETE FROM Product WHERE id = %s", (product_id,))
#     conn.commit()

# create_product_table()
# insert_product("product_1", 10.60, "red", "http:/urlimage")
# insert_product("product_2", 19.4, "black", "http:/urlimage")
# products = select_all_products()
# print(products)
# update_product(1, "product 1", 15.9, "blue", "http:/urlimage")
# delete_product(2)

# cur.close()
# conn.close()
'''3-masala'''

# class Alphabet:
#     def __init__(self):
#         self.letters = [chr(ord('A') + i) for i in range(26)] 

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index >= len(self.letters): 
#             raise StopIteration
#         letter = self.letters[self.index]  
#         self.index += 1 
#         return letter

# alphabet = Alphabet()
# for letter in alphabet:
#     print(letter)

'''6-masala'''

# class DbConnect:
#     def __init__(self, database, user, password, host, port):
#         host = 'localhost'
#         user = 'postgres'
#         password = '123'
#         database = 'n42'
#         port = 5432
#         conn = psycopg2.connect(host=host,
#                         database=database,
#                         user=user,
#                         password=password,
#                         port=port
#                         )
#         cur = conn.cursor()

#     def __enter__(self):
#         self.conn = psycopg2.connect(database=self.database, user=self.user, password=self.password, host=self.host, port=self.port)
#         self.cur = self.conn.cursor()
#         return self.conn, self.cur

#     def __exit__(self, exc_type, exc_value, traceback):
#         if self.cur:
#             self.cur.close()
#         if self.conn:
#             self.conn.close()

# with DbConnect(database="n42", user="postgres", password=123, host="localhost", port=5432) as (conn, cur):
#     cur.execute("SELECT * FROM table")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)