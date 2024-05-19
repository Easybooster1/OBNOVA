import tkinter as tk
from tkinter import messagebox
import requests

morse_code = {
    'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ё': '.', 'Ж': '...-', 'З': '--..',
    'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.',
    'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.',
    'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--',
    'Я': '.-.-', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    '!': '-.-.--', '-': '-....-', '/': '-..-.', '(': '-.--.', ')': '-.--.-', ' ': '/'
}


class App:
    def __init__(self, master):
        self.window = master
        self.window.title("Escoria")
        self.version = "2.0"

        self.input_label = tk.Label(self.window, text="Введите текст:")
        self.input_label.pack()

        self.input_text = tk.Text(self.window, height=5, width=30)
        self.input_text.pack()

        self.encrypt_button = tk.Button(self.window, text="Зашифровать", command=self.encrypt_text)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(self.window, text="Расшифровать", command=self.decrypt_text)
        self.decrypt_button.pack()

        self.output_label = tk.Label(self.window, text="Результат:")
        self.output_label.pack()

        self.output_text = tk.Text(self.window, height=5, width=30)
        self.output_text.pack()

        self.copy_button = tk.Button(self.window, text="Скопировать", command=self.copy_to_clipboard, bg="red")  # Красная кнопка
        self.copy_button.pack()

        self.about_button = tk.Button(self.window, text="О программе", command=self.show_about, bg="green")  # Зеленая кнопка
        self.about_button.pack()

        self.create_menu()

    def encrypt_text(self):
        text = self.input_text.get("2.0", tk.END).upper().strip()
        encrypted_text = ''
        for char in text:
            if char in morse_code:
                encrypted_text += morse_code[char] + ' '
        if encrypted_text:
            self.output_text.delete("2.0", tk.END)
            self.output_text.insert(tk.END, encrypted_text)
        else:
            messagebox.showinfo("Ошибка", "Некорректный ввод")

    def decrypt_text(self):
        text = self.input_text.get("2.0", tk.END).strip()
        decrypted_text = ''
        morse_code_reverse = {value: key for key, value in morse_code.items()}
        words = text.split(' / ')
        for word in words:
            chars = word.split(' ')
            for char in chars:
                if char in morse_code_reverse:
                    decrypted_text += morse_code_reverse[char]
            decrypted_text += ' '
        if decrypted_text:
            self.output_text.delete("2.0", tk.END)
            self.output_text.insert(tk.END, decrypted_text)
        else:
            messagebox.showinfo("Ошибка", "Некорректный ввод")

    def copy_to_clipboard(self):
        text = self.output_text.get("2.0", tk.END).strip()
        if text:
            self.window.clipboard_clear()
            self.window.clipboard_append(text)
            messagebox.showinfo("Успешно", "Результат скопирован в буфер обмена!")
        else:
            messagebox.showinfo("Ошибка", "Нет текста для копирования.")

    def download_update(self):
        try:
            response = requests.get('https://raw.githubusercontent.com/Easybooster1/OBNOVA/main/dfsfs.py')
            with open('dfsfs.py', 'wb') as f:
                f.write(response.content)
            messagebox.showinfo("Обновление Escoria", "Обновление прошло успешно")

        except requests.RequestException as e:
            messagebox.showerror("Ошибка", f"Ошибочка: {e}")

    def check_update(self):
        try:
            response = requests.get('https://raw.githubusercontent.com/Easybooster1/OBNOVA/main/version.txt')
            if self.version == response.text:
                messagebox.showinfo("Обновление ПО", "Программа не требует обновления")
                return
            else:
                user_input = messagebox.askquestion("Обновление ПО", "Обнаружено обновление. Хотите обновить программу?")
                if user_input == "yes":
                    self.download_update()
        except requests.RequestException as e:
            messagebox.showerror("Ошибка", f"Не удалось проверить обновления: {e}")

    def create_menu(self):
        self.menu_bar = tk.Menu(self.window)
        self.window.config(menu=self.menu_bar)
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Обновление", menu=self.help_menu)
        self.help_menu.add_command(label="Проверить обновления", command=self.check_update)

    def show_about(self):
        messagebox.showinfo("О программе", "Escoria\nРазработчик:  [Буката Виталий ИСП330]\nВерсия: " + self.version)

root = tk.Tk()
app = App(root)
root.mainloop()
