from models import ToDoModel

class ToDoService:
    def __init__(self):
        self.model = ToDoModel()

    def create(self, params):
        return self.model.create(params)

    def update(self, item_id):
        return self.model.update(item_id)

    def delete(self, item_id):
        return self.model.delete(item_id)

    def select_ticket(self, id):
        response = self.model.get_by_id(id)
        return response

    def select_list(self, limit):
        response = self.model.list_select_items(limit)
        return response

    def list(self):
        response = self.model.list_items()
        return response
    
    def get_by_id(self, item_id):
        response = self.model.get_by_id(item_id)
        return response

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