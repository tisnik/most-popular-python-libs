import psycopg2

connection = psycopg2.connect(
    host="", port=5432, user="tester", password="123qwe", dbname="test"
)

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM v2")
    records = cursor.fetchall()
    for record in records:
        print(record, type(record[1]))
