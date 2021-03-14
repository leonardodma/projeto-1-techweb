from os import name
import sqlite3
from dataclasses import dataclass


class Database:
    def __init__(self, db_name):
        self.name = db_name + '.db'
        self.conn = sqlite3.connect(self.name)

        self.note =  """CREATE TABLE IF NOT EXISTS 
                   note (
                        id INTEGER PRIMARY KEY, 
                        title STRING, 
                        content STRING NOT NULL
                    );
                """ 

        self.conn.execute(self.note)

    def add(self, note):
        self.content = """INSERT INTO note (title, content) VALUES ('{}', '{}');""".format(note.title, note.content)  
        self.conn.execute(self.content)
        self.conn.commit()

    def update(self, entry):
        id = entry.id
        title = entry.title
        content = entry.content

        self.update = """
                        UPDATE note 
                        SET title = '{}', content = '{}' 
                        WHERE id = {}""".format(title, content, id)

        
        self.conn.execute(self.update)
        self.conn.commit()
    
    def delete(self, note_id):
        self.content = """
                        DELETE FROM note 
                        WHERE id = {}""".format(note_id)

        self.conn.execute(self.content)
        self.conn.commit()     

    def get_all(self):
        self.cursor = self.conn.execute("SELECT id, title, content FROM note")
        self.note_list = []
        
        for linha in self.cursor:
            note_obj = Note(linha[0], linha[1], linha[2])
            self.note_list.append(note_obj)
        
        return self.note_list

    

class Note:
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content 