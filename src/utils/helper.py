import json # Json formatında işlemler gerçekleştirebilmek için kullanılır.
import os # İşletim sistemi (Operating System) işlemleri için kullanılır.

def getConfig() -> dict:
    """ Konfigürasyon dosya içeriğini Json formatında okur ve sözlük olarak döndürür. """
    with open("config.json", 'r', encoding='utf-8') as file:
        configDict = json.load(file)
    return configDict

def getLanguage(language:str="en") -> dict:
    """ Girilen dil dosyasının içeriğini sözlük olarak döndürür. """
    languageList = ["en", "tr"]
    language = language.lower()
    if language not in languageList:
        language == "en"
    languagePath = f"lang/{language}.json"
    with open(languagePath, 'r', encoding='utf-8') as file:
        langDict = json.load(file)
    return langDict

def getAPIKeys() -> dict:
    """ keys.json dosyasındaki API anahtarlarını sözlük olarak döndürür. """
    filePath = "keys.json"
    if not os.path.exists(filePath):
        defaultData = { "accessKey": "", "secretKey": "" }
        with open(filePath, 'w', encoding='utf-8') as file:
            json.dump(defaultData, file, indent=4)
    with open(filePath, 'r', encoding='utf-8') as file:
        apiKeysDict = json.load(file)
    return apiKeysDict

def clear():
    """ Konsolu temizler. """
    if os.name == 'nt': # İşletim sistemi Windows ise koşul sağlanır.
        os.system('cls') # CMD'nin 'cls' komutu ile konsol temizlenir.
    else: # İşletim sistemi Windows değil ise koşul sağlanır.
        os.system('clear') # Terminal'in 'clear' komutu ile konsol temizlenir.