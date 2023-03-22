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

        text(f"\033[0;33m\nNome do Atleta: {self.nomeAtleta}\n")
        text(f"\033[0;33mSexo do(a) Atleta: {self.sexoAtleta} \n")
        text(f"\033[0;33mForça do(a) Atleta: {self.forcaAtleta} \n")
        text(f"\033[0;33mMelhor Lançamneto do(a) Atleta: {self.mLancaAtleta} \n")
        text(f"\033[0;33mCondicionamento Fisico do(a) Atleta: {self.fisicoAtleta} \n")
        text(f"\033[0;33mTecnica do(a) Atleta: {self.tecnicaAtleta} \n")