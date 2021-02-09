import time
import json
import datetime

invalid = "\n--Invalid response, please try again.--"
scheduleFile = "C:/Users/Ben/Desktop/Scheduler/schedule.json"
assignmentFile = "C:/Users/Ben/Desktop/Scheduler/assignment.json"

def load():
    for i in range(0, 40):
        time.sleep(0.00000000000001)
        print("-", end='', flush=True)
    print()

def unload():
    for i in range(0, 40):
        time.sleep(0.00000000000001)
        print('-' * (40 - i))
    print("--Goodbye!--")

def anythingElse():
    load()
    while True:
        userInput = input("Anything else?\n[0] - Yes\n[1] - No\n\nPlease choose an option: ")
        if userInput == "0":
            load()
            break
        elif userInput == "1":
            unload()
            return 1
        else:
            print(invalid)

def createSchedule():
    with open(scheduleFile) as f:
        data = json.load(f)
    while True:
        sched = input("Schedule Name: ")
        if sched not in data:
            break
        print(f'"{sched}" is already a schedule. Please enter a different name.')
    data[sched] = {}
    while True:
        number = input("Number of Classes (1 - 7): ")
        try:
            number = int(number)
            if number > 7 or number < 1:
                print(invalid)
            else:
                break
        except Exception:
            print(invalid)
    for i in range(1, number + 1):
        name = input(f"\nPeriod {i}: ")
        teacher = input("Teacher: ")
        description = input("Description: ")
        data[sched][name] = {}
        data[sched][name]["teacher"] = teacher
        data[sched][name]["description"] = description
    with open(scheduleFile, "w") as f:
        json.dump(data, f, indent=2)
    load()
    print(f'--Schedule "{sched}" created!--')

def seeSchedule():
    with open(scheduleFile) as f:
        data = json.load(f)
    if len(data) < 1:
        print("--There are currently no schedules.--")
        return
    num = 0
    while True:
        lister = []
        for i in data:
            lister += [i]
            print(f"[{num}] {i}\nPeriods: {len(data[i])}\n")
            num += 1
        num -= 1
        userInput = input("Please choose a schedule (or press e to exit): ")
        if userInput == "e":
            return
        else:
            try:
                userInput = int(userInput)
                if userInput > -1 and userInput <= num:
                    num = 0
                    load()
                    for i in data[lister[userInput]]:
                        print(f"Period {num + 1}: {i}\nTeacher: {data[lister[userInput]][i]['teacher']}\nDescription: {data[lister[userInput]][i]['description']}\n")
                        num += 1
                    userInput = input("Enter any key to return: ")
                    load()
                else:
                    print(invalid)
            except Exception:
                print(invalid)

def deleteSchedule():
    with open(scheduleFile) as f:
        data = json.load(f)
    if len(data) < 1:
        print("--There are currently no schedules.--")
        return
    num = 0
    while True:
        lister = []
        for i in data:
            lister += [i]
            print(f"[{num}] {i}\nPeriods: {len(data[i])}\n")
            num += 1
        num -= 1
        userInput = input("Please choose a schedule to delete (or press e to exit): ")
        if userInput == "e":
            return
        else:
            print()
            try:
                userInput = int(userInput)
                if userInput > -1 and userInput <= num:
                    num = 0
                    confirm = input(f'Are you sure you want to delete "{lister[userInput]}"?\nEnter "13579" to confirm, or enter anything else to cancel: ')
                    if confirm == "13579":
                        load()
                        del data[i]
                        with open(scheduleFile, "w") as f:
                            json.dump(data, f, indent=2)
                        userInput = input("--Schedule has been deleted.--\n\nEnter any key to return: ")
                        print()
                        break
                    else:
                        return
                else:
                    print(invalid)
            except Exception:
                print(invalid)

