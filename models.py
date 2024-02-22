import sqlite3

class ToDoModel:
    TABLENAME = "tickets"

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def get_by_id(self, id):
        query = f"select * from {self.TABLENAME} where id = {id}"
        result = self.conn.execute(query).fetchall()
        return [{column: row[i] for i, column in enumerate(result[0].keys())}
                for row in result]

    def create(self, params):
        print (params)
        query = f'insert into {self.TABLENAME} ' \
                f'(user_company, user_email, error_info) ' \
                f'values ("{params.get("user_company")}","{params.get("user_email")}",' \
                f'"{params.get("error_info")}")'
        
        self.conn.execute(query)

    def delete(self, item_id):
        query = f"DELETE FROM {self.TABLENAME} WHERE id = {item_id}"
        print (query)
        self.conn.execute(query)
        return self.list_items()

    def update(self, item_id,):

        query = f"UPDATE {self.TABLENAME} " \
                f"SET IsComplete = TRUE " \
                f"WHERE id = {item_id}"
    
        self.conn.execute(query)
        return self.get_by_id(item_id)

    def list_select_items(self, limit):
        query = f"SELECT * FROM {self.TABLENAME} LIMIT {limit}"
        result_set = self.conn.execute(query).fetchall()
        result = [{column: row[i]
                   for i, column in enumerate(result_set[0].keys())}
                  for row in result_set]
        return result
        
    def list_items(self):
        query = f"SELECT *" \
                f"from {self.TABLENAME}" 
        print (query)
        result_set = self.conn.execute(query).fetchall()
        print (result_set)
        result = [{column: row[i]
                  for i, column in enumerate(result_set[0].keys())}
                  for row in result_set]
        return result


