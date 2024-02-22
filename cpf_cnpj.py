from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('Tipo de documento inválido.')


class DocCpf:
    def __init__(self, documento):
        self._cpf = self.valida(documento)
    

    def valida(self, documento):
        documento = str(documento)
        validador = CPF()
        if validador.validate(documento):
            return documento
        else:
            raise ValueError("CPF inválido!")
        
        
    def mascara(self):
        mascara = CPF()
        return mascara.mask(self._cpf)
    

    def __str__(self):
        return self.mascara()
        

class DocCnpj:
    def __init__(self, documento):
        self._cnpj = self.valida(documento)
    

    def valida(self, documento):
        documento = str(documento)
        cnpj_validacao = CNPJ()
        if cnpj_validacao.validate(documento):
            return documento
        else:
            raise ValueError("CNPJ inválido!")
 

    def mascara(self):
        mascara = CNPJ()
        return mascara.mask(self._cnpj)
     

    def __str__(self):
        return self.mascara()
