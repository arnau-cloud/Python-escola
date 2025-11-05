sou_presi = int(input("Escriu el sou del president: "))
print("El sou del president és: " + str(sou_presi))

sou_dir = int(input("Escriu el sou del director: "))
print("El sou del director és: " + str(sou_dir))

sou_cap = int(input("Escriu el sou del cap: "))
print("El sou del cap és: " + str(sou_cap))

sou_administratiu = int(input("Escriu el sou del administratiu: "))
print("El sou del administratiu és: " + str(sou_administratiu))

if sou_administratiu < sou_cap < sou_dir <sou_presi:
    print("Els sous son correctes")

else:
    print("Els sous son incorrectes")