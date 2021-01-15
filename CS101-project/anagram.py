"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
DATA = []


def main():
    read_dictionary()
    while True:
        s = input("Find anagrams for: ")
        if s == EXIT:
            break
        else:
            find_anagrams(s)


def read_dictionary():
    with open(FILE) as data_set:
        for letter in data_set:
            DATA.append(letter.strip())


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    print("Searching...")
    ans = []
    d = {}
    d_cur = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    ans = helper(s, "", len(s), ans, d, d_cur)
    c = list(set(DATA) & set(ans))
    for i in c:
        print(f"Found: {i}")
        print("Searching...")
    print(f"{len(c)} anagrams: {c}")


def helper(s, cur, target_len, ans, d, d_cur):
    for ch in s:
        if ch not in cur:
            cur += ch
            d_cur[ch] = 1
            # has_prefix is much slower than my version
            # if has_prefix(cur) is False:
            #     d_cur[ch[-1]] -= 1
            #     cur = cur[:-1]
            if len(cur) == target_len:
                ans.append(cur)
            else:
                helper(s, cur, target_len, ans, d, d_cur)
            d_cur[ch[-1]] -= 1
            cur = cur[:-1]
        elif d_cur[ch] < d[ch]:
            cur += ch
            d_cur[ch] += 1
            # has_prefix is much slower than my version
            # if has_prefix(cur) is False:
            #     d_cur[ch[-1]] -= 1
            #     cur = cur[:-1]
            if len(cur) == target_len:
                ans.append(cur)
            else:
                helper(s, cur, target_len, ans, d, d_cur)
            d_cur[ch[-1]] -= 1
            cur = cur[:-1]
    return ans


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for i in DATA:
        if i.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
