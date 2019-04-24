#Ce code ouvre un fichier, le lit et ????
#Ce code utilise NLTK, generate, et CFG
#cfg = configuration file parser

from nltk.parse.generate
import generate
from nltk import CFG

grammaire_base = open('./bureau/cfg/noms.txt', encoding='utf-8').read()
grammaire = CFG.fromstring(grammaire_base)

for phrase in generate(grammaire, n=50)
print(''.join(phrase))
