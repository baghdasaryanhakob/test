data = [
    [23, 11, 5, 14],
    [8, 32, 20, 5]
]
color = input("Enter color: ")

brown = 0
blue = 1
green = 2
black = 3

total = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        total += data[i][j]

if color == "brown":
    brown_color = data[0][brown] + data[1][brown]
    brown_share = int(round(brown_color / total * 100, 2))
    print(brown_share)

if color == "blue":
    blue_color = data[0][blue] + data[1][blue]
    blue_share = int(round(blue_color / total * 100, 2))
    print(blue_share)

if color == "green":
    green_color = data[0][green] + data[1][green]
    green_share = int(round(green_color / total * 100, 2))
    print(green_share)

if color == "black":
    black_color = data[0][black] + data[1][black]
    black_share = int(round(black_color / total * 100, 2))
    print(black_share)

