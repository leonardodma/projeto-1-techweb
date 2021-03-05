  
from utils import load_data, load_template, build_response
import urllib
import json
from database import Database, Note


db = Database("notes")


def create_note(chave, valor):
    id = None
    title = chave 
    content = valor

    return Note(id, title, content)


def post_into_note(corpo):
    new_note = []
    for chave_valor in corpo.split('&'):
        unquote = urllib.parse.unquote_plus(chave_valor).split('=')
        print('Unquote: {}'.format(unquote))
        valor = unquote[1]
        new_note.append(valor)

    return create_note(new_note[0], new_note[1])


# Filling the table
for valores in load_data('notes.json'):
    db.add(create_note(valores['titulo'], valores['detalhes']))



def index(request):
    note_template = load_template('components/note.html')

    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]

        note = post_into_note(corpo)
        db.add(note)

        return build_response(code=303, reason='See Other', headers='Location: /')


    else:
        all_notes = db.get_all()
        # Cria uma lista de <li>'s para cada anotação
        # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
        notes_li = [
            note_template.format(title=dados.title, details=dados.content)
            for dados in all_notes
        ]
        notes = '\n'.join(notes_li)

        return build_response() + load_template('index.html').format(notes=notes).encode()