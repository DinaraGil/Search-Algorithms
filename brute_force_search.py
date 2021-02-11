def main(text, pattern):
    len_of_pattern = len(pattern)
    len_of_text = len(text)

    for i in range(0, len_of_text - len_of_pattern + 1):
        for j in range(0, len_of_pattern):
            if text[i + j] != pattern[j]:
                break

            if j == len_of_pattern - 1:
                return i


text = input()
pattern = input()

result = main(text, pattern)

if result is None:
    print('No such pattern')
else:
    print('Index =', result)