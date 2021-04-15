import os
import json 


"""
Implemente a função extract_route, que recebe uma string com a requisição e devolve a rota, 
excluindo o primeiro caractere (/). Por exemplo, para a requisição "Stranger Things" acima, 
sua função deve devolver 'img/strangerthings/stranger-things.jpg'.
"""
def extract_route(request):
    # print("request: {}".format(request))
    return request.split()[1][1:]


"""
Implemente a função read_file, que recebe um argumento do tipo Path e devolve o conteúdo desse
arquivo. Se a extensão do arquivo for alguma entre .txt, .html, .css, .js, sua função deve ler
o arquivo como text e devolver uma string. Leia qualquer outro tipo de arquivo como binário e
devolve os bytes. Se precisar refrescar a memória, leia a documentação da função open.
"""
def read_file(path):
    filename, file_extension = os.path.splitext(path)

    abrir_texto = ['.txt', '.html', '.css', '.js']
    
    if file_extension in abrir_texto:
        with open(path, 'rt', encoding='utf-8') as arquivo:
            return arquivo.read().encode(encoding='utf-8')
    else:
        with open(path, 'rb') as arquivo:
            return arquivo.read()

"""
Implemente a função load_data, que recebe o caminho de um arquivo JSON e devolve o conteúdo do 
arquivo com esse nome dentro da pasta data carregado como um objeto Python. Por exemplo: se o 
conteúdo do arquivo data/dados.json for a string {"chave": "valor"}, sua função deve devolver o 
dicionário Python {"chave": "valor"} para a entrada dados.json (note que o nome da pasta não é 
enviado como argumento). Dica: já existe uma função Python para isso (e você viu em Design de Software).

"""
def load_data(json_file):
    with open('data/' + json_file, encoding='utf-8') as json_path: 
        data = json.load(json_path) 

    return data


"""
Implemente a função load_template que recebe o nome de um arquivo de template e devolve uma string 
com o conteúdo desse arquivo. O nome do arquivo não inclui o nome da pasta templates. Por exemplo: 
para a entrada index.html você deve carregar o conteúdo do arquivo templates/index.html.
"""
def load_template(template_file):
    path = 'templates/' + template_file
    return read_file(path).decode(encoding='utf-8')


"""
Implemente a função build_response no arquivo utils.py. Ele deve receber os seguintes argumentos: 
build_response(body='', code=200, reason='OK', headers='') (talvez você queira ler isso: 
https://docs.python.org/3/tutorial/controlflow.html#default-argument-values).
"""

def build_response(body='', code=200, reason='OK', headers=''):
    response = 'HTTP/1.1 ' + str(code) + ' ' + reason
    
    if len(headers) == 0:
        response += '\n\n' + body
    else:
        response += '\n' + headers + '\n\n' + body

    return response.encode(encoding='utf-8')