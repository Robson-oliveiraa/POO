from printt import text

class Atletas:
    def __init__(self,nome,sexo,forca,mLance,Fisico,Tecnica):
        self.nomeAtleta = nome
        self.sexoAtleta = sexo
        self.forcaAtleta = forca
        self.mLancaAtleta = mLance
        self.fisicoAtleta = Fisico
        self.tecnicaAtleta = Tecnica

    def carta(self):

        if self.sexoAtleta == "M":
            text(f"\033[0;33m\nNome do Atleta: {self.nomeAtleta}\n")
            text(f"\033[0;33mSexo do Atleta: {self.sexoAtleta} \n")
            text(f"\033[0;33mForça do Atleta: {self.forcaAtleta} \n")
            text(f"\033[0;33mMelhor Lançamneto do Atleta: {self.mLancaAtleta} \n")
            text(f"\033[0;33mCondicionamento Fisico do Atleta: {self.fisicoAtleta} \n")
            text(f"\033[0;33mTecnica do Atleta: {self.tecnicaAtleta} \n")
        else:
            text(f"\033[0;33m\nNome da Atleta: {self.nomeAtleta}\n")
            text(f"\033[0;33mSexo da Atleta: {self.sexoAtleta} \n")
            text(f"\033[0;33mForça da Atleta: {self.forcaAtleta} \n")
            text(f"\033[0;33mMelhor Lançamneto da Atleta: {self.mLancaAtleta} \n")
            text(f"\033[0;33mCondicionamento Fisico da Atleta: {self.fisicoAtleta} \n")
            text(f"\033[0;33mTecnica da Atleta: {self.tecnicaAtleta} \n")