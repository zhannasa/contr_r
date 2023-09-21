import json
import os
from datetime import datetime

def create_note():
    title = input("Enter the note title: ")
    body = input("Enter the note body: ")
    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M")  
    note = {"id": generate_id(), "title": title, "body": body, "timestamp": timestamp}
    return note

def generate_id():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
            if notes:
                last_note = notes[-1]
                return last_note["id"] + 1
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        pass
    return 1

def save_note(note):
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        notes = []

    notes.append(note)

    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)  

def list_notes():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
            for note in notes:
                print(f"ID: {note['id']}, Title: {note['title']}, Create time: {note['timestamp']}")
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("Notes list is empty.")

def edit_note():
    note_id = int(input("Enter note ID to edit: "))
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("Notes list is empty.")
        return

    for note in notes:
        if note["id"] == note_id:
            new_title = input("Enter the new note title: ")
            new_body = input("Enter the new note body: ")
            note["title"] = new_title
            note["body"] = new_body
            note["timestamp"] = datetime.now().strftime("%d.%m.%Y %H:%M")
            with open("notes.json", "w") as file:
                json.dump(notes, file)
            print("Note is edited.")
            return

    print("Note with this ID is not found.")

def delete_note():
    note_id = int(input("Enter note ID to delete: "))
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("Notes list is empty.")
        return

    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            with open("notes.json", "w") as file:
                json.dump(notes, file)
            print("Note is deleted.")
            return

    print("Note with this ID is not found.")

def filter_notes_by_date():
    date_str = input("Enter the date (d.m.y) to filter notes by date: ")
    try:
        selected_date = datetime.strptime(date_str, "%d.%m.%Y")
    except ValueError:
        print("Incorrect date format. Use the format 'd.m.y'.")
        return

    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("Notes list is empty.")
        return

    filtered_notes = [note for note in notes if datetime.strptime(note["timestamp"], "%d.%m.%Y %H:%M").date() == selected_date.date()]

    if filtered_notes:
        print("\nNotes by selected date:")
        for note in filtered_notes:
            print(f"ID: {note['id']}, Title: {note['title']}, Create date: {note['timestamp']}")
    else:
        print("Notes by selected date are not found.")

def view_note_by_id():
    note_id = int(input("Enter note ID to view: "))
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("Notes list is empty.")
        return

    for note in notes:
        if note["id"] == note_id:
            print(f"\nNote with ID {note_id}:")
            print(f"Title: {note['title']}")
            print(f"Note body:\n{note['body']}")
            print(f"Note time: {note['timestamp']}")
            return

    print("Note with this ID is not found.")

def main():
    while True:
        print("\nChoose the option:")
        print("1. Create note")
        print("2. Edit note")
        print("3. Delete note")
        print("4. List notes")
        print("5. Filter notes by date")
        print("6. View note by ID")
        print("7. Exit")


        choice = input("Enter the option number: ")

        if choice == "1":
            note = create_note()
            save_note(note)
            print("Your note is saved.")
        elif choice == "2":
            edit_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("\nHere you have your notes list:")
            list_notes()
        elif choice == "5":
            filter_notes_by_date()
        elif choice == "6":
            view_note_by_id()
        elif choice == "7":
            print("Exit from program.")
            break
        else:
            print("Your choice is incorrect. Please, choose the existing option number.")
    
if __name__ == "__main__":
    main()



