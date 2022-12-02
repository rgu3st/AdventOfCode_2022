
def __init__():
    print("Does this run init?? No. :(")


def run_day_1():
    print("Reading day1 input.")

    inputData = []
    caloriesByElf = []

    with open("./Data/input_day1.txt", 'r') as fileData:
        inputData = fileData.readlines()


    print("Input data:")
    print(inputData)

    elfIndex:int = 0
    calories:int = 0

    for line in inputData:
        if line == "\n":
            caloriesByElf.append(calories)
            elfIndex += 1
            calories = 0
            continue

        calory_on_line = int(line.strip())
        calories += calory_on_line


    print(f"Num elfs: {elfIndex}")
    caloriesByElf.sort()
    print(f"Most calories is: {caloriesByElf[-1]}")

    print(f"Top three:{caloriesByElf[-1]}, {caloriesByElf[-2]}, {caloriesByElf[-3]}")
    print(f"Top three:{caloriesByElf[-3:]}")

    print(f"Total of top-3 calories are: {sum(caloriesByElf[-3:])}")