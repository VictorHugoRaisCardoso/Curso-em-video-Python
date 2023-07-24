def notas(*nota, sit=False):
    '''
<<< NOTAS >>>
    => Função para analizar a nota e situação de vários alunos.
    :Parametro nota: Aceita uma ou mais notas de alunos.
    :Parametro sit: valor opcional, se verdadeiro (True), exibe a situação atual da turma (RUIM, RASOAVEL, BOA)
    :return: Retorna um dicionário com todas as informações sobre a respeito da turma.
    '''
    resumo = dict()
    resumo ['Total de notas'] = len(nota)
    resumo ['Maior nota'] = max(nota)
    resumo ['Menor nota'] = min(nota)
    resumo ['Media'] = sum(nota) / len(nota)
    if sit:
        if resumo['Media'] <= 5.9:
            resumo['Situação'] = 'RUIM'
        elif resumo['Media'] <= 6.9:
            resumo['Situação'] = 'RASOAVEL'
        elif resumo['Media'] >= 7:
            resumo['Situação'] = 'BOA'
    return resumo

resp = notas(5.5, 3.5)
print(resp)
