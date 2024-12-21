from load_dataset import load_data


def find_nearest_to_50(dict):
    diff = {}
    for key in dict.keys():
        diff[key] = abs(0.5-dict[key])
    return min(diff, key=diff.get)


def ask_question(data):
    variety = {}
    for column in data.columns:
        if column not in ('animal_name', 'legs'):
            variety[column] = sum(data[column]) / len(data)
    feature = find_nearest_to_50(variety)
    answer = input('Is your animal a ' + feature + ' (Yes/No)?\n')
    answer = 1 if answer == 'Yes' else 0
    data = data[data[feature] == answer].drop(columns=feature)
    print(data)
    return data


def guess_animal():
    data = load_data()
    while len(data) > 1:
        data = ask_question(data)
    if len(data) == 0:
        return "I don't know about such animal"
    return data['animal_name']


def main():

    print(guess_animal())


if __name__ == '__main__':
    main()
