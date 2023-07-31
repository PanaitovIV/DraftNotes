import datetime
import json
import colorama
from colorama import Fore, Back, Style



def print_notes(notes):
    if not notes:
        print(Fore.RED + 'Заметок не найдено' + Style.RESET_ALL)
    for note in notes:
                print(f'ID: {note["id"]}')
                print(f'Заголовок: {note["title"]}')
                print(f'Тело заметки: {note["body"]}')
                print(f'Дата/время: {note["timestamp"]}')
                print(Fore.CYAN + '-------------------------------' + Style.RESET_ALL)


def print_note(note):
        print(f'ID: {note["id"]}')
        print(f'Заголовок: {note["title"]}')
        print(f'Тело заметки: {note["body"]}')
        print(f'Дата/время: {note["timestamp"]}')
        print(Fore.CYAN + '-------------------------------' + Style.RESET_ALL)

def read_notes_file(file_name):
    with open(file_name, 'r', encoding='utf8') as f:
        notes = json.load(f)
    return notes

def save_notes_json(notes, file_name):
    with open(file_name, 'w', encoding='utf8') as f:
        json.dump(notes, f, ensure_ascii=False)

def filter_notes_by_date(notes, date):
    filtered_notes = []
    for note in notes:
        if date in note['timestamp']:
            filtered_notes.append(note)
    return filtered_notes

def add_note(notes):
    id = len(notes) + 1
    title = input('Введите заголовок: ')
    body = input('Введите тело заметки: ')
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    notes.append({'id': id, 'title': title, 'body': body, 'timestamp': timestamp})
    return notes

def delete_note(notes, id):
    flag = False
    for note in notes:
        if note['id'] == id:
            notes.remove(note)
            flag = True
            break
    if flag == True: print(Fore.GREEN + 'Заметка удалена' + Style.RESET_ALL)
    else: print(Fore.RED + 'Заметка не найдена' + Style.RESET_ALL)
    return notes

def edit_note(notes, id):
    flag = False
    for note in notes:
        if note['id'] == id:
            new_title = input(f'Введите новый заголовок (было: {note["title"]}): ')
            new_body = input(f'Введите новое тело заметки (было: {note["body"]}): ')
            note['title'] = new_title
            note['body'] = new_body
            note['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            flag = True
            break
    if flag == True: print(Fore.GREEN + 'Заметка отредактирована' + Style.RESET_ALL)
    else: print(Fore.RED + 'Заметка не найдена' + Style.RESET_ALL)
    return notes

def get_file():
    id = 1
    title = 'Default title'
    body = 'Empty note'
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    default_file = [{'id': id, 'title': title, 'body': body, 'timestamp': timestamp}]
    save_notes_json(default_file, file_name='data.json')