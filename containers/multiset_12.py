from multiset import Multiset
from collections import Counter

c = Counter()

sentences = """
Počátek každodenní práce na poli formování pozice vyžaduje návrh a realizaci
směru progresivního rozvoje. Na druhé straně rámec stavu a vývoje postavení
vyžadují nalezení a jednoznačné upřesnění systému masové účasti. Vzájemné
postavení organizačních autorit stejně jako stabilní a kvantitativní vzrůst a
sféra naší aktivity napomáhá přípravě a realizaci nových návrhů. Stejně tak
stálé, informačně-propagandistické zabezpečení naší práce jednoznačně
předurčuje implementaci odpovídajících podmínek aktivizace. Nesmíme však
zapomínat, že konzultace se širokým aktivem vyzaduje rozšiřování logistických
prostředků a forem působení. Ideové úvahy nejvyššího řádu a rovněž upřesnění a
rozvoj struktur přetváří strukturu vedení dalších směrů rozvoje. Tímto způsobem
komplexní analýza našich možností od nás vyžaduje analýzy systému výchovy
pracovníků odpovídajících aktuálním potřebám. Závažnost těchto problémů je
natolik zřejmá, že nový model organizační činnosti zvyšuje potřebu aplikace
modelu rozvoje. Pestré a bohaté zkušenosti jasně říkají, že další rozvoj
různých forem činnosti představuje pozoruhodný experiment prověrky možnosti
nasazení veškerých dostupných prostředků. Každodenní praxe nám potvrzuje, že
počátek každodenní práce na poli formování pozice ve značné míře podmiňuje
vytvoření tvorby nových zdrojů.
"""

words = sentences.split()
c.update(words)

m = Multiset(c)
print(m)
