# Problem 20: Group Anagrams
# Given an array of strings, group the anagrams together. Two words are considered anagrams if they have the same characters but in a different order.

def is_anagram (s1: str, s2: str) -> bool:
    flag: bool = True
    for char in s1:
        if char not in s2:
            flag = False
    return flag


def group_anagrams (strings):
    result = []
    done = []
    for i in range(len(strings)):
        lst = []
        if i not in done:
            for j in range(1, len(strings)):
                if is_anagram(strings[i], strings[j]) and i != j:
                    if not lst:
                        lst.append(strings[i])
                        lst.append(strings[j])
                        done.append(i)
                        done.append(j)
                    else:
                            lst.append(strings[j])
                            done.append(j)
                elif not lst:
                    lst.append(strings[i])
            result.append(lst)
    return result


print(group_anagrams (["listen", "silent", "enlist", "google", "gogole", "foo", "oof"]))