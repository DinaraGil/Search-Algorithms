text = input()
pattern = input()

d = {}
len_of_pattern = len(pattern)
for i in range(len_of_pattern):
    d[pattern[i]] = len_of_pattern - i - 1

print(d)


def alg(text, pattern):
    step = 1
    for i in range(len(pattern) - 1, len(text), step):
        k = i
        for j in range(len(pattern) - 1, -1, -1):
            if text[k] == pattern[j]:
                if j == 0:
                    return k
                k -= 1
                continue

            elif text[i] in d:
                step += d[text[i]]
                break
            else:
                step += len(pattern)
                break


result = alg(text, pattern)

if result is None:
    print('No such pattern')
else:
    print(result)
