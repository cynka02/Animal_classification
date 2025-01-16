from load_dataset import load_data
import tkinter as tk
from ctypes import windll


def place_input_box():
    input_box_border.place(relx=0.5, rely=0.54, anchor='center')
    input_box.pack()

    submit_button_border.place(relx=0.5, rely=0.66, anchor='center')
    submit_button.pack()

    place_forget((button1_border, button2_border))


def place_choice_buttons():
    button1_border.place(relx=0.44, rely=0.55, anchor='center')
    button1.pack()

    button2_border.place(relx=0.56, rely=0.55, anchor='center')
    button2.pack()

    place_forget((input_box_border, submit_button_border))


def place_play_again_button():
    play_again_button_border.place(relx=0.5, rely=0.72, anchor='center')
    play_again_button.pack()


def place_top_label():
    top_label.place(relx=0.5, rely=0.42, anchor='center')


def place_forget(elements):
    if type(elements) is tuple:
        for ele in elements:
            ele.place_forget()
    else:
        elements.place_forget()


def answer_set_legs(value):
    if value.isnumeric():
        answer.set(int(value))
        place_forget(error_label)
    else:
        error_label.place(relx=0.5, rely=0.75, anchor='center')
        input_box.delete(0, tk.END)


def find_nearest_to_50(dict):
    """
        Finds the most diverse column among animal features. The closer to 50%, the greater the differentiation

        Returns:
            str: column name that is the most diverse.
    """

    diff = {}
    for key in dict.keys():
        diff[key] = abs(0.5-dict[key])
    return min(diff, key=diff.get)


def ask_question(feature):
    if feature == 'predator':
        question_text.set('Is your animal a predator?')
    elif feature in ('aquatic', 'venomous', 'domestic', 'catsize', 'airborne', 'toothed'):
        question_text.set('Is your animal ' + feature + '?')
    elif feature in ('hair', 'feathers', 'backbone', 'fins', 'tail'):
        question_text.set('Does your animal have ' + feature + '?')
    elif feature == 'eggs':
        question_text.set('Does your animal lay eggs?')
    elif feature == 'milk':
        question_text.set('Does your animal can produce milk?')
    elif feature == 'breathes':
        question_text.set('Does your animal breathe?')
    elif feature == 'legs':
        question_text.set('How many legs does your animal have?')


def guessing_step(data):
    """
        Performs full quessing step:
            1. Calculates variety of all animal features.
            2. Sends question to user about most diverse feature.
            3. Filter data based on this answer.
    """

    variety = {}

    for column in data.columns:
        if column not in ('animal_name', 'legs'):
            variety[column] = sum(data[column]) / len(data)
        elif column == 'legs':
            variety[column] = data[column].value_counts(ascending=True).iloc[0] / len(data)

    feature = find_nearest_to_50(variety)
    ask_question(feature)

    if feature == 'legs':
        place_input_box()
        submit_button.wait_variable(answer)
        place_forget((input_box_border, submit_button_border))
    else:
        if button1_border.winfo_viewable():
            button1.wait_variable(answer)
        else:
            place_choice_buttons()
            button1.wait_variable(answer)

    data = data[data[feature] == answer.get()].drop(columns=feature)
    return data


def guess_animal():
    data = load_data()

    while len(data) > 1:
        data = guessing_step(data)

        if len(data.drop(columns='animal_name').drop_duplicates()) == 1 and len(data) != 1:
            place_forget((top_label, button1_border, button2_border, input_box_border, submit_button_border))
            final_label.config(text="I don't have enough data to continue this guessing,\n "
                                    "but probably you're thinking of one of these animals:\n\n" +
                                    ', '.join(data['animal_name'].tolist()))
            final_label.place(relx=0.5, rely=0.5, anchor='center')
            break

    if len(data) == 0:
        place_forget((top_label, button1_border, button2_border, input_box_border, submit_button_border))
        final_label.config(text="Sorry, I don't know what animal you're thinking of.", font=('Arial', 45, 'bold'))
        final_label.place(relx=0.5, rely=0.45, anchor='center')
    elif len(data) == 1:
        place_forget((top_label, button1_border, button2_border, input_box_border, submit_button_border))
        final_label.config(text='\nMy guess is: ' + data['animal_name'].iloc[0], font=('Arial', 60, 'bold'))
        final_label.place(relx=0.5, rely=0.45, anchor='center')

    place_play_again_button()


def start():
    place_forget((final_label, play_again_button_border))
    input_box.delete(0, tk.END)
    place_top_label()
    place_choice_buttons()
    guess_animal()


# Creating app

app = tk.Tk()
app.geometry('1920x1080')
app.title('Animal Guesser')
windll.shcore.SetProcessDpiAwareness(1)

start_var = tk.IntVar()
question_text = tk.StringVar()
answer = tk.IntVar()

# Creating all elements

button_start = tk.Button(app, text='Start Animal Guesser', command=lambda: start_var.set(1), font=('Arial', 70, 'bold'),
                         bg='black', fg='white', cursor='hand2', bd=0,
                         activebackground='black', activeforeground='white')

top_label = tk.Label(app, textvariable=question_text, font=('Arial', 65, 'bold'))

button1_border = tk.Frame(app, highlightbackground="black", highlightthickness=5, bd=0)
button2_border = tk.Frame(app, highlightbackground="black", highlightthickness=5, bd=0)

button1 = tk.Button(button1_border, text='Yes', command=lambda: answer.set(1), bg='white', fg='black', cursor='hand2',
                    font=('Arial', 40, 'bold'), bd=0, activebackground='white', activeforeground='black', width=5)
button2 = tk.Button(button2_border, text='No', command=lambda: answer.set(0), bg='black', fg='white', cursor='hand2',
                    font=('Arial', 40, 'bold'), bd=0, activebackground='black', activeforeground='white', width=5)

input_box_border = tk.Frame(app, highlightbackground="black", highlightthickness=3, bd=0)
input_box = tk.Entry(input_box_border, font=('Arial', 45, 'normal'), justify='center')

submit_button_border = tk.Frame(app, highlightbackground="black", highlightthickness=5, bd=0)
submit_button = tk.Button(submit_button_border, text='Submit', command=lambda: answer_set_legs(input_box.get()),
                          bg='black', fg='white', cursor='hand2', font=('Arial', 40, 'bold'), bd=0,
                          activebackground='black', activeforeground='white', width=7)

error_label = tk.Label(app, text='Legs count must be a natural number!', font=('Arial', 25, 'bold'), fg='red')

final_label = tk.Label(app, text='', font=('Arial', 35, 'bold'))

play_again_button_border = tk.Frame(app, highlightbackground="black", highlightthickness=5, bd=0)
play_again_button = tk.Button(play_again_button_border, text='Play again!', command=start,
                              bg='black', fg='white', cursor='hand2', font=('Arial', 40, 'bold'), bd=0,
                              activebackground='black', activeforeground='white', width=9)

# Starting guessing

button_start.place(relx=0.5, rely=0.5, anchor='center')
button_start.wait_variable(start_var)

button_start.destroy()

start()

app.mainloop()
