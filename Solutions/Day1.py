import csv

def read_file():
    with open('./input/day1input.csv', 'r', encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        return list(reader)

def split_list_left():
    return [int(row[0]) for row in read_file()]  # Convert to integers

def split_list_right():
    return [int(row[1]) for row in read_file()]  # Convert to integers

def calc_difference(left_list, right_list):
    total = 0
    for left, right in zip(left_list, right_list):  # Pair elements from both lists
        total += abs(left - right)  # Calculate absolute difference
    return total

def solve_day1():
    left_list = split_list_left()
    right_list = split_list_right()

    left_list.sort()
    right_list.sort()

    difference = calc_difference(left_list, right_list)
    print(f"Total difference: {difference}")


solve_day1()