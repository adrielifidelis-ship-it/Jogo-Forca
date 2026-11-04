import random
from django.shortcuts import render, redirect

PALAVRAS = [
    'PYTHON', 'DJANGO', 'VERCEL', 'PROGRAMACAO', 'DEVELOPER', 'TECNOLOGIA',
    'ALGORITMO', 'BANCO', 'DADOS', 'SERVIDOR', 'CLIENTE', 'INTERFACE',
    'COMPUTADOR', 'SISTEMA', 'INTERNET', 'ROTEADOR', 'MEMORIA', 'PROCESSADOR',
    'HARDWARE', 'SOFTWARE', 'BIBLIOTECA', 'VARIAVEL', 'FUNCAO', 'CLASSE',
    'OBJETO', 'METODO', 'ATRIBUTO', 'ESTRUTURA', 'CODIGO', 'PROJETO',
    'APLICACAO', 'NAVEGADOR', 'DEBUGER', 'FRAMEWORK', 'BACKEND', 'FRONTEND',
    'FULLSTACK', 'AUTENTICACAO', 'SEGURANCA', 'CRIPTOGRAFIA', 'REDE', 'PACOTE',
    'MODULO', 'TERMINAL', 'COMANDO', 'VERSAO', 'REPOSITORIO', 'GIT',
    'GITHUB', 'DEPLOY', 'NUVEM', 'TESTE', 'ARQUIVO', 'PASTA',
    'DIRETORIO', 'EXECUTAVEL', 'COMPILADOR', 'INTERPRETE', 'SINTAXE', 'LOGICA',
    'OPERADOR', 'CONDICIONAL', 'LOOP', 'MATRIZ', 'LISTA', 'DICIONARIO',
    'TUPLA', 'CONJUNTO', 'STRING', 'INTEIRO', 'FLOAT', 'BOOLEANO',
    'REQUISICAO', 'RESPOSTA', 'CHAVE', 'VALOR', 'TABELA', 'COLUNA',
    'LINHA', 'CONSULTA', 'INDICE', 'CACHE', 'LOG', 'ERRO',
    'EXCECAO', 'EVENTO', 'FLUXO', 'DESIGN', 'LAYOUT', 'ESTILO',
    'CSS', 'HTML', 'JAVASCRIPT', 'JSON', 'API', 'REST', 'URL', 'TOKEN'
]

def jogo(request):
    if 'palavra' not in request.session:
        request.session['palavra'] = random.choice(PALAVRAS)
        request.session['letras_chutadas'] = []
        request.session['tentativas_restantes'] = 6

    palavra_secreta = request.session['palavra']
    letras_chutadas = request.session['letras_chutadas']

    if request.method == 'POST':
        letra = request.POST.get('letra', '').upper()
        if letra and letra not in letras_chutadas:
            letras_chutadas.append(letra)
            request.session['letras_chutadas'] = letras_chutadas
            if letra not in palavra_secreta:
                request.session['tentativas_restantes'] -= 1
        return redirect('jogo')

    palavra_oculta = [letra if letra in letras_chutadas else '_' for letra in palavra_secreta]
    ganhou = '_' not in palavra_oculta
    perdeu = request.session['tentativas_restantes'] <= 0

    context = {
        'palavra_oculta': ' '.join(palavra_oculta),
        'letras_chutadas': ', '.join(letras_chutadas),
        'tentativas': request.session['tentativas_restantes'],
        'ganhou': ganhou,
        'perdeu': perdeu,
        'palavra_correta': palavra_secreta,
    }
    return render(request, 'forca/jogo.html', context)

def reiniciar(request):
    request.session.flush()
    return redirect('jogo')