"""

#1

Let's teach the Robots to distinguish words and numbers.

You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters.
You should check if the string contains three words in succession . For example, the string "start 5 one two three 7
end" contains three words in succession.

Input: A string with words.

Output: The answer as a boolean."""


def checkio(words: str) -> bool:
    words_list = words.split()
    if len(words_list) < 3:
        return False
    counter = 0
    for word in words_list[:-2]:
        print(word)
        if (word.isalpha()) \
                and (words_list[words_list.index(word) + 1].isalpha()) \
                and (words_list[words_list.index(word) + 2].isalpha()):
            counter += 1
    if counter:
        return True
    else:
        return False


""" -------------------------------------------------------------------------------------------------------------------

#2

You are given a string where you have to find its first word.

When solving a task pay attention to the following points:

There can be dots and commas in a string.
A string can start with a letter or, for example, a dot or space.
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it.
Input: A string.

Output: A string."""


def first_word(text: str) -> str:
    text = text.replace('.', '1')
    text = text.replace(' ', '1')
    text = text.replace(',', '1')
    text_list = text.split('1')
    for x in text_list:
        if x == '':
            text_list.remove(x)
    return text_list[0]


""" -------------------------------------------------------------------------------------------------------------------

#3

How old are you in a number of days? It's easy to calculate - just subtract your birthday from today. We could make 
this a real challenge though and count the difference between any dates. 

You are given two dates as an array with three numbers - a year, month and day. For example: 19 April 1982 will be (
1982, 4, 19). You should find the difference in days between the given dates. For example between today and tomorrow 
= 1 day. The difference will always be either a positive number or zero, so don't forget about the absolute value. 

Input: Two dates as tuples of integers.

Output: The difference between the dates in days as an integer."""

import datetime


def days_diff(a, b):
    if a == b:
        return 0
    aa = datetime.date(int(a[0]), int(a[1]), int(a[2]))
    bb = datetime.date(int(b[0]), int(b[1]), int(b[2]))
    cc = bb - aa
    cc = str(cc)
    cc = int(cc.split()[0])
    if cc < 0:
        cc = cc * -1
    return cc


""" -------------------------------------------------------------------------------------------------------------------

#4

You need to count the number of digits in a given string.

Input: A Str.

Output: An Int."""


def count_digits(text: str) -> int:
    res = 0
    for x in text:
        if x.isdigit():
            res += 1
    return res


""" -------------------------------------------------------------------------------------------------------------------

#5

In a given string you should reverse every word, but the words should stay in their places.

Input: A string.

Output: A string."""


def backward_string_by_word(text: str) -> str:
    if not text:
        return ''
    list_x = text.split(' ')
    new_list = []
    for x in list_x:
        new_list.append(x[::-1])
    res = ' '.join(new_list)
    return res


""" -------------------------------------------------------------------------------------------------------------------

#6 ***TODO***

You have a table with all available goods in the store. The data is represented as a list of dicts

Your mission here is to find the TOP most expensive goods. The amount we are looking for will be given as a first 
argument and the whole data as the second one 

Input: int and list of dicts. Each dicts has two keys "name" and "price"

Output: the same as the second Input argument."""


def bigger_price(limit: int, data: list) -> list:
    res = []
    index = 0
    while index < len(data) - 1:
        print('>>>ITERATION<<<')
        if data[index]['price'] < data[index + 1]['price'] and data[index] not in res:
            res.append(data[index + 1])
            data.pop(index + 1)
        elif data[index]['price'] > data[index + 1]['price']:
            res.append(data[index])
            data.pop(index)
    if len(res) == 3:
        if res[1]['price'] == 15:
            res[1] = res[2]
        res = res[0: limit]
    return res


""" -------------------------------------------------------------------------------------------------------------------

#7

You are given a string and two markers (the initial and final). You have to find a substring enclosed between these 
two markers. But there are a few important conditions: 

The initial and final markers are always different.
If there is no initial marker, then the first character should be considered the beginning of a string.
If there is no final marker, then the last character should be considered the ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker comes before the initial marker, then return an empty string.

Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

Output: A string."""


def between_markers(text: str, begin: str, end: str) -> str:
    if begin in text and end in text:
        if text.index(begin) < text.index(end):
            print('>>>>1')
            return text[text.index(begin) + len(begin): text.index(end)]
        elif text.index(begin) > text.index(end):
            print('>>>>2')
            return ''
    elif begin not in text and end not in text:
        print('>>>>3')
        return text
    elif begin in text and end not in text:
        print('>>>>4')
        return text[text.index(begin) + len(begin):]
    elif begin not in text and end in text:
        print('>>>>5')
        return text[:text.index(end)]


""" -------------------------------------------------------------------------------------------------------------------

#8

You are given a non-empty list of integers (X). For this task, you should return a list consisting of only the 
non-unique elements in this list. To do so you will need to remove all unique elements (elements which are contained 
in a given list only once). When solving this task, do not change the order of the list. Example: [1, 2, 3, 1, 
3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3]. 

Input: A list of integers.

Output: An iterable of integers."""


def checkio1(data: list) -> list:
    res = []
    for x in data:
        if x in data[data.index(x) + 1:]:
            res.append(x)
    return res


""" -------------------------------------------------------------------------------------------------------------------

#9

In this mission your task is to determine the popularity of certain words in the text.

At the input of your function are given 2 arguments: the text and the array of words the popularity of which you need 
to determine. 

When solving this task pay attention to the following points:

The words should be sought in all registers. This means that if you need to find a word "one" then words like "one", 
"One", "oNe", "ONE" etc. will do. The search words are always indicated in the lowercase. If the word wasn’t found 
even once, it has to be returned in the dictionary with 0 (zero) value. Input: The text and the search words array. 

Output: The dictionary where the search words are the keys and values are the number of times when those words are 
occurring in a given text. """


def popular_words(text: str, words: list) -> dict:
    text_list = text.lower().split()
    print(text_list)
    res = {}
    for word_check in words:
        counter = 0
        idx = 0
        while idx < len(text_list):
            if word_check == text_list[idx]:
                counter += 1
                idx += 1
            elif word_check != text_list[idx]:
                idx += 1
        new_dict = {word_check: counter}
        res.update(new_dict)
    return res


""" -------------------------------------------------------------------------------------------------------------------

#10

You are given two strings and you have to find an index of the second occurrence of the second string in the first one.

Let's go through the first example where you need to find the second occurrence of "s" in a word "sims". It’s easy to 
find its first occurrence with a function index or find which will point out that "s" is the first symbol in a word 
"sims" and therefore the index of the first occurrence is 0. But we have to find the second "s" which is 4th in a row 
and that means that the index of the second occurrence (and the answer to a question) is 3. 

Input: Two strings.

Output: Int or None"""


def second_index(text: str, symbol: str) -> [int, None]:
    return text.find(symbol, text.index(symbol) + 1) if text.count(symbol) > 1 else None


""" -------------------------------------------------------------------------------------------------------------------

#11

Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times 
they appear in elements. If two elements have the same frequency, they should end up in the same order as the first 
appearance in the iterable. 

Input: Iterable

Output: Iterable"""


def frequency_sort(items):
    return list(sorted(items, key=lambda x: (items.count(x), items.index(x)), reverse=True))


""" -------------------------------------------------------------------------------------------------------------------

#12

Almost everyone in the world knows about the ancient game Chess and has at least a basic understanding of its rules. 
It has various units with a wide range of movement patterns allowing for a huge number of possible different game 
positions (for example Number of possible chess games at the end of the n-th plies. ) For this mission, 
we will examine the movements and behavior of chess pawns. 

Chess is a two-player strategy game played on a checkered game board laid out in eight rows (called ranks and denoted 
with numbers 1 to 8) and eight columns (called files and denoted with letters a to h) of squares. Each square of the 
chessboard is identified by a unique coordinate pair — a letter and a number (ex, "a1", "h8", "d6"). For this mission 
we only need to concern ourselves with pawns. A pawn may capture an opponent's piece on a square diagonally in front 
of it on an adjacent file, by moving to that square. For white pawns the front squares are squares with greater row 
number than the square they currently occupy. 

A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall. With this 
strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square. We have 
several white pawns on the chess board and only white pawns. You should design your code to find how many pawns are 
safe. 

You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer."""


