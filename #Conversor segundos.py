#Conversor segundos

def convertir_segundos(segundos):
    """
    Convert seconds to hours, minutes and seconds
    """
    horas = segundos // 3600
    minutos = (segundos - horas * 3600) // 60
    segundos_restantes = segundos - horas * 3600 - minutos * 60
    return horas, minutos, segundos_restantes
