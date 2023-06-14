import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(0, instance.__len__()):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    dicio = dict(
        nome_do_arquivo=path_file,
        qtd_linhas=len(txt_importer(path_file)),
        linhas_do_arquivo=txt_importer(path_file),
    )
    instance.enqueue(dicio)
    print(instance.search(0), file=sys.stdout)


def remove(instance):
    if instance.__len__() == 0:
        print("Não há elementos", file=sys.stdout)
    else:
        path_file = instance.search(0)["nome_do_arquivo"]
        instance.dequeue()
        print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    if not 0 <= position <= instance.__len__():
        print("Posição inválida", file=sys.stderr)
    else:
        print(instance.search(position), file=sys.stdout)
