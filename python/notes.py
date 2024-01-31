import json
import os


def main_menu(data: dict, id_note: int):
    while True:

        print('Выберите действие: ')
        print('1 - создать новую заметку')
        print('2 - вывести содержание заметки')
        print('3 - удалить заметку')
        print('4 - редактировать содержание заметки')
        print('5 - вывести список заметок')
        print('6 - вывести заметки с датой')
        print('  - выход из программы')
        
        get = input('Введите действие: ')
        if get == '':
            print('До свидания!')
            with open(json_file_path, 'w') as file: # write new notebook back to json
                json.dump(data, file, indent=2)
            break
        elif get == '1':
            data = create(data, id_note, get_data())
            id_note += 1

        elif get == '2':
            note_id = input('Введите ID заметки: ')
            print (data[note_id])
            
        elif get == '3':
            note_id = input('Введите ID заметки: ')
            data.pop(note_id, None)

        elif get == '4':
            note_id = input('Введите ID заметки: ')
            data = create(data, note_id, get_data())
        
        elif get == '5':
            print_notes_book(data)
        elif get == '6':
            date = get_date()
            for note in data.values():
                if note[2] == date:
                    print(note)

        else:
            print('Некорректный ввод данных, введите ещё раз: ')

def create(data: dict, id: int, elem: list) -> dict: # add new note
    data[id] = elem
    return data

def print_notes_book(data: dict) -> None:
    for key, values in data.items():
        print(f'{key} {values}')

from datetime import datetime

def get_data() -> list: # ask user data
    note_title = input('Введите заголовок заметки: ')
    note_text = input('Введите текст заметки: ')
    current_time = datetime.now()
    note_time = current_time.strftime("%Y-%m-%d")
    return [note_title, note_text, note_time]

def get_date(): # ask user date
    user_date = input('Введите дату заметки (в формате "YYYY-mm-dd"): ')
    return (user_date)



json_file_path = 'notes.json'

if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as file:
        batch_data = json.load(file)
else:
    batch_data = {}

id_note = int(sorted(batch_data.keys())[-1]) + 1


main_menu(batch_data, id_note)