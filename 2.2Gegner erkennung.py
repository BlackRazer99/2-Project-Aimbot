#Identify Enemy and see if its possible to kill then kill with minimun Shots

playerinSight = input("Is the player friend or foe? ")
playerLife = int(input("How much life does the player have? "))
weaponEquiped = input("which Weapon did you Buy? ")


if playerinSight == "red":
    if playerLife <= 150 or weaponEquiped == "AWP":
        print("Use Aimbot") #if I had a functioning one
    else:
        print("Enemy has to much Health")
else:
    print("Friendly Fire is forbidden")

shotsFired = 0

#ignoring Health and Damage Calc for now as I do not now nor care

if weaponEquiped == "AK":
    shotsFired = 5
elif weaponEquiped == "Submachine Gun":
    shotsFired = 8
elif weaponEquiped == "Rifle":
    shotsFired = 2
else: shotsFired = 10

for shots in range(shotsFired):
    print("Shoot Aimboot")
