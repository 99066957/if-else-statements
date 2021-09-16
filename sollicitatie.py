

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+      Sollicitatieformulier  Ruimte-vuilnisman        +")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Er wordt u een aantal relevante vragen gesteld...")
print("Gelieve die naar eer en geweten in te vullen")
print("Als blijkt dat u aan de criteria voldoet dan komt u in")
print("aanmerking voor een serieus sollicitatiegesprek!")
print("Ontspan maar blijf wakker, hier komen de vragen")
print("--")
input("Druk op enter om te beginnen.")


naam = input("Wat is uw naam?")
diploma = input("Bent u in bezit van een Diploma MBO-4 ondernemen? J/N")
rijbewijs = input("Bent u in bezit van een geldig Vrachtwagen rijbewijs? J/N")
hoed = input("Heeft u een hoge hoed? J/N") 
cm = int(input("Wat is uw lichaamslengte?"))
kg = int(input("Wat is uw lichaamsgewicht?"))
certificiaat = input("Heeft u een Certificaat “Overleven met gevaarlijk personeel”? J/N")
geslacht = input("Van welk geslacht bent u? M/V")
if geslacht == 'M':
    snor = input('Heeft u een snor breder dan 10 cm? J/N')
else:
    snor = input('Heeft u rood krulhaar langer dan 20 cm? J/N')

if diploma == 'J' and rijbewijs == 'J' and hoed == 'J' and snor == 'J' and cm >= 150 and kg >= 90 and certificiaat == 'J':
    print("Proficiat! U komt in aanmerking voor een sollicitatiegesprek, stuur snel uw CV""")
    input("Klik enter om uw CV te versturen")
            
else:
    print(f"""---------------------------------------------------------------------------------------------
|Beste {naam},
|U voldoet niet aan onze strenge eisen voor de functie van Circusdirecteur, het spijt ons!
---------------------------------------------------------------------------------------------""")
    input('Klik enter om het programma af te sluiten')
        


   