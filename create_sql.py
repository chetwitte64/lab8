import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_ticket_table()

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def create_ticket_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "tickets" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_company TEXT NOT NULL,
        user_email TEXT,
        error_info TEXT,
        IsComplete BOOLEAN DEFAULT 0,
        CreatedOn Date default CURRENT_DATE
        );
        """

        self.conn.execute(query)
        print("Table 'tickets' created successfully.")

Schema()