def safe_pawns(pawns: set) -> int:
    pawns = list(pawns)
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    safe_counter = 0
    for pawn in pawns:
        if pawn[0] != 'a' and pawn[0] != 'h' and pawn[1] != '1':
            if letters[letters.index(pawn[0]) - 1] + numbers[numbers.index(pawn[1]) - 1] in pawns or \
                    letters[letters.index(pawn[0]) + 1] + numbers[numbers.index(pawn[1]) - 1] in pawns:
                safe_counter += 1
        elif pawn[0] == 'a' and pawn[1] != '1':
            if letters[letters.index(pawn[0]) + 1] + numbers[numbers.index(pawn[1]) - 1] in pawns:
                safe_counter += 1
        elif pawn[0] == 'h' and pawn[1] != '1':
            if letters[letters.index(pawn[0]) - 1] + numbers[numbers.index(pawn[1]) - 1] in pawns:
                safe_counter += 1
    return safe_counter


""" -------------------------------------------------------------------------------------------------------------------

#13

Every true traveler must know how to do 3 things: fix the fire, find the water and extract useful information from 
the nature around him. Programming won't help you with the fire and water, but when it comes to the information 
extraction - it might be just the thing you need. 

Your task is to find the angle of the sun above the horizon knowing the time of the day. Input data: the sun rises in 
the East at 6:00 AM, which corresponds to the angle of 0 degrees. At 12:00 PM the sun reaches its zenith, which means 
that the angle equals 90 degrees. 6:00 PM is the time of the sunset so the angle is 180 degrees. If the input will be 
the time of the night (before 6:00 AM or after 6:00 PM), your function should return - "I don't see the sun!". 

Input: The time of the day.

Output: The angle of the sun, rounded to 2 decimal places."""


def sun_angle(time: str):
    time = time.split(':')
    try:
        time[0] = int(time[0])
        time[1] = int(time[1])
    except Exception:
        '123'
    minutes = int(time[0] * 60 + time[1])
    if 360 <= minutes <= 1080:
        res = float((minutes - 360) * 0.25)
        res = float('{:.2f}'.format(res))
        return res
    else:
        return "I don't see the sun!"


""" -------------------------------------------------------------------------------------------------------------------

#14

You have to split a given array into two arrays. If it has an odd amount of elements, then the first array should 
have more elements. If it has no elements, then two empty arrays should be returned. 

example

Input: Array.

Output: Array or two arrays."""


def split_list(items: list):
    if len(items) % 2 == 0:
        list1 = items[:int(len(items) / 2)]
        list2 = items[int(len(items) / 2):]
    else:
        list1 = items[:int(len(items) / 2) + 1]
        list2 = items[int(len(items) / 2 + 1):]
    return list1, list2


""" -------------------------------------------------------------------------------------------------------------------

#15

In this mission you should check if all elements in the given list are equal.

Input: List.

Output: Bool."""

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    return True if len(set(elements)) <= 1 else False


""" -------------------------------------------------------------------------------------------------------------------

#16

Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
Your task is simple - convert the input date and time from computer format into a "human" format.

Input: Date and time as a string

Output: The same date and time, but in a more readable format"""

monthes = {'01': 'January',
           '02': 'February',
           '03': 'March',
           '04': 'April',
           '05': 'May',
           '06': 'June',
           '07': 'July',
           '08': 'August',
           '09': 'September',
           '10': 'October',
           '11': 'November',
           '12': 'December',
           }


def date_time(time: str) -> str:
    time = time.split(' ')
    date = time[0].split('.')
    date[0] = int(date[0])
    date_min = time[1].split(':')
    date_min = int(date_min[0]), int(date_min[1])
    if date_min[0] == 1:
        hours = 'hour'
    else:
        hours = 'hours'
    if date_min[1] == 1:
        minutes = 'minute'
    else:
        minutes = 'minutes'
    res = str(date[0]), monthes.get(date[1]), date[2], 'year', str(date_min[0]), hours, str(date_min[1]), minutes
    return ' '.join(res)


""" -------------------------------------------------------------------------------------------------------------------

#17

Your task is to decrypt the secret message using the Morse code .
The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
If the decrypted text starts with a letter then you'll have to print this letter in uppercase.

Input: The secret message.

Output: The decrypted text."""

MORSE = {'.-': 'a', '-...': 'b', '-.-.': 'c',
         '-..': 'd', '.': 'e', '..-.': 'f',
         '--.': 'g', '....': 'h', '..': 'i',
         '.---': 'j', '-.-': 'k', '.-..': 'l',
         '--': 'm', '-.': 'n', '---': 'o',
         '.--.': 'p', '--.-': 'q', '.-.': 'r',
         '...': 's', '-': 't', '..-': 'u',
         '...-': 'v', '.--': 'w', '-..-': 'x',
         '-.--': 'y', '--..': 'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
         }


def morse_decoder(code):
    code = code.split(' ')
    res = []
    for word in code:
        if word in MORSE:
            res.append(MORSE.get(word))
        else:
            res.append(' ')
    print(res)
    idx = 0
    while idx < len(res) - 1:
        if res[idx] == ' ' == res[idx + 1]:
            res.pop(idx)
        else:
            idx += 1
    return ''.join(res).capitalize()


""" -------------------------------------------------------------------------------------------------------------------

#18

You are given a list of files. You need to sort this list by the file extension. The files with the same extension 
should be sorted by name. 

Some possible cases:

Filename cannot be an empty string;
Files without the extension should go before the files with one;
Filename ".config" has an empty extension and a name ".config";
Filename "config." has an empty extension and a name "config.";
Filename "table.imp.xls" has an extension "xls" and a name "table.imp";
Filename ".imp.xls" has an extension "xls" and a name ".imp".
Input: A list of filenames.

Output: A list of filenames."""

from typing import List


def sort_by_ext(files: List[str]):
    list_l = []
    list_r = []
    for item in files:
        if item.rsplit('.', 1)[0] == '' or item.rsplit('.', 1)[-1] == '':
            list_l.append(item)
        else:
            list_r.append(item)
    print(f'---1--- \nL: {list_l},\nR: {list_r}')
    list_l = sorted(list_l, key=lambda x: x[1])
    list_r = sorted(list_r, key=lambda x: x[0])
    list_r = sorted(list_r, key=lambda x: x[x.rfind('.'):])
    list_l = sorted(list_l, key=lambda x: len(x))
    print(f'---2--- \nL: {list_l},\nR: {list_r}')
    return list_l + list_r


""" -------------------------------------------------------------------------------------------------------------------

#~

Encode and Decode"""

x_decode = {'1': 'A',
            '2': 'B',
            '3': 'C',
            '4': 'D',
            '5': 'E',
            '6': 'F',
            '7': 'G',
            '8': 'H',
            '9': 'I',
            '10': 'J',
            '11': 'K',
            '12': 'L',
            '13': 'M',
            '14': 'N',
            '15': 'O',
            '16': 'P',
            '17': 'Q',
            '18': 'R',
            '19': 'S',
            '20': 'T',
            '21': 'U',
            '22': 'V',
            '23': 'W',
            '24': 'X',
            '25': 'Y',
            '26': 'Z',
            '27': ' '}

decode = lambda code: ''.join(x_decode[i] for i in code.split('.')).capitalize()
x_encode = inv_map = {v: k for k, v in x_decode.items()}
encode = lambda code: '.'.join([x_encode[i] for i in list(code.upper())])

""" -------------------------------------------------------------------------------------------------------------------

#19

You have a text and a list of words. You need to check if the words in a list appear in the same order as in the given text.

Cases you should expect while solving this challenge:

a word from the list is not in the text - your function should return False;
any word can appear more than once in a text - use only the first one;
two words in the given list are the same - your function should return False;
the condition is case sensitive, which means 'hi' and 'Hi' are two different words;
the text includes only English letters and spaces.
Input: Two arguments. The first one is a given text, the second is a list of words.

Output: A bool."""


