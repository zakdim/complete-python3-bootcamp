from PIL import Image


def s16_127():
    words = Image.open('word_matrix.png')
    print(type(words))
    print(words.size)
    w, h = words.size

    mask = Image.open('mask.png')
    print(type(mask))
    print(mask.size)

    mask = mask.resize((w, h))
    print(mask.size)
    mask.putalpha(128)
    # mask.show()

    words.paste(mask, (0, 0), mask)
    words.show()
    # words.save('puzzle_answer.png')


if __name__ == '__main__':
    s16_127()
