PNG_MAGIC_NUMBER = b'\x89PNG\r\n\x1a\n'

class TextColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    VALUE = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def setValueColor(text):
        return TextColors.VALUE + text + TextColors.ENDC