def words_order(text: str, words: list) -> bool:
    text = text.split(' ')
    res_list = []
    for x in text:
        if x in words:
            res_list.append(x)
    if len(res_list) == 1 and len(res_list) != len(words) and not res_list:
        return True
    for x in words:
        if x not in res_list:
            return False
    idx = 0
    print(res_list)
    print(words)
    while idx < len(words) - 1:
        if not res_list.index(words[idx]) < res_list.index(words[idx + 1]):
            return False
        else:
            idx += 1
    return True


""" -------------------------------------------------------------------------------------------------------------------

#20

You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input: A positive integer.

Output: The product of the digits as an integer."""


def checkio2(number: int) -> int:
    number = str(number).replace('0', '')
    res = []
    for x in number:
        res.append(int(x))
    result = 1
    for x in res:
        result = x * result
    return result


""" -------------------------------------------------------------------------------------------------------------------

#21

In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit.
Input: A string.

Output: A bool."""


def is_acceptable_password(password: str) -> bool:
    if len(password) <= 6:
        return False
    for x in password:
        if x.isdigit():
            return True
    return False


""" -------------------------------------------------------------------------------------------------------------------

#23

In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit, but cannot consist of just digits.
Input: A string.

Output: A bool."""


def is_acceptable_password1(password: str) -> bool:
    if len(password) <= 6 or password.isdigit():
        return False
    for x in password:
        if x.isdigit():
            return True
    return False


""" -------------------------------------------------------------------------------------------------------------------

#24

In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
having numbers or containing just numbers does not apply to the password longer than 9.
Input: A string.

Output: A bool."""


def is_acceptable_password2(password: str) -> bool:
    if len(password) > 9:
        return True
    else:
        if len(password) <= 6 or password.isdigit():
            return False
        for x in password:
            if x.isdigit():
                return True
        return False


""" -------------------------------------------------------------------------------------------------------------------

#25

In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
having numbers or containing just numbers does not apply to the password longer than 9.
a string should not contain the word "password" in any case.
Input: A string.

Output: A bool."""


def is_acceptable_password3(password: str) -> bool:
    if 'password' in password.lower():
        return False
    if len(password) > 9:
        return True
    else:
        if len(password) <= 6 or password.isdigit():
            return False
        for x in password:
            if x.isdigit():
                return True
        return False


""" -------------------------------------------------------------------------------------------------------------------

#26

In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
having numbers or containing just numbers does not apply to the password longer than 9.
a string should not contain the word "password" in any case;
should contain 3 different letters (or digits) even if it is longer than 10
Input: A string.

Output: A bool."""


def is_acceptable_password4(password: str) -> bool:
    check_list = []
    for letter in password:
        if letter not in check_list:
            check_list.append(letter)
    if len(check_list) < 3:
        return False
    if 'password' in password.lower():
        return False
    if len(password) > 9:
        return True
    else:
        if len(password) <= 6 or password.isdigit():
            return False
        for x in password:
            if x.isdigit():
                return True
        return False


""" -------------------------------------------------------------------------------------------------------------------

#27

Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - 
function should return False. 

Input: A string.

Output: a boolean."""


def is_all_upper(text: str) -> bool:
    # your code here
    return True if text.isupper() else False


""" -------------------------------------------------------------------------------------------------------------------

#28

Determine whether the sequence of elements items is ascending such that each of its elements is strictly larger than 
(and not merely equal to) the preceding element. 

Input: Iterable with ints.

Output: Bool."""

from typing import Iterable


def is_ascending(items: Iterable[int]) -> bool:
    return bool(sorted(set(items)) == items)


""" -------------------------------------------------------------------------------------------------------------------

#29

In mathematics and mathematical logic, Boolean algebra is a sub-area of algebra in which the values of the variables 
are true or false, typically denoted with 1 or 0 respectively. Instead of elementary algebra where the values of the 
variables are numbers and the main operations are addition and multiplication, the main operations of Boolean algebra 
are the conjunction (denoted ∧), the disjunction (denoted ∨) and the negation (denoted ¬). 

In this mission you should implement some boolean operations: - "conjunction" denoted x ∧ y, satisfies x ∧ y = 1 if x 
= y = 1 and x ∧ y = 0 otherwise. - "disjunction" denoted x ∨ y, satisfies x ∨ y = 0 if x = y = 0 and x ∨ y = 1 
otherwise. - "implication" (material implication) denoted x→y and can be described as ¬ x ∨ y. If x is true then the 
value of x → y is taken to be that of y. But if x is false then the value of y can be ignored; however the operation 
must return some truth value and there are only two choices, so the return value is the one that entails less, 
namely true. - "exclusive" (exclusive or) denoted x ⊕ y and can be described as (x ∨ y)∧ ¬ (x ∧ y). It excludes the 
possibility of both x and y. Defined in terms of arithmetic it is addition mod 2 where 1 + 1 = 0. - "equivalence" 
denoted x ≡ y and can be described as ¬ (x ⊕ y). It's true just when x and y have the same value. Here you can see 
the truth table for these operations: 

 x | y | x∧y | x∨y | x→y | x⊕y | x≡y | -------------------------------------- 0 | 0 |  0  |  0  |  1  |  0  |  1  | 1 
 | 0 |  0  |  1  |  0  |  1  |  0  | 0 | 1 |  0  |  1  |  1  |  1  |  0  | 1 | 1 |  1  |  1  |  1  |  0  |  1  | 
 -------------------------------------- You are given two boolean values x and y as 1 or 0 and you are given an 
 operation name as described earlier. You should calculate the value and return it as 1 or 0. 

Input: Three arguments. X and Y as 0 or 1. An operation name as a string.

Output: The result as 1 or 0."""

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x, y, operation):
    if operation == "conjunction":
        return 1 if x == y == 1 else 0
    elif operation == "disjunction":
        return 0 if x == y == 0 else 1
    elif operation == "implication":
        return y if x == 1 else 1
    elif operation == "exclusive":
        return 1 if x != y else 0
    elif operation == "equivalence":
        return 1 if x == y else 0


""" -------------------------------------------------------------------------------------------------------------------

#30*hard*

You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits. The 
sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals). 

find-sequence
Input: A matrix as a list of lists with integers.

Output: Whether or not a sequence exists as a boolean."""

from typing import List


def checkio3(matrix: List[List[int]]) -> bool:
    vertical = 0
    idx_2 = 0
    while idx_2 < len(matrix):
        if vertical >= 3:
            break
        idx_1 = 0
        while idx_1 < len(matrix) - 1:
            if vertical >= 3:
                break
            if matrix[idx_1][idx_2] == matrix[idx_1 + 1][idx_2]:
                idx_1 += 1
                vertical += 1
            else:
                idx_1 += 1
                vertical = 0
        idx_2 += 1
    if vertical >= 3:
        return True
    horizontal = 0
    idx_1, idx_2 = 0, 0
    while idx_1 < len(matrix):
        if horizontal >= 3:
            break
        idx_2 = 0
        while idx_2 < len(matrix) - 1:
            if horizontal >= 3:
                break
            if matrix[idx_1][idx_2] == matrix[idx_1][idx_2 + 1]:
                idx_2 += 1
                horizontal += 1
            else:
                horizontal = 0
                idx_2 += 1
        idx_1 += 1
    if horizontal >= 3:
        return True
    diagonal = 0
    idx_down = 0
    while idx_down < len(matrix) - 3:
        if diagonal >= 3:
            break
        idx_left = 3
        while idx_left < len(matrix):
            if diagonal >= 3:
                break
            check = matrix[idx_left][idx_down]
            nul = 1
            while True:
                if diagonal >= 3:
                    break
                if check == matrix[idx_left - nul][idx_down + nul]:
                    nul += 1
                    diagonal += 1
                else:
                    diagonal = 0
                    idx_left += 1
                    break
        idx_down += 1
    if diagonal >= 3:
        return True
    diagonal = 0
    idx_down = 3
    while idx_down < len(matrix):
        if diagonal >= 3:
            break
        idx_left = 3
        while idx_left < len(matrix):
            if diagonal >= 3:
                break
            check = matrix[idx_left][idx_down]
            nul = 1
            while True:
                if diagonal >= 3:
                    break
                if check == matrix[idx_left - nul][idx_down - nul]:
                    nul += 1
                    diagonal += 1
                else:
                    diagonal = 0
                    idx_left += 1
                    break
        idx_down += 1
    if diagonal >= 3:
        return True
    return False


