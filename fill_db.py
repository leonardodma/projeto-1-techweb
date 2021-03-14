from utils import load_data
from database import Database, Note

db = Database("notes")
# Filling the table
for valores in load_data('notes.json'):
    db.add(Note(None, valores['titulo'], valores['detalhes']))