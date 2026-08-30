import random
grid = [["." for i in range(5)] for i in range(5)]
food_row = random.randint(0,4)
food_col = random.randint(0,4)
grid[food_row][food_col] = "F"

while True:
    snake_row = int(input("Enter the row value: "))
    snake_col = int(input("Enter the column value: "))
    if 0 <= snake_row < 5 and 0 <= snake_col < 5:
        grid[snake_row][snake_col] = "S"
    else:
        print("Please retry again with a value between 0 and 4")
        continue
    if snake_row == food_row and snake_col == food_col:
        for row in grid:
            for item in row:
                print(item,end=" ")
            print()
        print("Yum! The snake ate the food!")
        break
    else:
        for row in grid:
            for item in row:
                print(item,end=" ")
            print()
        grid[snake_row][snake_col] = "."