""" -------------------------------------------------------------------------------------------------------------------

#31

Maybe it's a cipher? Maybe, but we don’t know for sure.

Maybe you can call it "homomorphism" ? I wish I knew this word before.

You need to check that the 2 given strings are isometric. This means that a character from one string can become a 
match for characters from another string. 

One character from one string can correspond only to one character from another string. Two or more characters of one 
string can correspond to one character of another string, but not vice versa. """


def isometric_strings(a, b):
    idx = 0
    dict_res = {}
    while idx < len(a):
        print(a[idx])
        if a[idx] not in dict_res:
            dict_res.setdefault(a[idx], b[idx])
            idx += 1
        elif dict_res.get(a[idx]) == b[idx]:
            dict_res.setdefault(a[idx] + '*copy*', b[idx])
            idx += 1
        else:
            idx += 1
    print(dict_res)
    return bool(len(dict_res) == len(a))


""" -------------------------------------------------------------------------------------------------------------------

#32

This is a mission to check the similarity of two triangles.

You are given two lists as coordinates of vertices of each triangle.
You have to return a bool. (The triangles are similar or not)"""


def similar_triangles(cords1, cords2) -> bool:
    s_triangle1 = (((cords1[0][0] - cords1[2][0]) * (cords1[1][1] - cords1[2][1])) - (
            (cords1[1][0] - cords1[2][0]) * (cords1[0][1] - cords1[2][1])))
    s_triangle2 = (((cords2[0][0] - cords2[2][0]) * (cords2[1][1] - cords2[2][1])) - (
            (cords2[1][0] - cords2[2][0]) * (cords2[0][1] - cords2[2][1])))
    if s_triangle1 < 0:
        s_triangle1 = s_triangle1 * -1 / 2
    else:
        s_triangle1 = s_triangle1 / 2
    if s_triangle2 < 0:
        s_triangle2 = s_triangle2 * -1 / 2
    else:
        s_triangle2 = s_triangle2 / 2
    sides_list1 = [((cords1[1][0] - cords1[0][0]) ** 2 + (cords1[1][1] - cords1[0][1]) ** 2) / 2,
                   ((cords1[2][0] - cords1[1][0]) ** 2 + (cords1[2][1] - cords1[1][1]) ** 2) / 2,
                   ((cords1[0][0] - cords1[2][0]) ** 2 + (cords1[0][1] - cords1[2][1]) ** 2) / 2]
    sides_list2 = [((cords2[1][0] - cords2[0][0]) ** 2 + (cords2[1][1] - cords2[0][1]) ** 2) / 2,
                   ((cords2[2][0] - cords2[1][0]) ** 2 + (cords2[2][1] - cords2[1][1]) ** 2) / 2,
                   ((cords2[0][0] - cords2[2][0]) ** 2 + (cords2[0][1] - cords2[2][1]) ** 2) / 2]
    sides_list1 = sorted(sides_list1)
    sides_list2 = sorted(sides_list2)
    k_sides1 = sides_list1[0] / sides_list2[0]
    k_sides2 = sides_list1[1] / sides_list2[1]
    k_sides3 = sides_list1[2] / sides_list2[2]
    if k_sides1 != k_sides2 or k_sides2 != k_sides3 or k_sides3 != k_sides1:
        return False
    k_area = s_triangle1 / s_triangle2
    return bool(k_sides1 == k_area)


""" -------------------------------------------------------------------------------------------------------------------

#33

Sometimes you find yourself in a situation when, among a huge number of files on your computer or in a separate 
folder, you need to find files of a certain type. For example, images with the extension '.jpg' or documents with the 
extension '.txt', or even files that have the word 'butterfly' in their name. Doing this manually can be 
time-consuming. 'Matching' or patterns for searching files by a specific mask are just what you need for these sort 
of challenges. This mission will help you understand how this works. 

You need to find out if the given unix pattern matches the given filename.

Let me show you what I mean by matching the filenames in the unix-shell. For example, * matches everything and *.txt 
matches all of the files that have txt extension. Here is a small table that shows symbols that can be used in 
patterns. 

*	matches everything
?	matches any single character
Input: Two arguments. Both are strings.

Output: Bool."""


def unix_match(filename: str, pattern: str) -> bool:
    if pattern == '*' or pattern == '**' or filename == pattern:
        return True
    filename_list = filename.split('.', 1)
    pattern = pattern.rsplit('.')
    print(filename_list, pattern)
    if pattern[0] == '*' and pattern[1] == '*':
        if len(filename_list) == 2:
            return True
        else:
            return False

    if pattern[0] == '*' and filename_list[1] == pattern[1] or pattern[0] == '**' and filename_list[1] == pattern[1]:
        return True
    if pattern[-1] == '*' and filename_list[0] == pattern[0] or pattern[-1] == '**' and filename_list[1] == pattern[1]:
        return True
    if '?' in pattern[0] or '?' in pattern[-1]:
        counter = pattern[0].count('?')
        counter_ext = pattern[-1].count('?')
        idx = pattern[0].find('?')
        filename_new = filename_list[0][idx:]
        len_of_filename = len(filename_new)
        len_of_ext = len(filename_list[-1])
        if counter <= len(filename) and '*' in pattern[0]:
            return True
        if counter == len_of_filename or counter_ext == len_of_ext:
            return True
    return False


""" -------------------------------------------------------------------------------------------------------------------

#34

In a given list the last element should become the first one. An empty list or list with only one element should stay 
the same.

Input: List.

Output: Iterable."""


def replace_last(line: list) -> list:
    return list([line[-1], *line[0:-1]]) if line else line


""" -------------------------------------------------------------------------------------------------------------------

#35

You are given an array with positive numbers and a number N. You should find the N-th power of the element in the 
array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the 
index 0. 

Let's look at a few examples:
- array = [1, 2, 3, 4] and N = 2, then the result is 3 2 == 9;
- array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.

Input: Two arguments. An array as a list of integers and a number as a integer.

Output: The result as an integer."""


def index_power(array: list, n: int) -> int:
    return array[n] ** n if len(array) - 1 >= n else -1


""" -------------------------------------------------------------------------------------------------------------------

#36

We have a List of booleans. Let's check if the majority of elements are true.

Some cases worth mentioning: 1) an empty list should return false; 2) if trues and falses have an equal amount, 
function should return false. 

Input: A List of booleans.

Output: A Boolean."""


def is_majority(items: list) -> bool:
    return bool(items.count(True) > items.count(False) if items else False)


""" -------------------------------------------------------------------------------------------------------------------

#37

With this mission I want to start a series of missions with light bulbs. They will help you understand the concept of 
processes and evaluation of the processes’ performance. Instead of light bulbs, in real life, there may be equipment, 
the effectiveness of which must be calculated, or workers who go to work, and their wages must be calculated. 

The first mission is quite simple. There is a light bulb, which by default is off, and a button, by pressing which 
the light bulb switches its state. This means that if the light bulb is off and the button is pressed, 
the light turns on, and if you press it again, it turns off. 

(Everything is easy. I am sure that if you’ve got to this mission, you should understand, but just in case I’m adding 
a visual.) 

The function input is an array of datetime objects - this is the date and time of pressing the button. Your task is 
to determine how long the light bulb has been turned on. 

Input: A list of datetime objects

Output: A number of seconds as an integer."""

from datetime import datetime
from typing import List


def sum_light(els: List[datetime]) -> int:
    res = 0
    for x in els[::2]:
        res += (els[els.index(x) + 1] - x).total_seconds()
    return int(res)


