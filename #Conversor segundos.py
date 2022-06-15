#Conversor segundos

def convert_seconds(seconds):
    """
    Convert seconds to hours, minutes and seconds
    """
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
