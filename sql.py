import sqlite3


def create_tables(conn):

    conn.executescript("""
        CREATE TABLE EMPLOYEE(                                                    
        ID INTEGER PRIMARY KEY,                                                    
        NAME STRING NOT NULL,                                                      
        SALARY INTEGER NOT NULL,                                               
        DEPT_ID INTEGER NOT NULL);

        CREATE TABLE DEPARTMENT(                                                    
        ID INTEGER PRIMARY KEY,                                                    
        NAME STRING NOT NULL,                                                      
        LOCATION STRING NOT NULL);

      """)

def init_tables(cursor):
    employees = [(1, 'Candice', 4685, 1),
                 (2, 'Julia', 2559, 2),
                 (3, 'Bob', 4405, 4),
                 (4, 'Scarlet', 2350, 1),
                 (5, 'Ileana', 1151, 4)]
    departments = [(1, 'Executive', 'Sydney'),
                   (2, 'Production', 'Sydney'),
                   (3, 'Resources', 'Cape Town'),
                   (4, 'Technical', 'Texas'),
                   (5, 'Management', 'Paris')]

    # Insert the data into the table
    for employee in employees:
        cursor.execute("INSERT INTO EMPLOYEE VALUES (?, ?, ?, ?)", employee)
    for department in departments:
        cursor.execute("INSERT INTO DEPARTMENT VALUES (?, ?, ?)", department)




if __name__ == '__main__':
    # Connect to the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    create_tables(conn)
    init_tables(cursor)

    cursor.execute(
        "SELECT DEPARTMENT.NAME, COUNT(EMPLOYEE.ID) as employee_count "
        "FROM DEPARTMENT LEFT JOIN EMPLOYEE ON DEPARTMENT.ID = EMPLOYEE.DEPT_ID "
        "GROUP BY DEPARTMENT.ID ORDER BY employee_count DESC")

    # get data
    rows = cursor.fetchall()

    # Iterate rows and print data
    for row in rows:
        print(row)
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

