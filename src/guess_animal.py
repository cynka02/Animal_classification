from load_dataset import load_data


def find_nearest_to_50(dict):
    diff = {}
    for key in dict.keys():
        diff[key] = abs(0.5-dict[key])
    return min(diff, key=diff.get)


def ask_question(data):
    variety = {}
    for column in data.columns:
        if column not in ('animal_name', 'legs'):  # Legs should be added based on a different rules
            variety[column] = sum(data[column]) / len(data)
    feature = find_nearest_to_50(variety)
    answer = input('Is your animal a ' + feature + ' (Yes/No)?\n')  # Need to add more types of questions
    answer = 1 if answer == 'Yes' else 0
    data = data[data[feature] == answer].drop(columns=feature)
    return data


def guess_animal():
    data = load_data()
    while len(data) > 1:  # Also should stop when length of data didn't change after last iteration
        data = ask_question(data)
    if len(data) == 0:
        return "I don't know about such animal"
    # Add elif len(data) > 0
    return data['animal_name']


def main():

    print(guess_animal())


if __name__ == '__main__':
    main()
