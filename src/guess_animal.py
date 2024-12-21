from load_dataset import load_data


def ask_question(data):
    return data


def guess_animal():
    data = load_data()
    while len(data) > 1:
        data = ask_question(data)
    return data['animal_name'][0]


def main():

    guess_animal()


if __name__ == '__main__':
    main()