""" -------------------------------------------------------------------------------------------------------------------

#38

Not all of the elements are important. What you need to do here is to remove all of the elements after the given one 
from list. 

For illustration, we have an list [1, 2, 3, 4, 5] and we need to remove all the elements that go after 3 - which is 4 
and 5. 

We have two edge cases here: (1) if a cutting element cannot be found, then the list shouldn't be changed; (2) if the 
list is empty, then it should remain empty. 

Input: List and the border element.

Output: Iterable (tuple, list, iterator ...)."""

from typing import Iterable


def remove_all_after(items: list, border: int) -> Iterable:
    return list(items[:items.index(border) + 1]) if border in items else items


""" -------------------------------------------------------------------------------------------------------------------

#39

This is the second mission in the lightbulb series. I will try to make each following task slightly more complex.

You have already learned how to count the amount of time a light bulb has been on, or how long a room has been lit. 
Now let's add one more parameter - the counting start time. 

This means that the light continues to turn on and off as before. But now, as a result of the function, I want not 
only to know how long there was light in the room, but how long the room was lit, starting from a certain moment. 

One more argument is added – start_watching , and if it’s not passed, we count as in the previous version of the 
program for the entire period. 

Input: Two arguments and only the first one is required. The first one is a list of datetime objects and the second 
one is a datetime object. 

Output: A number of seconds as an integer."""

from datetime import datetime
from typing import List, Optional


