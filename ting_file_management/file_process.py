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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
