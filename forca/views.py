import random
from django.shortcuts import render, redirect

# Dicionário com Palavras e Dicas
PALAVRAS_COM_DICAS = [
    {'palavra': 'PYTHON', 'dica': 'Linguagem de programação famosa pela sintaxe simples e pelo símbolo de cobra.'},
    {'palavra': 'DJANGO', 'dica': 'Framework web em Python muito usado para criar sites com batteries included.'},
    {'palavra': 'VERCEL', 'dica': 'Plataforma de hospedagem na nuvem focada em projetos web modernos e serverless.'},
    {'palavra': 'PROGRAMACAO', 'dica': 'A arte de escrever instruções para que computadores realizem tarefas.'},
    {'palavra': 'DEVELOPER', 'dica': 'Profissional que constrói software, aplicações e sistemas.'},
    {'palavra': 'TECNOLOGIA', 'dica': 'Conjunto de conhecimentos e ferramentas aplicadas à resolução de problemas.'},
    {'palavra': 'ALGORITMO', 'dica': 'Sequência passo a passo de instruções bem definidas para resolver um problema.'},
    {'palavra': 'BANCO', 'dica': 'Local estruturado onde dados são armazenados e organizados.'},
    {'palavra': 'DADOS', 'dica': 'Informações brutas processadas por computadores.'},
    {'palavra': 'SERVIDOR', 'dica': 'Computador potente encarregado de fornecer recursos ou dados a outros computadores.'},
    {'palavra': 'CLIENTE', 'dica': 'Dispositivo ou aplicação que consome dados de um servidor.'},
    {'palavra': 'INTERFACE', 'dica': 'Ponto de interação visual ou lógica entre o usuário e o sistema.'},
    {'palavra': 'COMPUTADOR', 'dica': 'Máquina eletrônica que processa dados segundo instruções.'},
    {'palavra': 'SISTEMA', 'dica': 'Conjunto de componentes integrados que funcionam juntos.'},
    {'palavra': 'INTERNET', 'dica': 'Rede global de computadores interconectados.'},
    {'palavra': 'ROTEADOR', 'dica': 'Dispositivo que encaminha pacotes de dados entre redes.'},
    {'palavra': 'MEMORIA', 'dica': 'Componente que armazena dados temporários ou permanentes.'},
    {'palavra': 'PROCESSADOR', 'dica': 'O cérebro do computador, responsável pelas operações lógicas e matemáticas.'},
    {'palavra': 'HARDWARE', 'dica': 'Parte física do computador (placa, memória, tela).'},
    {'palavra': 'SOFTWARE', 'dica': 'Conjunto de programas e instruções que rodam no computador.'},
    {'palavra': 'BIBLIOTECA', 'dica': 'Conjunto de rotinas e códigos pré-prontos reutilizáveis.'},
    {'palavra': 'VARIAVEL', 'dica': 'Espaço na memória que guarda um valor que pode mudar.'},
    {'palavra': 'FUNCAO', 'dica': 'Bloco de código reutilizável que realiza uma tarefa específica.'},
    {'palavra': 'CLASSE', 'dica': 'Modelo ou molde usado para criar objetos na programação.'},
    {'palavra': 'OBJETO', 'dica': 'Instância de uma classe na programação orientada a objetos.'},
    {'palavra': 'METODO', 'dica': 'Função associada a um objeto ou classe.'},
    {'palavra': 'ATRIBUTO', 'dica': 'Característica ou propriedade de um objeto.'},
    {'palavra': 'ESTRUTURA', 'dica': 'Forma como os dados são organizados na memória.'},
    {'palavra': 'CODIGO', 'dica': 'Texto escrito numa linguagem de programação.'},
    {'palavra': 'PROJETO', 'dica': 'Esforço temporário para criar um produto ou serviço único.'},
    {'palavra': 'APLICACAO', 'dica': 'Programa de computador feito para uso final do usuário.'},
    {'palavra': 'NAVEGADOR', 'dica': 'Programa usado para acessar a web (ex: Chrome, Firefox).'},
    {'palavra': 'DEBUGER', 'dica': 'Ferramenta usada para procurar e corrigir erros no código.'},
    {'palavra': 'FRAMEWORK', 'dica': 'Estrutura base pronta que facilita o desenvolvimento de aplicações.'},
    {'palavra': 'BACKEND', 'dica': 'Parte do sistema que roda no servidor, invisível ao usuário final.'},
    {'palavra': 'FRONTEND', 'dica': 'Parte visual do sistema com a qual o usuário interage diretamente.'},
    {'palavra': 'FULLSTACK', 'dica': 'Desenvolvedor que trabalha tanto no frontend quanto no backend.'},
    {'palavra': 'AUTENTICACAO', 'dica': 'Processo de verificação de identidade (ex: login e senha).'},
    {'palavra': 'SEGURANCA', 'dica': 'Prática de proteger sistemas e dados contra acessos não autorizados.'},
    {'palavra': 'CRIPTOGRAFIA', 'dica': 'Técnica de codificar dados para que apenas o destinatário os leia.'},
    {'palavra': 'REDE', 'dica': 'Conjunto de dispositivos conectados para compartilhar recursos.'},
    {'palavra': 'PACOTE', 'dica': 'Unidade de dados enviada por uma rede de computadores.'},
    {'palavra': 'MODULO', 'dica': 'Arquivo contendo código Python que pode ser importado por outros.'},
    {'palavra': 'TERMINAL', 'dica': 'Interface baseada em texto para enviar comandos ao sistema.'},
    {'palavra': 'COMANDO', 'dica': 'Instrução direta dada ao computador via terminal.'},
    {'palavra': 'VERSAO', 'dica': 'Estado específico de um software em evolução.'},
    {'palavra': 'REPOSITORIO', 'dica': 'Local onde o código do projeto e o histórico de alterações são mantidos.'},
    {'palavra': 'GIT', 'dica': 'Sistema de controle de versão distribuído muito popular.'},
    {'palavra': 'GITHUB', 'dica': 'Plataforma online para hospedar repositórios Git.'},
    {'palavra': 'DEPLOY', 'dica': 'Ato de colocar uma aplicação pronta no ar para ser acessada.'},
    {'palavra': 'NUVEM', 'dica': 'Serviços de computação oferecidos pela internet.'},
    {'palavra': 'TESTE', 'dica': 'Processo de verificação para garantir que o código funciona como esperado.'},
    {'palavra': 'ARQUIVO', 'dica': 'Recurso para guardar dados em um dispositivo de armazenamento.'},
    {'palavra': 'PASTA', 'dica': 'Diretório usado para organizar arquivos.'},
    {'palavra': 'DIRETORIO', 'dica': 'Outro nome para uma pasta no sistema de arquivos.'},
    {'palavra': 'EXECUTAVEL', 'dica': 'Arquivo contendo um programa pronto para ser rodado.'},
    {'palavra': 'COMPILADOR', 'dica': 'Traduz código de programação para linguagem de máquina inteira de uma vez.'},
    {'palavra': 'INTERPRETE', 'dica': 'Executa código de programação linha por linha (ex: Python).'},
    {'palavra': 'SINTAXE', 'dica': 'Regras gramaticais de uma linguagem de programação.'},
    {'palavra': 'LOGICA', 'dica': 'Raciocínio sequencial usado para construir programas.'},
    {'palavra': 'OPERADOR', 'dica': 'Símbolo usado para operações (+, -, ==, etc).'},
    {'palavra': 'CONDICIONAL', 'dica': 'Estrutura que toma decisões no código (if/else).'},
    {'palavra': 'LOOP', 'dica': 'Estrutura de repetição no código (for/while).'},
    {'palavra': 'MATRIZ', 'dica': 'Estrutura de dados bidimensional (linhas e colunas).'},
    {'palavra': 'LISTA', 'dica': 'Coleção ordenada de itens em Python.'},
    {'palavra': 'DICIONARIO', 'dica': 'Coleção de pares chave-valor em Python.'},
    {'palavra': 'TUPLA', 'dica': 'Coleção ordenada e imutável de itens em Python.'},
    {'palavra': 'CONJUNTO', 'dica': 'Coleção de itens únicos não ordenados.'},
    {'palavra': 'STRING', 'dica': 'Tipo de dado para representar texto.'},
    {'palavra': 'INTEIRO', 'dica': 'Tipo de dado para números sem casas decimais.'},
    {'palavra': 'FLOAT', 'dica': 'Tipo de dado para números com casas decimais.'},
    {'palavra': 'BOOLEANO', 'dica': 'Tipo de dado com apenas dois valores: True ou False.'},
    {'palavra': 'REQUISICAO', 'dica': 'Pedido feito pelo cliente ao servidor (ex: GET, POST).'},
    {'palavra': 'RESPOSTA', 'dica': 'Dados devolvidos pelo servidor após uma requisição.'},
    {'palavra': 'CHAVE', 'dica': 'Identificador único num par chave-valor.'},
    {'palavra': 'VALOR', 'dica': 'Informação associada a uma chave.'},
    {'palavra': 'TABELA', 'dica': 'Estrutura de linhas e colunas num banco de dados.'},
    {'palavra': 'COLUNA', 'dica': 'Campo vertical de dados numa tabela.'},
    {'palavra': 'LINHA', 'dica': 'Registro horizontal completo numa tabela.'},
    {'palavra': 'CONSULTA', 'dica': 'Busca realizada num banco de dados (query).'},
    {'palavra': 'INDICE', 'dica': 'Estrutura que acelera buscas no banco de dados ou lista.'},
    {'palavra': 'CACHE', 'dica': 'Memória de acesso ultra-rápido para dados frequentes.'},
    {'palavra': 'LOG', 'dica': 'Registro de eventos que acontecem no sistema.'},
    {'palavra': 'ERRO', 'dica': 'Falha ou comportamento inesperado no programa.'},
    {'palavra': 'EXCECAO', 'dica': 'Erro que ocorre durante a execução do programa.'},
    {'palavra': 'EVENTO', 'dica': 'Ação detectada pelo programa (ex: clique de mouse).'},
    {'palavra': 'FLUXO', 'dica': 'Caminho de execução do código.'},
    {'palavra': 'DESIGN', 'dica': 'Planejamento e concepção da aparência e usabilidade.'},
    {'palavra': 'LAYOUT', 'dica': 'Disposição dos elementos visuais na tela.'},
    {'palavra': 'ESTILO', 'dica': 'Regras visuais aplicadas a elementos HTML.'},
    {'palavra': 'CSS', 'dica': 'Linguagem usada para estilizar páginas web.'},
    {'palavra': 'HTML', 'dica': 'Linguagem de marcação para estruturar páginas web.'},
    {'palavra': 'JAVASCRIPT', 'dica': 'Linguagem de programação que dá interatividade às páginas web.'},
    {'palavra': 'JSON', 'dica': 'Formato leve de troca de dados estruturado em texto.'},
    {'palavra': 'API', 'dica': 'Conjunto de rotinas que permite a comunicação entre diferentes sistemas.'},
    {'palavra': 'REST', 'dica': 'Estilo de arquitetura para serviços web.'},
    {'palavra': 'URL', 'dica': 'Endereço web de um recurso na internet.'},
    {'palavra': 'TOKEN', 'dica': 'Código de autenticação ou chave de acesso.'}
]

def jogo(request):
    if 'palavra' not in request.session:
        item_sorteado = random.choice(PALAVRAS_COM_DICAS)
        request.session['palavra'] = item_sorteado['palavra']
        request.session['dica'] = item_sorteado['dica']
        request.session['letras_chutadas'] = []
        request.session['tentativas_restantes'] = 6

    palavra_secreta = request.session['palavra']
    dica_palavra = request.session.get('dica', 'Palavra sobre tecnologia e programação.')
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
        'erros': 6 - request.session['tentativas_restantes'],
        'dica': dica_palavra,
        'ganhou': ganhou,
        'perdeu': perdeu,
        'palavra_correta': palavra_secreta,
    }
    return render(request, 'forca/jogo.html', context)

def reiniciar(request):
    request.session.flush()
    return redirect('jogo')