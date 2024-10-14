import psycopg2
import psycopg2.extras

# Connect to your postgres DB
hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = ''
port_id = 0000
conn = None
cur = None

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id)
    print("Connection to the database was successful")

    # Create a cursor object using the cursor() method
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute("DROP TABLE IF EXISTS employee")

    create_script = ''' CREATE TABLE IF NOT EXISTS employee (
        id int PRIMARY KEY NOT NULL,
        name varchar(40) NOT NULL,
        salary int,
        dept_id varchar(30))
    '''

    cur.execute(create_script)

    insert_script = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
    insert_values = (1, 'James', 12000, 'D1'), (2, 'Robin', 15000, 'D1'), (3, 'Xavier', 20000, 'D2')
    for record in insert_values:
        cur.execute(insert_script, record)

    update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
    cur.execute(update_script)

    delete_script = 'DELETE FROM employee WHERE name = %s'
    delete_record = ('James',)
    cur.execute(delete_script, delete_record)

    cur.execute('SELECT * FROM employee')
    for record in cur.fetchall():
        print(record['name'], record['salary'])

    conn.commit()
    print("Table created successfully in PostgreSQL ")



except Exception as error:
    print("Error: ", error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