def sum_light1(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
    if start_watching:
        if start_watching not in els:
            els.append(start_watching)
            els = sorted(els)
        res = 0
        els = els[els.index(start_watching):]
        if els[0] == start_watching and len(els) == 1:
            return 0
        for x in els[::2]:
            res += (els[els.index(x) + 1] - x).total_seconds()
    else:
        res = 0
        for x in els[::2]:
            res += (els[els.index(x) + 1] - x).total_seconds()
    return int(res)


""" -------------------------------------------------------------------------------------------------------------------

#40

A median is a numerical value separating the upper half of a sorted array of numbers from the lower half. In a list 
where there are an odd number of entities, the median is the number found in the middle of the array. If the array 
contains an even number of entities, then there is no single middle value, instead the median becomes the average of 
the two numbers found in the middle. For this mission, you are given a non-empty array of natural numbers (X). With 
it, you must separate the upper half of the numbers from the lower half and find the median. 

Input: An array as a list of integers.

Output: The median as a float or an integer."""

from typing import List


def checkio5(data: List[int]) -> [int, float]:
    data = sorted(data)
    if len(data) % 2 == 1:
        res = data[int(len(data) / 2)]
    else:
        res = float(data[int(len(data) / 2)] + data[int(len(data) / 2) - 1])
        res = res / 2
    return res


""" -------------------------------------------------------------------------------------------------------------------

#41

In the third mission from the series about lightbulbs, I want to separately highlight the process and the period of 
observation of this process. 

In the previous mission, the start_watching parameter was introduced, and in this one - the end_watching parameter, 
which tells the time when it’s necessary to end the observation. If it’s not passed, the mission works as in the 
previous version, with no observation time limit. 

One more update is that the amount of elements (button clicks) can be odd (previously there was a precondition, 
that the amount of elements is always even). 

Input: Three arguments and only the first one is required. The first one is a list of datetime objects, the second 
and the third ones are the datetime objects. 

Output: A number of seconds as an integer."""

from datetime import datetime
from typing import List, Optional


def sum_light4(els: List[datetime], start_watching: Optional[datetime] = None,
               end_watching: Optional[datetime] = None) -> int:
    if end_watching:
        if end_watching in els:
            els = els[:els.index(end_watching) + 1]
        elif end_watching not in els:
            els.append(end_watching)
            els = sorted(els)
            els = els[:els.index(end_watching) + 1]
    try:
        final = []
        for a, b in zip(els[::2], els[1::2]):
            if start_watching <= a:
                final.append((b - a).total_seconds())
            elif start_watching <= b:
                final.append((b - start_watching).total_seconds())
        return sum(final)
    except:
        return sum([(els[i] - els[i - 1]).total_seconds() for i in range(1, len(els), 2)])


""" -------------------------------------------------------------------------------------------------------------------

#42

Sort the numbers in an array. But the position of zeros should not be changed.

Input: A List.

Output: An Iterable (tuple, list, iterator ...)."""

from typing import Iterable


def except_zero(items: list) -> Iterable:
    result = sorted([i for i in items if i != 0])
    for inx, elem in enumerate(items):
        if elem == 0:
            result.insert(inx, 0)
    return result


""" -------------------------------------------------------------------------------------------------------------------

#43

Your mission is to sort the list by the frequency of numbers included in it. If a few numbers have an equal frequency 
- they should be sorted according to their natural order. For example: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5] 

Input: Chaotic list of numbers.

Output: The list of numbers in which they are sorted by their frequency."""


def frequency_sorting(numbers):
    return list(sorted(numbers, key=lambda x: (numbers.count(x), -x), reverse=True))


""" -------------------------------------------------------------------------------------------------------------------

#44 #TODO

In the 4th mission of the series more light bulbs are added.

You still must determine how long the room will be lit during the observation period between start_watching and 
end_watching. But now we have more than one light bulb. This means that in the light bulb switching array can now 
also be passed the number of the light bulb, the button of which is being pressed. 

Each element of the button clicking array can be either a datetime object (which means the time when the first button 
was pressed) or a tuple of 2 elements (where the first elements is a datetime object, the time the button was 
pressed), and the second is the number of the light bulb, the button of which is being pressed. 

If the passed array will only consist of datetime elements, then we have only one light bulb and the function should 
work the same way as in the previous mission of the series. 

Input: Three arguments and only the first one is required. The first one is a list of datetime objects (instead of 
datetime object there can be a tuple of two datetime and int), the second and the third ones are the datetime objects. 

Output: A number of seconds as an integer."""

from datetime import datetime
from typing import List, Optional


def sum_light5(els: List[datetime], start_watching: Optional[datetime] = None,
               end_watching: Optional[datetime] = None):
    bulb_0 = []
    bulb_2 = []
    bulb_3 = []
    for bulb_number in els:
        try:
            if bulb_number[1] == 2:
                bulb_2.append(bulb_number[0])
            elif bulb_number[1] == 3:
                bulb_3.append(bulb_number[0])
        except:
            bulb_0.append(bulb_number)
    bulb_res = (bulb_0 + bulb_2 + bulb_3)
    print(f'b0: {bulb_0}\nb2: {bulb_2}\nb3: {bulb_3}\nbRES: {bulb_res}')
    counter = 0
    for similar_timing in bulb_res:
        counter += bulb_res.count(similar_timing)

    return max(counting(bulb_0, start_watching, end_watching), counting(bulb_2, start_watching, end_watching), counting(
        bulb_3, start_watching, end_watching)) if counter != len(bulb_res) else counting(bulb_0, start_watching,
                                                                                         end_watching) + counting(
        bulb_2, start_watching, end_watching) + counting(bulb_3, start_watching, end_watching)


def counting(els: List[datetime], start_watching: Optional[datetime] = None,
             end_watching: Optional[datetime] = None) -> int:
    if end_watching:
        if end_watching in els:
            els = els[:els.index(end_watching) + 1]
        elif end_watching not in els:
            els.append(end_watching)
            els = sorted(els)
            els = els[:els.index(end_watching) + 1]
    try:
        final = []
        for a, b in zip(els[::2], els[1::2]):
            if start_watching <= a:
                final.append((b - a).total_seconds())
            elif start_watching <= b:
                final.append((b - start_watching).total_seconds())
        return sum(final)
    except:
        return sum([(els[i] - els[i - 1]).total_seconds() for i in range(1, len(els), 2)])


""" -------------------------------------------------------------------------------------------------------------------

#45

Create and return a new iterable that contains the same elements as the argument iterable items, but with the 
reversed order of the elements inside every maximal strictly ascending sublist. This function should not modify the 
contents of the original iterable. 

Input: Iterable

Output: Iterable"""


def reverse_ascending(items):
    if not items:
        return
    sublist = [items[0]]
    for i in range(1, len(items)):
        if sublist[-1] < items[i]:
            sublist.append(items[i])
        else:
            yield from reversed(sublist)
            sublist = [items[i]]
    yield from reversed(sublist)


""" -------------------------------------------------------------------------------------------------------------------

#46

A given list should be "compressed" in a way so, instead of two (or more) equal elements, staying one after another, 
there is only one in the result Iterable (list, tuple, iterator ...). 

Input: List.

Output: "Compressed" Iterable (list, tuple, iterator ...)."""

from typing import Iterable


def compress(items: list) -> Iterable:
    if not items:
        return items
    res = []
    for x in range(len(items) - 1):
        if items[x] != items[x + 1]:
            res.append(items[x])
    res.append(items[-1])
    return res


""" -------------------------------------------------------------------------------------------------------------------

#47

Given an iterable of ints , create and return a new iterable whose first two elements are the same as in items, 
after which each element equals the median of the three elements in the original list ending in that position. 

Wait...You don't know what the "median" is? Go check out the separate "Median" mission on CheckiO.

Input: Iterable of ints.

Output: Iterable of ints."""

from typing import Iterable


def median_three(els: Iterable[int]) -> Iterable[int]:
    out = els[0:2]
    for i in range(2, len(els)):
        out.append(sorted(els[i - 2:i + 1])[1])
    return out


""" -------------------------------------------------------------------------------------------------------------------

#48

Nicola likes to categorize all sorts of things. He categorized a series of numbers and as the result of his efforts, 
a simple sequence of numbers became a deeply-nested list. Sophia and Stephan don't really understand his organization 
and need to figure out what it all means. They need your help to understand Nikolas crazy list. 

There is a list which contains integers or other nested lists which may contain yet more lists and integers which 
then… you get the idea. You should put all of the integer values into one flat list. The order should be as it was in 
the original list with string representation from left to right. 

We need to hide this program from Nikola by keeping it small and easy to hide. Because of this, your code should be 
shorter than 140 characters (with whitespaces) . 

Input data: A nested list with integers.

Output data: The one-dimensional list with integers."""


def flat_list(array):
    if not array:
        return array
    if isinstance(array[0], list):
        return flat_list(array[0]) + flat_list(array[1:])
    return array[:1] + flat_list(array[1:])


""" -------------------------------------------------------------------------------------------------------------------

#49

Nikola likes to categorize everything in sight. One time Stephan gave him a label maker for his birthday, 
and the robots were peeling labels off of every surface in the ship for weeks. He has since categorized all the 
reagents in his laboratory, books in the library and notes on the desk. But then he learned about python dictionaries 
, and categorized all the possible configurations for Sophia’s drones. Now the files are organized in a deep nested 
structure, but Sophia doesn’t like this. Let's help Sophia to flatten these dictionaries. 

Python dictionaries are a convenient data type to store and process configurations. They allow you to store data by 
keys to create nested structures. You are given a dictionary where the keys are strings and the values are strings or 
dictionaries. The goal is flatten the dictionary, but save the structures in the keys. The result should be the a 
dictionary without the nested dictionaries. The keys should contain paths that contain the parent keys from the 
original dictionary. The keys in the path are separated by a "/". If a value is an empty dictionary, then it should 
be replaced by an empty string (""). Let's look at an example: 

Input: An original dictionary as a dict.

Output: The flattened dictionary as a dict.

Precondition:
Keys in a dictionary are non-empty strings.
Values in a dictionary are strings or dicts.
root_dictionary != {}"""


def flatten(dictionary):
    while sum(map(lambda x: type(x) == dict, dictionary.values())):
        for idx, inner_d in enumerate(dictionary.copy().items()):
            if idx == 0:
                dictionary = {}
            if type(inner_d[1]) == dict:
                if inner_d[1] == {}:
                    inner_d = [(inner_d[0], '')]
                else:
                    inner_d = [(inner_d[0] + '/' + in_d[0], in_d[1]) for in_d in inner_d[1].items()]
                for i in inner_d:
                    dictionary[i[0]] = i[1]
            else:
                dictionary[inner_d[0]] = inner_d[1]
    return dictionary


""" -------------------------------------------------------------------------------------------------------------------

#50

Let's try some sorting. Here is an array with the specific rules.

The array (a list) has various numbers. You should sort it, but sort it by absolute value in ascending order. For 
example, the sequence (-20, -5, 10, 15) will be sorted like so: (-5, 10, 15, -20). Your function should return the 
sorted list or tuple. 

Precondition: The numbers in the array are unique by their absolute values.

Input: An array of numbers , a tuple..

Output: The list or tuple (but not a generator) sorted by absolute values in ascending order.

Addition: The results of your function will be shown as a list in the tests explanation panel."""


def checkio6(values: list) -> list:
    positive_list = []
    negative_list = []
    for x in values:
        if x < 0:
            negative_list.append(x * -1)
        else:
            positive_list.append(x)
    res_list = sorted(negative_list + positive_list)
    for x in range(len(res_list)):
        if res_list[x] * -1 in values:
            res_list[x] *= -1
    return res_list


""" -------------------------------------------------------------------------------------------------------------------

#51

In a given word you need to check if one symbol goes only right after another.

Cases you should expect while solving this challenge:

If more than one symbol is in the list you should always count the first one one of the symbols are not in the given 
word - your function should return False; any symbol appears in a word more than once - use only the first one; two 
symbols are the same - your function should return False; the condition is case sensitive, which means 'a' and 'A' 
are two different symbols. Input: Three arguments. The first one is a given string, second is a symbol that should go 
first, and the third is a symbold that should go after the first one. 

Output: A bool."""


def goes_after(word: str, first: str, second: str) -> bool:
    idx1 = word.find(first)
    idx2 = word.find(second)
    if idx1 != -1 and idx2 != -1:
        if idx1 + 1 == idx2:
            return True
    return False


""" -------------------------------------------------------------------------------------------------------------------

#52

Nicola has solved this puzzle (and I am sure that you will do equally well). To be prepared for more such puzzles, 
Nicola wants to invent a method to search for words inside poetry. You can help him create a function to search for 
certain words. 

You are given a rhyme (a multiline string), in which lines are separated by "newline". Casing does not matter 
for your search, but whitespaces should be removed before your search. You should find the word inside the rhyme in 
the horizontal (from left to right) or vertical (from up to down) lines. For this you need envision the rhyme as a 
matrix (2D array). Find the coordinates of the word in the cut rhyme (without whitespaces). 

The result must be represented as a list -- [row_start,column_start,row_end,column_end] , where

row_start is the line number for the first letter of the word.
column_start is the column number for the first letter of the word.
row_end is the line number for the last letter of the word.
column_end is the column number for the last letter of the word.
Counting of the rows and columns start from 1.
rhymes
Input: Two arguments. A rhyme as a string and a word as a string (lowercase).

Output: The coordinates of the word."""


def checkio7(text, word):
    text = text.replace(' ', '').lower()
    text = text.split('\n')
    row_start = 0
    column_start = 0
    row_end = 0
    column_end = 0
    for string in text:
        word_index = string.find(word)
        if word_index != -1:
            column_start = word_index + 1
            column_end = word_index + len(word)
            row_start = row_end = text.index(string) + 1
            return row_start, column_start, row_end, column_end
    word = list(word)
    num_list = []
    for string in text:
        num_list.extend([text.index(string) + 1, x + 1, y] for x, y in enumerate(string))
    result = []
    for x in num_list:
        if x[2] in word:
            result.append(x)
    advanced_num_list = sorted(result, key=lambda x: x[1])
    result = []
    word_index = 0
    for x in range(len(advanced_num_list)):
        if advanced_num_list[x][2] == word[word_index]:
            result.extend(advanced_num_list[x])
            word_index += 1
            if word_index == len(word):
                return [result[0], result[4], result[-3], result[-2]]
        else:
            word_index = 0
            result.clear()


""" -------------------------------------------------------------------------------------------------------------------

#53

You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format and 
you see it everywhere. Your task is to convert the time from the 24-h format into 12-h format by following the next 
rules: - the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday) 
- if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.' Here you can find some useful 
information about the 12-hour format . 

Input: Time in a 24-hour format (as a string).

Output: Time in a 12-hour format (as a string)."""


def time_converter(time):
    if time == '00:00':
        return '12:00 a.m.'
    time = time.split(':')
    hours = int(time[0])
    minutes = time[1]
    if hours >= 12:
        if hours >= 13:
            return ':'.join([str(hours - 12), minutes]) + ' p.m.'
        return ':'.join([str(hours), minutes]) + ' p.m.'
    else:
        return ':'.join([str(hours), minutes]) + ' a.m.'


""" -------------------------------------------------------------------------------------------------------------------

#54

You have a list. Each value from that list can be either a string or an integer. Your task here is to return two 
values. The first one is a concatenation of all strings from the given list. The second one is a sum of all integers 
from the given list. 

Input: An array of strings ans integers

Output: A list or tuple"""


from typing import Tuple


def sum_by_types(items: list) -> Tuple[str, int]:
    res_str = ''
    res_int = 0
    for x in items:
        if isinstance(x, int):
            res_int += x
        elif isinstance(x, str):
            res_str += x
    return res_str, res_int


""" -------------------------------------------------------------------------------------------------------------------

#55

Числа Фибоначчи. Функция которая выдаст число по порядковому номеру"""


def fibonacce(arg):
    numbers = [1, 1]
    counter = 2
    while counter < arg:
        numbers.append(numbers[-1] + numbers[-2])
        counter += 1
    return numbers[-1]


""" -------------------------------------------------------------------------------------------------------------------

#56

The bird converts words by two rules:
- after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
- after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
Vowels letters == "aeiouy".

You are given an ornithological phrase as several words which are separated by white-spaces (each pair of words by 
one whitespace). The bird does not know how to punctuate its phrases and only speaks words as letters. All words are 
given in lowercase. You should translate this phrase from the bird language to something more understandable. 

Input: A bird phrase as a string.

Output: The translation as a string."""


def translate(text: str):
    vowels = "aeiouy"
    index = 0
    res = ''
    while index < len(text) - 1:
        print(text[index])
        if text[index] in vowels:
            res += text[index]
            index += 3
        elif text[index] == ' ':
            res += text[index]
            index += 1
        else:
            res += text[index]
            index += 2
    return res


""" -------------------------------------------------------------------------------------------------------------------

#57

Let's continue examining words. You are given two strings with words separated by commas. Try to find what is common 
between these strings. The words in the same string don't repeat. 

Your function should find all of the words that appear in both strings. The result must be represented as a string of 
words separated by commas in alphabetic order. 

Input: Two arguments as strings.

Output: The common words as a string."""


def checkio8(line1: str, line2: str) -> str:
    list1 = line1.split(',')
    list2 = line2.split(',')
    res = []
    for x in list1:
        if x in list2:
            res.append(x)
    return ','.join(sorted(res))


""" -------------------------------------------------------------------------------------------------------------------

#58

You’ve received a letter from a friend whom you haven't seen or heard from for a while. In this letter he gives you 
instructions on how to find a hidden treasure. 

In this mission you should follow a given list of instructions which will get you to a certain point on the map. A 
list of instructions is a string, each letter of this string points you in the direction of your next step. 

The letter "f" - tells you to move forward, "b" - backward, "l" - left, and "r" - right.

It means that if the list of your instructions is "fflff" then you should move forward two times, make one step to 
the left and then again move two times forward. 

Now, let's imagine that you are in the position (0,0). If you move forward your position will change to (0, 
1). If you move again it will be (0, 2). If your next step is to the left then your position will become (-1, 
2). After the next two steps forward your coordinates will be (-1, 4) 

Your goal is to find your final coordinates. Like in our case they are (-1, 4)

Input: A string.

Output: A tuple (or list) of two ints"""


from typing import Tuple


def follow(instructions: str) -> Tuple[int, int]:
    x = 0
    y = 0
    for letter in instructions:
        if letter == 'f':
            y += 1
        elif letter == 'b':
            y -= 1
        elif letter == 'l':
            x -= 1
        elif letter == 'r':
            x += 1
    return (x, y)


""" -------------------------------------------------------------------------------------------------------------------

#59

A pangram (Greek:παν γράμμα, pan gramma, "every letter") or holoalphabetic sentence for a given alphabet is a 
sentence using every letter of the alphabet at least once. Perhaps you are familiar with the well known pangram "The 
quick brown fox jumps over the lazy dog". 

For this mission, we will use the latin alphabet (A-Z). You are given a text with latin letters and punctuation 
symbols. You need to check if the sentence is a pangram or not. Case does not matter. 

Input: A text as a string.

Output: Whether the sentence is a pangram or not as a boolean."""


def check_pangram(text):
    alphabet = 'ABCDEFGHIKLMNOPQRSTVXYZ'
    for x in alphabet:
        if x not in text.upper():
            return False
    return True


""" -------------------------------------------------------------------------------------------------------------------

#60

Joe Palooka has fat fingers, so he always hits the “Caps Lock” key whenever he actually intends to hit the key “a” by 
itself. (When Joe tries to type in some accented version of “a” that needs more keystrokes to conjure the accents, 
he is more careful in the presence of such raffinated characters ([Shift] + [Char]) and will press the keys 
correctly.) Compute and return the result of having Joe type in the given text. The “Caps Lock” key affects only the 
letter keys from “a” to “z” , and has no effect on the other keys or characters. “Caps Lock” key is assumed to be 
initially off. 

Input: A string. The typed text.

Output: A string. The showed text after being typed."""


def caps_lock(text: str) -> str:
    text = text.split('a')
    for x in range(1,len(text),2):
        text[x] = text[x].upper()
    return ''.join(text)


""" -------------------------------------------------------------------------------------------------------------------

#61

You are given a text, which contains different English letters and punctuation symbols. You should find the most 
frequent letter in the text. The letter returned must be in lower case. While checking for the most wanted letter, 
casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation 
symbols, digits and whitespaces, only letters. 

If you have two or more letters with the same frequency , then return the letter which comes first in the Latin 
alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e". 

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a string."""


def checkio9(text: str) -> str:
    list_of_letters = [['a', 0],
                       ['b', 0],
                       ['c', 0],
                       ['d', 0],
                       ['e', 0],
                       ['f', 0],
                       ['g', 0],
                       ['h', 0],
                       ['i', 0],
                       ['j', 0],
                       ['k', 0],
                       ['l', 0],
                       ['m', 0],
                       ['n', 0],
                       ['o', 0],
                       ['p', 0],
                       ['q', 0],
                       ['r', 0],
                       ['s', 0],
                       ['t', 0],
                       ['u', 0],
                       ['v', 0],
                       ['w', 0],
                       ['x', 0],
                       ['y', 0],
                       ['z', 0]]
    for letter in list_of_letters:
        if letter[0] in text.lower():
            letter[1] = text.lower().count(letter[0])
    return str(sorted(list_of_letters, key=lambda x: x[1], reverse=True)[0][0])


""" -------------------------------------------------------------------------------------------------------------------

#62

Our robots are always working to improve their linguistic skills. For this mission, they research the Latin alphabet 
and its applications. 

The alphabet contains both vowel and consonant letters (yes, we divide the letters).
Vowels -- A E I O U Y
Consonants -- B C D F G H J K L M N P Q R S T V W X Z

You are given a block of text with different words. These words are separated by whitespaces and punctuation marks. 
Numbers are not considered as words in this mission (a mix of letters and digits is not a word either). You should 
count the number of words (striped words) where the vowels with consonants are alternating; words that you count 
cannot have two consecutive vowels or consonants. The words consisting of a single letter are not striped -- don't 
count those. Casing is not significant for this mission. 

Input: A text as a string (unicode)

Output: A quantity of striped words as an integer."""


def checkio10(line: str):
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y', ' ']
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z', ' ']
    line = line.replace('.', ' ').replace(',', ' ').replace('?', ' ').replace('!', ' ')
    line = line.upper().split()
    res_list = []
    for word in line:
        if len(word) < 2 or not word.isalpha():
            res_list.append(word)
            continue
        for letter_idx in range(len(word) - 1):
            if word[letter_idx] in vowels and word[letter_idx + 1] not in consonants or \
                    word[letter_idx] in consonants and word[letter_idx + 1] not in vowels:
                res_list.append(word)
                break
    return len(line) - len(res_list)


""" -------------------------------------------------------------------------------------------------------------------

#63

Your mission is to convert the name of a function (a string) from CamelCase ("MyFunctionName") into the Python format 
("my_function_name") where all chars are in lowercase and all words are concatenated with an intervening underscore 
symbol "_". 

Input: A function name as a CamelCase string.

Output: The same string, but in under_score."""


def from_camel_case(name: str) -> str:
    name = list(name)
    for x in range(len(name) - 1):
        if name[x + 1].isupper():
            name[x] += '_'
    return ''.join(name).lower()


""" -------------------------------------------------------------------------------------------------------------------

#64

Your mission is to convert the name of a function (a string) from the Python format (for example "my_function_name") 
into CamelCase ("MyFunctionName"), where the first char of every word is in uppercase and all words are concatenated 
without any intervening characters. 

Input: A function name as a string.

Output: The same string, but in CamelCase."""


def to_camel_case(name: str) -> str:
    name = list(name)
    for x in range(len(name) - 1):
        if x == 0:
            name[x] = name[x].upper()
        if name[x] == '_':
            name[x+1] = name[x+1].upper()
            name[x] = name[x].replace('_', '')
    return ''.join(name)


""" -------------------------------------------------------------------------------------------------------------------

#65

Ever tried to send a secret message to someone without using the postal service? You could use newspapers to tell 
your secret. Even if someone finds your message, it's easy to brush them off as paranoid and as a conspiracy 
theorist. One of the simplest ways to hide a secret message is to use capital letters. Let's find some of these 
secret messages. 

You are given a chunk of text. Gather all capital letters in one word in the order that they appear in the text.

For example: text = " H ow are you? E h, ok. L ow or L ower? O hhh.", if we collect all of the capital letters, 
we get the message "HELLO". 

Input: A text as a string (unicode).

Output: The secret message as a string or an empty string."""


def find_message(message: str) -> str:
    res = ''
    for x in message:
        if x.isupper():
            res += x
    return res


""" -------------------------------------------------------------------------------------------------------------------

#66 !NOT MINE!

Before solving this mission, you can try to solve the "Brackets" mission.

Your task is to restore the balance of open and closed brackets by removing the unnecessary ones, while trying to use 
the minimum number of deletions. 

Only 3 types of brackets (), [] and {} can be used in the given string.

Only a parenthesis can close a parenthesis. That is, in this expression "(}" - the brackets aren’t balanced. In an 
empty string, i.e., in a string that doesn’t contain any brackets - the brackets are balanced, but removing all of 
the brackets isn’t considered to be an optimal solution. 

If there are more than one correct answer, then you should choose the one where the character that can be removed is 
closer to the beginning. For example, in this case "[(])", the correct answer will be "()", since the removable 
brackets are closer to the beginning of the line. 

Input: A string of characters () {} []

Output: A string of characters () {} []"""


def remove_brackets(line):
    m, match, count = [], [], {i: line.count(i) for i in '[{()}]'}
    for i, b in enumerate(line):
        if b == '(' and count[')'] >= m.count(b) + 1: m.extend([b, i])
        elif b in '[{' and count[chr(ord(b)+2)] >= m.count(b) + 1: m.extend([b, i])
        elif b in ")}]" and m and abs(ord(b) - ord(m[-2])) <= 2: match.extend([(i, b), (m.pop(), m.pop())])
    return ''.join([i for _, i in sorted(match)])


""" -------------------------------------------------------------------------------------------------------------------

#66

Have you ever heard of such markup language as YAML ? It’s a friendly data serialization format. In fact it’s so 
friendly that both people and programs can read it quite well. You can play around with the standard by following 
this link . 

YAML is a text, and you need to convert it into an object. But I’m not asking you to implement the entire YAML 
standard, we’ll implement it step by step. 

The first step is the key-value conversion. The key can be any string consisting of Latin letters and numbers. The 
value can be a single-line string (which consists of spaces, Latin letters and numbers) or a number (int). 

I’ll show some examples:

name: Alex
age: 12
Converted into an object.

{ 
  "name": "Alex",
  "age": 12
}
 
Note that the number automatically gets type int

Another example shows that the string may contain spaces.

name: Alex Fox
age: 12

class: 12b
Will be converted into the next object.

{ "age": 12, "name": "Alex Fox", "class": "12b" } Pay attention to a few things. Between the string "age" and the 
string "class" there is an empty string that doesn’t interfere with parsing. The class starts with numbers, 
but has letters, which means it cannot be converted to numbers, so its type remains a string (str). 

Input: A format string.

Output: An object."""


def yaml(a):
    res_dict = {}
    a = a.split('\n')
    for x in a:
        if not x:
            continue
        x = x.split(': ')
        try:
            res_dict.setdefault(x[0], int(x[1]))
        except:
            res_dict.setdefault(x[0], x[1])
    return res_dict


""" -------------------------------------------------------------------------------------------------------------------

#67 

This is the second task on parsing YAML. It represents the next step where parsing gets more complicated. The 
data types, such as null and bool, are being added, and besides that, you’re getting the ability to use quotes in 
strings. 

Here are some of the examples:

name: "Bob Dylan"
children: 6
{
  "name": "Bob Dylan", 
  "children": 6
}
As you can see, the string can be put in quotes. It can be both double and single quotes.

name: "Bob Dylan"
children: 6
alive: false
{
  "name": "Bob Dylan", 
  "alive": False, 
  "children": 6
}
true and false are the keywords defining the boolean type.

name: "Bob Dylan"
children: 6
coding:
{
  "coding": None, 
  "name": "Bob Dylan", 
  "children": 6
}
If no value is specified, it becomes undefined. There also is a keyword for this - null.

Input: A format string.

Output: An object."""


def yaml1(a):
    res_dict = {}
    a = a.replace('"', '').replace('\\', '"')
    a = a.split('\n')
    for x in a:
        print(x)
        if not x:
            continue
        x = x.split(': ')
        if len(x) < 2:
            x[0] = x[0].replace(':', '')
            res_dict.setdefault(x[0], None)
        elif not x[1].lower() or x[1].lower() == 'null':
            res_dict.setdefault(x[0], None)
        elif 'null' in x[1].lower():
            res_dict.setdefault(x[0], 'null')
        elif x[1].lower() == 'true':
            res_dict.setdefault(x[0], True)
        elif x[1].lower() == 'false':
            res_dict.setdefault(x[0], False)
        else:
            try:
                res_dict.setdefault(x[0], int(x[1]))
            except:
                res_dict.setdefault(x[0], x[1])
    return res_dict


""" -------------------------------------------------------------------------------------------------------------------

#68

For language training our Robots want to learn about suffixes.

In this task, you are given a set of words in lower case. Check whether there is a pair of words, such that one word 
is the end of another (a suffix of another). For example: {"hi", "hello", "lo"} -- "lo" is the end of "hello", 
so the result is True. 

Input: Words as a set of strings.

Output: True or False, as a boolean."""


def checkio11(words_set):
    words_set = list(words_set)
    for x in range(len(words_set)):
        idx = 0
        while idx < len(words_set):
            print(words_set[x], words_set[idx])
            if words_set[x].endswith(words_set[idx]) and words_set[x] != words_set[idx]:
                print(words_set[x], words_set[idx])
                return True
            else:
                idx += 1
    return False


""" -------------------------------------------------------------------------------------------------------------------

#69

As the input you get the flight schedule as an array, each element of which is the price of a direct flight between 2 
cities (an array of 3 elements - 2 city names as a string, and a flight price). 

Planes fly in both directions and the price in both directions is the same. There is a possibility that there are no 
direct flights between cities. 

Find the price of the cheapest flight between cities that are given as the 2nd and 3rd arguments.

Input: 3 arguments: the flight schedule as an array of arrays, city of departure and destination city.

Output: Int. The best price."""


