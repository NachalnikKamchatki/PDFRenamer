import os


def is_correct_filename(name: str, forbidden):
    for c in name:
        if c in forbidden:
            return False
    return True


def make_correct(filename: str, forbidden: list):
    if is_correct_filename(filename, forbidden):
        return filename
    else:
        for elem in forbidden:
            if elem in filename:
                filename = filename.replace(elem, '_')
    return filename


def main():
    forbidden = ['/', '\\', ':', '*', '?', '"', '>', '<', '|', '+', '%', '!', '@']
    incorrect_filename = 'asd:gh/skkrd|'
    print(is_correct_filename(incorrect_filename, forbidden))
    correct_fn = make_correct(incorrect_filename, forbidden)
    print(correct_fn)


if __name__ == '__main__':
    main()
