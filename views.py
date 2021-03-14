  
from utils import load_data, load_template, build_response
import urllib
import json
from database import Database, Note


db = Database("notes")


def post_into_note(corpo):  
    new_note = []
    for chave_valor in corpo.split('&'):
        unquote = urllib.parse.unquote_plus(chave_valor).split('=')
        print('Unquote: {}'.format(unquote))

        if unquote[0] == 'deleteNote':
            db.delete(unquote[1])
            return None
        
        else:
            valor = unquote[1]
            print('Valor: {}'.format(valor))
            new_note.append(valor)

            print("New note: {}".format(new_note))

    return Note(new_note[0], new_note[1], new_note[2])


def index(request):
    note_template = load_template('components/note.html')

    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]

        print("Corpo = {}".format(corpo))
        note = post_into_note(corpo)

        if note is None:
            print("Entroooooooooooooooooooooooooooooou")
            return build_response(code=303, reason='See Other', headers='Location: /')

        else:
            if note.id == 'None':
                db.add(note)
            else:
                db.update(note) # Importante para editar e ecluir uma nota

        return build_response(code=303, reason='See Other', headers='Location: /')


    else:
        all_notes = db.get_all()
        # Cria uma lista de <li>'s para cada anotação
        # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
        notes_li = [
            note_template.format(id=dados.id, title=dados.title, details=dados.content)
            for dados in all_notes
        ]
        notes = '\n'.join(notes_li)

        return build_response() + load_template('index.html').format(notes=notes).encode(encoding='utf-8')