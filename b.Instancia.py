class Palindromo():
      miCadenaDeTexto = ""
  def __init__(self,miCadenaDeTexto):
    self.miCadenaDeTexto=miCadenaDeTexto

  def Test(self):
    miCadenaDeTexto=self.miCadenaDeTexto
    def quita_acentos(s):
      replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
      for a, b in replacements:
        s = s.replace(a, b)
        return s
        #s cadena sin tildes
# y lo pongo en minisculas
    if quita_acentos(miCadenaDeTexto).lower()== quita_acentos(miCadenaDeTexto).lower()[::-1]:
      
      return True
      
    else:
      
      return False
      