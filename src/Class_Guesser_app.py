import json
import importlib
import pandas as pd
from utils import get_repo_path
from config import OUTPUT_FILE_PATH
from config import PATH_TO_CLASS_DATASET
from load_dataset import load_data
import tkinter as tk
from ctypes import windll


data = load_data()
classes = pd.read_csv(get_repo_path() / PATH_TO_CLASS_DATASET)


def get_best_model_name():
    with open(get_repo_path() / OUTPUT_FILE_PATH) as f:
        models_accuracy = json.load(f)
    return max(models_accuracy, key=models_accuracy.get)


def create_model(name):
    func_name = 'get_model_' + name.lower().replace(' ', '_')
    module_name = 'models.' + name.replace(' ', '')
    module = importlib.import_module(module_name)
    model = getattr(module, func_name)
    return model()


def predict_class(model, animal):
    data_to_predict = data[data['animal_name'] == animal].drop(columns=['class_type', 'animal_name'])
    predicted = int(model.predict(data_to_predict))
    return classes.loc[predicted-1, 'Class_Type']


def get_class(animal):
    class_number = data[data['animal_name'] == animal]['class_type'].iloc[0]
    return classes.loc[class_number-1, 'Class_Type']


def check_animal_exist(animal):
    return animal in data['animal_name'].values


def start():
    input_box_border.place(relx=0.5, rely=0.25, anchor='center')
    input_box.pack()
    submit_button_border.place(relx=0.5, rely=0.36, anchor='center')
    submit_button.pack()

    model = create_model(get_best_model_name())

    submit_button.wait_variable(animal_var)
    guess_animal(model)


def guess_animal(model):
    input_box.delete(0, tk.END)
    error_label.place_forget()

    if check_animal_exist(animal_var.get().lower()):
        animal_class = get_class(animal_var.get().lower())
        predicted_class = predict_class(model, animal_var.get().lower())

        animal_label.config(text='Animal: ' + animal_var.get().title())
        animal_label.place(relx=0.5, rely=0.5, anchor='center')

        guess_label1.config(text='From dataset it is: ' + animal_class)
        guess_label1.place(relx=0.5, rely=0.6, anchor='center')
        guess_label2.config(text='My predict is: ' + predicted_class)
        guess_label2.place(relx=0.5, rely=0.67, anchor='center')

        submit_button.wait_variable(animal_var)
        guess_animal(model)
    else:
        error_label.place(relx=0.5, rely=0.43, anchor='center')
        submit_button.wait_variable(animal_var)
        guess_animal(model)


app = tk.Tk()
app.geometry('1920x1080')
app.title('Class Guesser')
windll.shcore.SetProcessDpiAwareness(1)

start_var = tk.IntVar()
animal_var = tk.StringVar()

button_start = tk.Button(app, text='Start Class Guesser', command=lambda: start_var.set(1), font=('Arial', 70, 'bold'),
                         bg='black', fg='white', cursor='hand2', bd=0,
                         activebackground='black', activeforeground='white')

animal_label = tk.Label(app, font=('Arial', 47, 'bold'))

input_box_border = tk.Frame(app, highlightbackground="black", highlightthickness=3, bd=0)
input_box = tk.Entry(input_box_border, font=('Arial', 45, 'normal'), justify='center')

submit_button_border = tk.Frame(app, highlightbackground="black", highlightthickness=5, bd=0)
submit_button = tk.Button(submit_button_border, text='Submit', command=lambda: animal_var.set(input_box.get()),
                          bg='black', fg='white', cursor='hand2', font=('Arial', 37, 'bold'), bd=0,
                          activebackground='black', activeforeground='white', width=7)

error_label = tk.Label(app, text='Please type correct animal name!', font=('Arial', 25, 'bold'), fg='red')

guess_label1 = tk.Label(app, text='', font=('Arial', 40, 'bold'))
guess_label2 = tk.Label(app, text='', font=('Arial', 40, 'bold'))

# Starting guessing

button_start.place(relx=0.5, rely=0.5, anchor='center')
button_start.wait_variable(start_var)
button_start.destroy()

start()

app.mainloop()