def createAssignment():
    with open(assignmentFile) as f:
        data = json.load(f)
    while True:
        name = input("Assignment Name: ")
        if name not in data:
            break
        else:
            print(f'"{name}" is already an assignment. Please enter a different name.')
    classname = input("Class: ")
    while True:
        due = input('Due Date (mm/dd/yyyy): ')
        try:
            s = datetime.date(int(due.split("/")[2]), int(due.split("/")[1]), int(due.split("/")[0]))
            n = datetime.datetime.now().date()
            if s > n and len(due.split("/")) == 3:
                break
            elif(s <= n):
                print("\n--That date has already passed. Please enter a different response.--")
            else:
                print(invalid)
        except Exception:
            print(invalid)
    description = input("Description: ")
    data[name] = {}
    data[name]["class"] = classname
    data[name]["due"] = due
    data[name]["description"] = description
    with open(assignmentFile, "w") as f:
        json.dump(data, f, indent=2)
    load()
    print(f'--Assignment "{name}" created!--')

def seeAssignment():
    with open(assignmentFile) as f:
        data = json.load(f)
    if len(data) < 1:
        print("--There are currently no assignments.--")
        return
    num = 0
    for i in data:
        print(f"[{num}] Assignment: {i}{len(data[i])}\n{' ' * len(str(len(data[i])))}   Class: {data[i]['class']}\n{' ' * len(str(len(data[i])))}   Due Date: {data[i]['due']}\n{' ' * len(str(len(data[i])))}   Description: {data[i]['description']}\n")
        num += 1
    userInput = input("Press any key to return: ")

def deleteAssignment():
    with open(assignmentFile) as f:
        data = json.load(f)
    lister = [x for x in data]
    if len(data) < 1:
        print("--There are currently no assignments.--")
        return
    num = 0
    for i in data:
        print(f"[{num}] Assignment: {i}{len(data[i])}\n{' ' * len(str(len(data[i])))}   Class: {data[i]['class']}\n{' ' * len(str(len(data[i])))}   Due Date: {data[i]['due']}\n{' ' * len(str(len(data[i])))}   Description: {data[i]['description']}\n")
        num += 1
    num -= 1
    while True:
        try:
            userInput = input("Please choose an assignment to delete (or press e to exit): ")
            if userInput == "e":
                return
            elif int(userInput) > -1 and int(userInput) <= num:
                confirm = input(f'\nAre you sure you want to delete "{lister[int(userInput)]}"?\nEnter "13579" to confirm, or enter anything else to cancel: ')
                if confirm == "13579":
                    del data[lister[int(userInput)]]
                    with open(assignmentFile, "w") as f:
                        json.dump(data, f, indent=2)
                    userInput = input("--Assignment has been deleted.--\n\nEnter any key to return: ")
                    print()
                    break
            else:
                print(invalid)
        except Exception as e:
            print(e)

def programChoice():
    while True:
        userInput = input("[0] - Create a schedule\n[1] - See existing schedules\n[2] - Delete a schedule\n[3] - Create an assignment\n[4] - Create an assignment\n[5] - Delete a schedule\n\nPlease choose the program you would like to use: ")
        if userInput == "0":
            load()
            createSchedule()
            if anythingElse() == 1:
                break
        elif userInput == "1":
            load()
            seeSchedule()
            if anythingElse() == 1:
                break
        elif userInput == "2":
            load()
            deleteSchedule()
            if anythingElse() == 1:
                break
        elif userInput == "3":
            load()
            createAssignment()
            if anythingElse() == 1:
                break
        elif userInput == "4":
            load()
            seeAssignment()
            if anythingElse() == 1:
                break
        elif userInput == "5":
            load()
            deleteAssignment()
            if anythingElse() == 1:
                break
        else:
            print(invalid)

def main():
    print("\n\n-----Welcome to Scheduler.py, a program made to schedule classes and assignments.-----")
    while True:
        userInput = input("[0] - Begin\n[1] - Quit\n\nPlease choose an option: ")
        if userInput == "0":
            load()
            programChoice()
            break
        elif userInput == "1":
            unload()
            break
        else:
            print(invalid)

main()