
def get_ultima_imagem(paciente):
    try:
        return paciente.imagens_paciente.order_by('-id_imagem_paciente')[0]
    except IndexError:
        return None
