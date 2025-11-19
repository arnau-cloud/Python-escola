while True:
    renda = float(input("Introdueix la teva renda anual: "))
    if renda > 0:
        break
impost = float()
if renda <= 10000:
    impost = 0.05
if renda > 10000 and renda < 20000:
    impost = 0.15
if renda >= 20000 and renda < 35000:
    impost = 0.20
if renda >= 35000 and renda < 60000:
    impost = 0.30
if renda >= 60000:
    impost = 0.45

print(f"El teu impost és del {(impost * 100):.0f}%, un total de: {impost * renda}€")