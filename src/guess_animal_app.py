from load_dataset import load_data
import tkinter as tk


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

    top_label.update_idletasks()


def guessing_step(app, data):
    """
        Performs full quessing step:
            1. Calculates variety of all animal features.
            2. Sends question to user about most diverse feature.
            3. Filter data based on this answer.
    """

    variety = {}
    global answer

    for column in data.columns:
        if column not in ('animal_name', 'legs'):
            variety[column] = sum(data[column]) / len(data)
        elif column == 'legs':
            variety[column] = data[column].value_counts(ascending=True).iloc[0] / len(data)

    feature = find_nearest_to_50(variety)
    ask_question(feature)

    if feature == 'legs':
        button1.pack_forget()
        button2.pack_forget()
        input_box = tk.Entry(app)
        input_box.pack()
        sub_btn = tk.Button(app, text='Submit', command=lambda: answer.set(int(input_box.get())))
        sub_btn.pack()
        sub_btn.wait_variable(answer)
        input_box.destroy()
        sub_btn.destroy()

    else:
        if button1.winfo_viewable() and button2.winfo_viewable():
            button1.wait_variable(answer)
        else:
            button1.pack()
            button2.pack()
            button1.wait_variable(answer)

    data = data[data[feature] == answer.get()].drop(columns=feature)
    return data


def guess_animal(app):
    data = load_data()

    while len(data) > 1:
        data = guessing_step(app, data)
        if len(data.drop(columns='animal_name').drop_duplicates()) == 1 and len(data) != 1:
            top_label.destroy()
            button1.destroy()
            button2.destroy()
            final_text = tk.Label(app, text="I don't have enough data to continue this guessing, "
                                            "but probably you're thinking of one of these animals:\n" +
                                            ', '.join(data['animal_name'].tolist()))
            final_text.pack()
            break

    if len(data) == 0:
        top_label.destroy()
        button1.destroy()
        button2.destroy()
        final_text = tk.Label(app, text="Sorry, I don't know what animal you're thinking of.")
        final_text.pack()
    elif len(data) == 1:
        top_label.destroy()
        button1.destroy()
        button2.destroy()
        final_text = tk.Label(app, text='\nMy guess is: ' + data['animal_name'].iloc[0])
        final_text.pack()


def get_random_animal():
    data = load_data()
    animal = data.sample()

    animal_name = animal['animal_name'].iloc[0]
    catsize = 'Yes' if animal['catsize'].iloc[0] == 1 else 'No'

    return 'Try me if I can guess the animal below!\n' + animal_name + ' (catsize - ' + catsize + ')\n\n'


app = tk.Tk()
app.state('zoomed')
app.title('Animal Guesser')

start = tk.IntVar()

button_start = tk.Button(app, text='Start app', command=lambda: start.set(1))
button_start.pack()
button_start.wait_variable(start)

button_start.destroy()

question_text = tk.StringVar()
top_label = tk.Label(app, textvariable=question_text)
top_label.pack()

button1 = tk.Button(app, text='Yes', command=lambda: answer.set(1))
button2 = tk.Button(app, text='No', command=lambda: answer.set(0))
button1.pack()
button2.pack()

answer = tk.IntVar()

guess_animal(app)

app.mainloop()
