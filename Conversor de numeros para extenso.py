class ConverterExtenso:
    def __init__(self, dinheiro):
        self.numeros_por_extenso = dict(n0="", n1="UM", n2="DOIS", n3="TRÊS", n4="QUATRO", n5="CINCO", n6="SEIS",
                                        n7="SETE", n8="OITO", n9="NOVE", n10="DEZ", n11="ONZE", n12="DOZE", n13="TREZE",
                                        n14="QUATORZE", n15="QUINZE", n16="DEZESSEIS", n17="DEZESETE,", n18="DEZOITO",
                                        n19="DEZENOVE", n20="VINTE", n30="TRINTA", n40="QUARENTA", n50="CINQUENTA",
                                        n60="SESSENTA", n70="SETENTA", n80="OITENTA", n90="NOVENTA", n100="CENTO",
                                        n200="DUZENTOS", n300="TREZENTOS", n400="QUATROCENTOS", n500="QUINHENTOS",
                                        n600="SEISCENTOS", n700="SETECENTOS", n800="OITOCENTOS", n900="NOVECENTOS")

        self.dinheiro = dinheiro
        self.milhao_reais = self.converter(dinheiro.split(",")[0][:-6])
        self.milhar_reais = self.converter(dinheiro.split(",")[0][:-3][-3:])
        self.reais = self.converter(dinheiro.split(",")[0][-3:])
        self.centavos = self.converter(dinheiro.split(",")[-1])

        self.resultado = ""

    def converter(self, numero):
        if str(numero) == "":
            return ""
        if int(numero) < 21:
            return self.numeros_por_extenso["n" + str(int(numero))]
        if int(numero) < 100:
            if str(numero)[-1] != "0":
                return self.numeros_por_extenso["n" + str(numero)[-2] + "0"] + " E " + self.converter(numero[-1])
            return self.numeros_por_extenso["n" + str(numero)[-2] + "0"]
        if int(numero) == 100:
            return "CEM"
        if self.converter(numero[-2:]) == "":
            return self.numeros_por_extenso["n" + str(numero)[-3] + "00"]
        return self.numeros_por_extenso["n" + str(numero)[-3] + "00"] + " E " + self.converter(numero[-2:])

    def regras_gramaticais(self):
        if self.milhao_reais != "":
            if self.milhao_reais == "UM":
                self.milhao_reais += " MILHÃO"
            else:
                self.milhao_reais += " MILHÕES"
        if self.milhar_reais != "":
            if self.milhar_reais != "UM":
                self.milhar_reais += " MIL"
            else:
                self.milhar_reais = "MIL"
            if self.reais != "":
                if self.dinheiro.split(",")[0][-3:][0] == "0":
                    self.reais = "E " + self.reais
                if (self.dinheiro.split(",")[0][-3:][1:]) == "00":
                    self.reais = "E " + self.reais
        if self.milhar_reais != "":
            if self.reais != "":
                self.milhar_reais += " "
        if int(self.dinheiro.split(",")[0]) >= 1:
            if self.reais == "UM":
                self.reais += " REAL"
            else:
                self.reais += " REAIS"
            if self.dinheiro.split(",")[0][-6:] == "000000":
                self.reais = " DE REAIS"
        if self.centavos != "":
            if self.centavos == "UM":
                self.centavos = self.centavos + " CENTAVO"
            else:
                self.centavos = self.centavos + " CENTAVOS"
            if int(self.dinheiro.split(",")[0]) >= 1:
                self.centavos = " E " + self.centavos
        if self.milhao_reais != "":
            if self.milhar_reais != "":
                self.milhao_reais += " "

        self.resultado = self.milhao_reais + self.milhar_reais + self.reais + self.centavos

    def __repr__(self):
        self.regras_gramaticais()
        return self.resultado
