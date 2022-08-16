import re


class Automata():
    entero = "^(\+|-)?[0-9]+$"
    real = "^(\+|-)?[0-9]+(.|,)[0-9]+$"
    email = "^([a-z]|[A-Z])+([0-9]|([a-z]|[A-Z]))*@([a-z]|[A-Z])+.([a-z]|[A-Z]){3}(.([a-z]|[A-Z]){2})?$"
    cientifica = "^(\+|-)?[0-9]+((.|,)?[0-9]+)?(E|e)(\+|-)?[0-9]+$"

    def validacion(self, value):
        if re.match(self.entero, value):
            return 'Es un numero entero'
        elif re.match(self.real, value):
            return 'Es un numero real'
        elif re.match(self.cientifica, value):
            return 'Es un número con notación cientifica'
        elif re.match(self.email, value):
            return 'Es un e-mail'
        else:
            return 'No hay un valor valido'
