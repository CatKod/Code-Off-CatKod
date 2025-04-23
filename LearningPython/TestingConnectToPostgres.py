import psycopg2

def connect_to_postgres():
    try:
        conn = psycopg2.connect("dbname=test_connect user=postgres password=271205 host=localhost port=5432")
        return conn
    except Exception as e:
        print("Error connecting to the database:", e)
        return None

def insert_into_customers(name, email, age):
    conn = connect_to_postgres()
    if conn:
        try:
            cur = conn.cursor()

            cur.execute(
                "INSERT INTO customers (name, email, age) VALUES (%s, %s, %s)",
                (name, email, age)
            )

            conn.commit()
            print("Data inserted successfully.")
        except Exception as e:
            print("Error inserting data:", e)
        finally:
            cur.close()
            conn.close()

def insert_into_products(name_product, price, quantity):
    conn = connect_to_postgres()
    if conn:
        try:
            cur = conn.cursor()

            cur.execute(
                "INSERT INTO products (name_product, price, quantity) VALUES (%s, %s, %s)",
                (name_product, price, quantity)
            )

            conn.commit()
            print("Data inserted successfully.")
        except Exception as e:
            print("Error inserting data:", e)
        finally:
            cur.close()
            conn.close()

def delete_from_products(name_product):
    conn = connect_to_postgres()
    if conn:
        try:
            cur = conn.cursor()

            cur.execute(
                "DELETE FROM products WHERE name_product = %s",
                (name_product,)
            )

            conn.commit()
            print("Data deleted successfully.")
        except Exception as e:
            print("Error deleting data:", e)
        finally:
            cur.close()
            conn.close()

def increse_product_price(name_product):
    conn = connect_to_postgres()
    if conn:
        try:
            cur = conn.cursor()

            cur.execute(
                "UPDATE products SET price = 1.1 * price WHERE name_product = %s",
                (name_product,)
            )

            conn.commit()
            print("Price increased successfully.")
        except Exception as e:
            print("Error updating data:", e)
        finally:
            cur.close()
            conn.close()

def print_products_table():
    conn = connect_to_postgres()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM products LIMIT 10")
            rows = cur.fetchall()

            for row in rows:
                print(row)
        except Exception as e:
            print("Error fetching data:", e)
        finally:
            cur.close()
            conn.close()

def insert_into_catogry(id, name_catogory, price, special):
    conn = connect_to_postgres()
    if conn:
        try:
            cur = conn.cursor()

            cur.execute(
                "INSERT INTO catogry (id, name_catogory, price, special) VALUES (%s, %s, %s, %s)",
                (id, name_catogory, price, special)
            )

            conn.commit()
            print("Data inserted successfully.")
        except Exception as e:
            print("Error inserting data:", e)
        finally:
            cur.close()
            conn.close()

def print_catogry_table():
    conn = connect_to_postgres()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM catogry")
            rows = cur.fetchall()

            for row in rows:
                print(row)
        except Exception as e:
            print("Error fetching data:", e)
        finally:
            cur.close()
            conn.close()

if __name__ == "__main__":
    typeinput = int(input("Enter: "))
    if typeinput == 1:
        name = input("Enter name: ")
        email = input("Enter email: ")
        age = int(input("Enter age: "))
        insert_into_customers(name, email, age)
    elif typeinput == 2:
        for i in range(3):
            name_product = input("Enter name_product: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            insert_into_products(name_product, price, quantity)
    elif typeinput == 3:
        print_products_table()
    elif typeinput == 4:
        number = int(input("Enter number: "))
        for i in range(number):
            id = int(input("Enter id: "))
            name_catogory = input("Enter name_catogory: ")
            price = float(input("Enter price: "))
            special = input("Enter special: ")
            insert_into_catogry(id, name_catogory, price, special)

        print_catogry_table()
    elif typeinput == 5:
        name_product = input("Enter name_product: ")
        delete_from_products(name_product)
        print_products_table()
    elif typeinput == 6:
        name_product = input("Enter name_product: ")
        increse_product_price(name_product)
        print_products_table()