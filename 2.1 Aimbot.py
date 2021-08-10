#Aimbot

goalPosition = [100, 100]

startPosition = [int(input("Add your Start Coordinate for x " )), int(input("Add your Start Coordinate for y "))]


while startPosition[0] != goalPosition[0]:
    while startPosition[1] != goalPosition[1]:
        print(startPosition[1])
        startPosition[1] = startPosition[1] + 1
        if startPosition[1] == goalPosition[1] :
            print("ZielPosition Y achse Erreicht")
    print(startPosition[0])
    startPosition[0] = startPosition[0] + 1
    if startPosition[0] == goalPosition[0] :
            print("ZielPosition X achse Erreicht")

print(startPosition)
