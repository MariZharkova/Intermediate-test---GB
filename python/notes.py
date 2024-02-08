from datetime import datetime
import json
import os


def main_menu(data: dict, id_note: int):
    print_prompt = True
    while True:

        if print_prompt:
            print('Выберите действие и нажмите "Enter": ')
            print('1 - создать новую заметку')
            print('2 - вывести содержание заметки')
            print('3 - удалить заметку')
            print('4 - редактировать содержание заметки')
            print('5 - вывести список заметок')
            print('6 - вывести заметки с определённой датой')
            print('Для выхода из программы нажмите "Enter"')

        get = input('Введите действие: ')
        if get == '':
            print('До свидания!')
            try:
                with open(json_file_path, 'w') as file:  # write new notebook back to json
                    json.dump(data, file, indent=2)
            except Exception as e:
                print("Ошибка записи в файл {e}")
            break
        elif get == '1':
            data = create(data, id_note, get_data())
            id_note += 1

        elif get == '2':
            get_id = input('Введите ID заметки: ')
            if get_id in data.keys():
                print(data[get_id][1])
            else:
                print('Такой ID не существует')

        elif get == '3':
            get_id = input('Введите ID заметки: ')
            if get_id in data.keys():
                data.pop(get_id, None)
            else:
                print('Такой ID не существует')

        elif get == '4':
            get_id = input('Введите ID заметки: ')
            if get_id in data.keys():
                print('Содержание заметки: ', data[get_id][1])
                data[get_id][1] = get_text()
                data[get_id][2] = datetime.now().strftime("%Y-%m-%d")
            else:
                print('Такой ID не существует')    

        elif get == '5':
            if data == {}:
                print ('Нет заметок')
            else:
                print_notes_book(data)

        elif get == '6':
            date = get_date()
            found = False
            for note in data.values():
                if note[2] == date:
                    print_note(note)
                    found = True
            if not found:    
                print('Некорректный ввод данных или нет такой даты')
        else:
            print('Некорректный ввод данных, введите ещё раз: ')
            print_prompt = False


def create(data: dict, id: int, elem: list) -> dict:  # add new note
    data[id] = elem
    return data


def print_notes_book(data: dict) -> None:
    for key, value in data.items():
        print(f"\nID - {key}")
        print_note(value)

def get_data() -> list:  # ask user data
    note_title = input('Введите заголовок заметки: ')
    note_text = input('Введите текст заметки: ')
    note_time = datetime.now().strftime("%Y-%m-%d")
    return [note_title, note_text, note_time]


def get_date():  # ask user date
    user_date = input('Введите дату заметки (в формате "YYYY-mm-dd"): ')
    return (user_date)


def get_text() -> list:  # ask user new text
    note_text = input('Введите новый текст заметки: ')
    return (note_text)

def print_note(note: list):
    print(f'Note "{note[0]}" from {note[2]}')
    print('----------')
    print(note[1])
    print('----------')


json_file_path = 'notes.json'

if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as file:
        notes_book = json.load(file)
else:
    notes_book = {}

id_note = int(sorted(notes_book.keys())[-1]) + 1

main_menu(notes_book, id_note)
