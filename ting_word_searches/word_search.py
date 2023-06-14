def exists_word(word, instance):
    ocorrencias = []
    for index in range(0, instance.__len__()):
        nome_do_arquivo = instance.search(index)["nome_do_arquivo"]
        linhas_do_arquivo = instance.search(index)["linhas_do_arquivo"]
        for index, linha in enumerate(linhas_do_arquivo):
            if word.lower() in linha.lower():
                ocorrencias.append({"linha": index + 1})
    dicio = [
        dict(
            palavra=word,
            arquivo=nome_do_arquivo,
            ocorrencias=ocorrencias,
        )
    ]
    return dicio if ocorrencias else []


def search_by_word(word, instance):
    ocorrencias = []
    for index in range(0, instance.__len__()):
        nome_do_arquivo = instance.search(index)["nome_do_arquivo"]
        linhas_do_arquivo = instance.search(index)["linhas_do_arquivo"]
        for index, linha in enumerate(linhas_do_arquivo):
            if word.lower() in linha.lower():
                ocorrencias.append({"linha": index + 1, "conteudo": linha})
    dicio = [
        dict(
            palavra=word,
            arquivo=nome_do_arquivo,
            ocorrencias=ocorrencias,
        )
    ]
    return dicio if ocorrencias else []
