import psycopg2

# Database connection parameters
hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = ''
port_id = 0000
conn = None
cur = None

try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)
    print("Connection to the database was successful")

    # Create a cursor object using the cursor() method
    cur = conn.cursor()

    # SQL script to create a table if it does not already exist
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
    insert_value = (1, 'James', 12000, 'D1'), (2, 'Robin', 15000, 'D1'), (3, 'Xavier', 20000, 'D1')
    
    # Execute the insert script with the provided values
    cur.executemany(insert_script, insert_value)

    # Commit the transaction
    conn.commit()
    print("Table created successfully in PostgreSQL")

except Exception as error:
    # Print any error that occurs during the process
    print("Error: ", error)
finally:
    # Close the cursor and connection to clean up
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
