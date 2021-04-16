# Translator supports all google languages and supports it

import googletrans
print(googletrans.LANGUAGES)

#pip install translate

from translate import Translator
translator= Translator(to_lang="French")
translation = translator.translate("Hello Everyone, How are you doing?!")
print translation
