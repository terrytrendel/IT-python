import journal
from banner import banner
banner("DEEP THOUGHTS", "TRENDEL")

def main():
    run_event_loop()

def run_event_loop():
    filename = "default"
    journal_data = journal.load(filename)

    while True:
        command = input("[L]ist entries, [A]dd an entry, E[x]it: ")

        if command == "L":
            list_entries(journal_data)
        elif command == "A":
                add_entry(journal_data)
        elif command.upper() == "X":
                    break
        else:
            print("sorry, i dont understand")
    journal.save(filename, journal_data)



def list_entries(data):
    print("Your journal entries:")
    entries = reversed(data)
    for num, entry in enumerate(entries):
        print(f"{num+1} - {entry}")






def add_entry(data):
    entry = input("type your entry, <ENTER> to exit: \n")
    journal.add_entry(entry, data)
    #data.append(entry)












main()