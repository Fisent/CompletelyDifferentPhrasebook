from glosbe_access import Glosbe

g = Glosbe(from_lang='eng', dest_lang='pol')

print(g.translate('shoe'))

