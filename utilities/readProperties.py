import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getBaseURL():
        url=config.get('common info','LandingPage_URL')
        return url

    @staticmethod
    def getPenghasilan():
        penghasilan=config.get('common info','penghasilan')
        return penghasilan
    
    @staticmethod
    def getInflasi():
        Inflasi=config.get('common info','inflasi')
        return Inflasi

    @staticmethod
    def getUsiaKini():
        UsiaKini=config.get('common info','UsiaKini')
        return UsiaKini

    @staticmethod
    def getUsiaPensiun():
        UsiaPensiun=config.get('common info','UsiaPensiun')
        return UsiaPensiun

    @staticmethod
    def getGayaRasio():
        GayaRasio=config.get('common info','gaya_rasio')
        return GayaRasio

    @staticmethod
    def getLamaPensiun():
        LamaPensiun=config.get('common info','lama_pensiun')
        return LamaPensiun

    @staticmethod
    def getSukuBunga():
        SukuBunga=config.get('common info','suku_bunga')
        return SukuBunga

    @staticmethod
    def getEmail():
        Email=config.get('common info','email')
        return Email

    @staticmethod
    def getPhone():
        Phone=config.get('common info','phone')
        return Phone

    @staticmethod
    def getAddress():
        Address=config.get('common info','address')
        return Address

    @staticmethod
    def getUsiaKini2():
        UsiaKini2=config.get('common info','UsiaKini2')
        return UsiaKini2

    @staticmethod
    def getUsiaPensiun2():
        UsiaPensiun2=config.get('common info','UsiaPensiun2')
        return UsiaPensiun2

    
    
        
