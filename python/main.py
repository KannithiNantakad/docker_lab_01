import psycopg2

conn = psycopg2.connect(
    host="postgres",
    port=5432,
    database="de_db",
    user="deuser",
    password="depassword"
)

cursor = conn.cursor()

cursor.execute("""
    INSERT INTO customers (name, email, country)
    VALUES (%s, %s, %s)
""", (
    "Kannithi",
    "kannithi@example.com",
    "Thailand"
))

conn.commit()

cursor.close()
conn.close()

print("Data inserted successfully!")