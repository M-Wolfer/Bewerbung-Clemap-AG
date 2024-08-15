#coding=utf-8
#Deklaration
corpus = 'Danke für das Job Interview es hat mich sehr gefreut. Der Unterschied zwischen Energie und Leistung macht die Abhänigkeit der Zeit, ja. Die Scheinleistung kommt ins Spiel wenn Kapazitaeten und Induktivitaeten im Verbraucher sind. Unabhaengig von der Zeit wuensche ich einen schoenen erholsamen Urlaub und danke fuer die Zeit sowie das Interview. Marius'
woerter = {}
einzelwoerter_pure = []

#Entfernen von Sonderzeichen
einzelwoerter = corpus.split(" ")
for x in einzelwoerter:
    x = x.replace(".","")
    x = x.replace(",","")
    einzelwoerter_pure.append(x)
print(einzelwoerter_pure)

#Füllen von Dictionary
for x in einzelwoerter_pure:
    anzahl = einzelwoerter_pure.count(x)
    woerter[x] = anzahl
    
#Sortieren des Dictionary
top_3 = dict(sorted(woerter.items(), key=lambda item: item[1], reverse=True)[:3])
print(top_3)

