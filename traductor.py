from translate import Translator
translator = Translator(from_lang="spanish", to_lang="english")

text=input("Que deseas traducir: \n")
resp= translator.translate(text)
print(resp)