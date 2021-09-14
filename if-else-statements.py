print("Type ja of nee")
true = str(input("Is de kaas geel?"))
if true == "ja":
    true = str(input("Zitten er gaten in?"))
    if true == "ja":
        true = str(input('Is de kaas belachelijk duur?'))
        if true == "ja":
            print("Emmenthaler")
            input("Druk op enter om het aftesluiten.")
        if true == "nee":
            print("Leerdammer")
            input("Druk op enter om het aftesluiten.")      
    elif true == "nee":
        true = str(input('Is de kaas hard als steen?'))
        if true == "ja":
            print("Pamigiano Reggiano")
            input("Druk op enter om het aftesluiten.")  
        if true == "nee":
            print("Goudse Kaas")
            input("Druk op enter om het aftesluiten.") 
if true == "nee":
    true = str(input("Heeft de kaas blauwe schimmels?"))
    if true == "nee":
        true = str(input("Heeft de kaas een korst?"))
        if true == "ja":
            print("Camembert")
            input("Druk op enter om het aftesluiten.")
        if true == "nee":
            print("Mozzarella")
            input("Druk op enter om het aftesluiten.") 
    elif true == "ja":
        true = str(input("Heeft de kaas een korst?"))
        if true == "ja":
            print("Bleu de Rochbaron")
            input("Druk op enter om het aftesluiten.")
        if true == "nee":
            print("Fourme d'Ambert")
            input("Druk op enter om het aftesluiten.")





        



