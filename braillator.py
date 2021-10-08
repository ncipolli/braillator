original = "abcdefghijklmnopqrstuvwxyz0123456789çàáéíóúâêôãõ.,;:?!-"

braille = "⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠯⠫⠷⠿⠌⠬⠾⠡⠣⠹⠜⠪⠄⠂⠆⠒⠢⠖⠤"

ap = "⠣⠄"   # abre parênteses
fp = "⠠⠜"   # fecha parênteses
tr = "⠤⠤"   # travessão

num = "⠼"   # indicador numérico
mai = "⠨"   # indicador maiúscula
cxa = "⠨⠨"  # indicador caixa alta
gis = "⠔"   # indicador grifo, itálico e sublinhado


transtab = str.maketrans(original, braille)

text = "alô alô marciano , aqui quem fala é da terra !"

cont = text.split()

for i in range(len(cont)):
  if cont[i].isdigit():
    cont[i] = num + str(cont[i]).translate(transtab)
  if cont[i] == '(':
    cont[i] = ap
  if cont[i] == ')':
    cont[i] = fp
  if cont[i] == '_':
    cont[i] = tr
  else:
    cont[i] = str(cont[i]).translate(transtab)

conte = " ".join(cont)
traducao = str(conte)

arquivo = open('trad.txt', 'w', encoding='utf-8')
arquivo.writelines(traducao)
arquivo.close()