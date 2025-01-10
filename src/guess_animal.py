from load_dataset import load_data


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
        return input('Is your animal a predator? (Yes/No)\n')
    elif feature in ('aquatic', 'venomous', 'domestic', 'catsize', 'airborne', 'toothed'):
        return input('Is your animal ' + feature + '? (Yes/No)\n')
    elif feature in ('hair', 'feathers', 'backbone', 'fins', 'tail'):
        return input('Does your animal have ' + feature + '? (Yes/No)\n')
    elif feature == 'eggs':
        return input('Does your animal lay eggs? (Yes/No)\n')
    elif feature == 'milk':
        return input('Does your animal can produce milk? (Yes/No)\n')
    elif feature == 'breathes':
        return input('Does your animal breathe? (Yes/No)\n')
    elif feature == 'legs':
        return input('How many legs does your animal have?\n')


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

    answer = ask_question(feature)
    if feature != 'legs':
        answer = 1 if answer == 'Yes' else 0

    data = data[data[feature] == int(answer)].drop(columns=feature)
    return data


def guess_animal():
    data = load_data()

    while len(data) > 1:
        data = guessing_step(data)
        if len(data.drop(columns='animal_name').drop_duplicates()) == 1 and len(data) != 1:
            return "I don't have enough data to continue this guessing, " \
                   "but probably you're thinking of one of these animals:\n" + ', '.join(data['animal_name'].tolist())

    if len(data) == 0:
        return "Sorry, I don't know what animal you're thinking of."
    else:
        return '\nMy guess is: ' + data['animal_name'].iloc[0]


def get_random_animal():
    data = load_data()
    animal = data.sample()

    animal_name = animal['animal_name'].iloc[0]
    catsize = 'Yes' if animal['catsize'].iloc[0] == 1 else 'No'

    return 'Try me if I can guess the animal below!\n' + animal_name + ' (catsize - ' + catsize + ')\n\n'


def main():

    print(get_random_animal())
    print(guess_animal())


if __name__ == '__main__':
    main()
