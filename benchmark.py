from prolog import prolog
import random

from guesswho import CHARACTERS, find_character

def compare_prolog_db(a, b, count = 10000):
    avg = [[],[]]
    g_sum =  [{},{}]
    app_sum = {}

    for char in CHARACTERS:
        g_sum[0][char] = 0
        g_sum[1][char] = 0
        app_sum[char] = 0

    for i in range(count):

        r_char = random.choice(CHARACTERS)
        app_sum[r_char] += 1

        prolog.consult(a)
        char, question_count = find_character(r_char)
        avg[0].append(question_count)

        g_sum[0][char] += question_count

        prolog.consult(b)
        char, question_count = find_character(r_char)
        avg[1].append(question_count)

        g_sum[1][char] += question_count
        print(i)


    a = sum(avg[0]) / count
    b = sum(avg[1]) / count

    print(a)
    print(b)

    print((b) / (a))

    print(g_sum[0])
    print(g_sum[1])

    diff_avg = 0
    diff_wgt_avg = 0

    for name in g_sum[0].keys():
        if app_sum[name] == 0:
            continue
        diff = g_sum[1][name] - g_sum[0][name]
        print(f"{name}: {diff} {(diff) / app_sum[name]}")
        diff_avg += diff
        diff_wgt_avg += (diff) / app_sum[name]

    print(f"avg: {diff_avg / len(CHARACTERS)}")
    print(f"w_avg: {diff_wgt_avg / len(CHARACTERS)}")


def compare_funct(a, b, count = 10000):
    avg = [[],[]]
    g_sum =  [{},{}]
    app_sum = {}

    for char in CHARACTERS:
        g_sum[0][char] = 0
        g_sum[1][char] = 0
        app_sum[char] = 0

    for i in range(count):

        r_char = random.choice(CHARACTERS)
        app_sum[r_char] += 1

        char, question_count = find_character(r_char,a)
        avg[0].append(question_count)

        g_sum[0][char] += question_count

        char, question_count = find_character(r_char, b)
        avg[1].append(question_count)

        g_sum[1][char] += question_count
        print(i)


    a = sum(avg[0]) / count
    b = sum(avg[1]) / count

    print(a)
    print(b)

    print((b) / (a))

    print(g_sum[0])
    print(g_sum[1])

    diff_avg = 0
    diff_wgt_avg = 0

    for name in g_sum[0].keys():
        if app_sum[name] == 0:
            continue
        diff = g_sum[1][name] - g_sum[0][name]
        print(f"{name}: {diff} {(diff) / app_sum[name]}")
        diff_avg += diff
        diff_wgt_avg += (diff) / app_sum[name]

    print(f"avg: {diff_avg / len(CHARACTERS)}")
    print(f"w_avg: {diff_wgt_avg / len(CHARACTERS)}")
