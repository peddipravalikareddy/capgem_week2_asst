#17
#Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`.
# Implement this in `SQLDatabase` and `NoSQLDatabase`.
from abc import ABC, abstractmethod
class IDatabaseOperations:
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self):
        pass
class SQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Inserting data in SQL database")
    def update(self):
        print("Updating data in SQL database")
    def delete(self):
        print("Deleting data in SQL database")
class NoSQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Inserting data in NoSQL database")
    def update(self):
        print("Updating data in NoSQL database")
    def delete(self):
        print("Deleting data in NoSQL database")
sql = SQLDatabase()
sql.insert()
sql.delete()
nosql = NoSQLDatabase()
nosql.insert()
nosql.delete()
