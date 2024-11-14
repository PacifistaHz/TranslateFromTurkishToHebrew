from googletrans import Translator

# Çeviri fonksiyonunu tanımla
def translate_to_hebrew(text):
    translator = Translator()
    translation = translator.translate(text, src='tr', dest='he')
    return translation.text

# Kullanıcıdan Türkçe metin al
turkish_text = input("Türkçe metni giriniz: ")

# Metni İbranice'ye çevir
hebrew_text = translate_to_hebrew(turkish_text)

# Çeviriyi ekrana yazdır
print("İbranice Çeviri: " + hebrew_text)
