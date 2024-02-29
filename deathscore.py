import os
import time

def show_lifetime_data():
    try:
        with open("lifetime/lifetime.txt", "r") as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print("Lifetime data file not found.")

def show_weekly_data(week_number):
    try:
        file_path = f"weekly/week {week_number}.txt"
        with open(file_path, "r") as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print(f"Weekly data for week {week_number} not found.")

def main():
    gamemode = input("Choose a gamemode (lifetime/weekly): ").lower()

    if gamemode == "lifetime":
        show_lifetime_data()
    elif gamemode == "weekly":
        week_number = input("What week? ")
        try:
            week_number = int(week_number)
            show_weekly_data(week_number)
        except ValueError:
            print("Please enter a valid week number.")
    else:
        print("Invalid gamemode.")

if __name__ == "__main__":
    main()
