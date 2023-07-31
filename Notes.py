import os.path
import colorama
from colorama import Fore, Style
import Methods as Methods




def main():
    colorama.init
    os.system("cls")
    if os.path.exists('data.json'):
        file_name = 'data.json'
        notes = Methods.read_notes_file(file_name)
    else:
        Methods.get_file()
        file_name = 'data.json'
        notes = Methods.read_notes_file(file_name)
    

    while True:
        print(Fore.YELLOW +'Выберите действие:')
        print('1. Вывести все заметки')
        print('2. Вывести заметки за определенную дату')
        print('3. Вывести конкретную заметку')
        print('4. Добавить новую заметку')
        print('5. Редактировать заметку')
        print('6. Удалить заметку')
        print('7. Выход')

        choice = input(Fore.WHITE +'Ваш выбор: ')

        if choice == '1':
            Methods.print_notes(notes)
        elif choice == '2':
            date_str = input('Введите дату в формате ГГГГ-ММ-ДД: ')
            filtered_notes = Methods.filter_notes_by_date(notes, date_str)
            Methods.print_notes(filtered_notes)
        elif choice == '3':
            id = int(input('Введите ID заметки: '))
            flag = False
            for note in notes:
                if note['id'] == id:
                    Methods.print_note(note)
                    flag = True
                    break
            if flag == False: print(Fore.RED + 'Заметка не найдена' + Style.RESET_ALL)
        elif choice == '4':
            notes = Methods.add_note(notes)
            Methods.save_notes_json(notes, file_name)
            print(Fore.GREEN + 'Заметка добавлена' + Style.RESET_ALL)
        elif choice == '5':
            id = int(input('Введите ID заметки для редактирования: '))
            notes = Methods.edit_note(notes, id)
            Methods.save_notes_json(notes, file_name)
        elif choice == '6':
            id = int(input('Введите ID заметки для удаления: '))
            notes = Methods.delete_note(notes, id)
            Methods.save_notes_json(notes, file_name)
        elif choice == '7':
            print(Style.RESET_ALL)
            os.system("cls")
            break
        else:
            print(Fore.RED + 'Недопустимый выбор' + Style.RESET_ALL)

if __name__ == '__main__':
    main()