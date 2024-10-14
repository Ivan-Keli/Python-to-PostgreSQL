import psycopg2
import psycopg2.extras

# Database connection parameters
hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = ''
port_id = 0000
conn = None

try:
    # Establish a connection to the PostgreSQL database using a context manager
    with psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id) as conn:

        print("Connection to the database was successful")

    # Create a cursor object using the cursor() method with DictCursor factory
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

        # Drop the employee table if it exists
        cur.execute("DROP TABLE IF EXISTS employee")

        # SQL script to create the employee table
        create_script = ''' CREATE TABLE IF NOT EXISTS employee (
            id int PRIMARY KEY NOT NULL,
            name varchar(40) NOT NULL,
            salary int,
            dept_id varchar(30))
        '''

        # Execute the create table script
        cur.execute(create_script)

        # SQL script to insert data into the employee table
        insert_script = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
        insert_values = (1, 'James', 12000, 'D1'), (2, 'Robin', 15000, 'D1'), (3, 'Xavier', 20000, 'D2')
        
        # Insert each record into the employee table
        for record in insert_values:
            cur.execute(insert_script, record)

        # SQL script to update the salary of all employees
        update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
        cur.execute(update_script)

        # SQL script to delete an employee by name
        delete_script = 'DELETE FROM employee WHERE name = %s'
        delete_record = ('James',)
        cur.execute(delete_script, delete_record)

        # Select all records from the employee table
        cur.execute('SELECT * FROM employee')
        
        # Fetch and print each record
        for record in cur.fetchall():
            print(record['name'], record['salary'])

        print("Table created successfully in PostgreSQL")

except Exception as error:
    # Print any error that occurs during the database operations
    print("Error: ", error)
finally:
    # Ensure the connection is closed
    if conn is not None:
        conn.close()
