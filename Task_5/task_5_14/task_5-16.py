import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",  # База работает на твоём компьютере
        port="5432",  # Стандартный порт PostgreSQL
        user="postgres",  # Имя пользователя (из docker-compose.yml)
        password="example",  # Пароль (из docker-compose.yml)
        database="testdb"  # Имя базы данных
    )

    print(" Подключение к базе данных прошло успешно!")
    cursor = connection.cursor()

    cursor.execute('''
SELECT product_id, COUNT(*) AS supplier_count 
FROM suppliers 
GROUP BY product_id;
''')
    result = cursor.fetchone()
    print(f"\n Количество товаров в базе: {result[0]}")

    cursor.close()
    connection.close()
    print("\n Соединение закрыто.")

except Exception as error:
    print(f" Ошибка: {error}")