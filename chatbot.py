import os


def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} Entre no site www... e acesse inscrever-se, atenda todos os requisitos, e pronto!{os.linesep}')
    elif resposta == '2':
        print(
            f'{os.linesep}{nome} a idade minima é de 16 anos, e a maxima de 40 anos.{os.linesep}')
    elif resposta == '3':
        print(
            f'{os.linesep}{nome} Todos os da região de Limeira e americana.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} São 5 vagas no total.{os.linesep}')
    elif resposta == '5':
        print(f'{os.linesep}{nome} A avaliação vai ser feita por meio de duas etapas, a primeira sera um teste fisico de resistencia, ja a segunda será feita por meio de 2 partidas treino, uma com a nossa equipe atual e outra somente entre os participantes, o cadidato se destacando em qualquer uma das duas poderá ser escolhido por nossos avaliadores.{os.linesep}')
    elif resposta == '6':
        print(f'{os.linesep}{nome}As inscrições abrem no dia 15 de Janeiro do ano atual, e se encerra dia 20 de Fevereiro do ano atual. Já a avaliação sera feita dia 10 de março do ano atual!.{os.linesep}')

    else:
        print("Digite apenas 1, 2, 3, 4, 5 ou 6!")


def start():
    print('Olá! Bem-vindo a Black Bulls!')

    nome = input('Digite seu nome:')
    email = input('Digite seu e-mail:')
    while True:

        resposta = input(
            f'Como posso te ajudar meu cadidato?{os.linesep}[1] - Como faço para entrar no time?{os.linesep}[2] - Qual á idade minima?{os.linesep}[3] - Quais campeonatos iremos participar?{os.linesep}[4] - Quantas vagas possuem?{os.linesep}[5] - Como será feito á avaliação?{os.linesep}[6] - Qual a data de inscrição?{os.linesep}')

        processar_resposta(resposta, nome)


if __name__ == '__main__':
    start()
