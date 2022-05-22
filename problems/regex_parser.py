def is_match(text, pattern):
#    match = True
    text_index = 0
    pattern_index = 0
    while text_index < len(text) and pattern_index < len(pattern):
        if pattern[pattern_index] == ".":
            pattern_index += 1
            text_index += 1
            continue
        elif pattern_index + 1 < len(pattern) and pattern[pattern_index + 1] == "*":
            wild_card_character = pattern[pattern_index]
            while text_index < len(text) and text[text_index] == wild_card_character:
                text_index += 1
            pattern_index += 2
        else:
            if text[text_index] == pattern[pattern_index]:
                text_index += 1
                pattern_index += 1
                continue
            else:
                return False

    # case 1 : text_index = len(text), pattern_index = len(pattern) - return True
    if text_index == len(text) and pattern_index == len(pattern):
        return True

    # case 2 :  text_index still not reached the last character
    if text_index < len(text) and pattern_index == len(pattern):
        return False

    # case 3 : patten_index has more characters
    # if all succeeding characters are of the form x* where x is a valid character ( apart from  * and .)
    if text_index == len(text) and pattern_index < len(pattern):
        while pattern_index < len(pattern):
            if pattern[pattern_index] == "*":
                raise Exception("Invalid pattern. * should be preceded with a character")
            # pattern[pattern_index] it is a valid character
            if pattern_index + 1 < len(pattern) and pattern[pattern_index + 1] == "*":
                pattern_index += 2
                continue
            else:
                return False
        return True


def is_match_recurse(text, pattern, text_index, pattern_index):
    # Recursion base condition
    # t = None
    # if text_index < len(text):
    #     t = text[text_index]
    # p = None
    # if pattern_index < len(pattern):
    #     p = pattern[pattern_index]
    # print("finding match for ",text_index, pattern_index, t, p, len(text), len(pattern))

    if text_index >= len(text):
#        print("Reached end of ")
        if pattern_index >= len(pattern): # Both text and pattern have ended
 #           print("Reached end")
            return True
        elif pattern_index + 1 < len(pattern) and pattern[pattern_index + 1] == "*":
            return is_match_recurse(text, pattern, text_index, pattern_index + 2)
        else:
            return False
    # pattern ended but more text
    elif pattern_index >= len(pattern):
        return False

    elif pattern_index + 1 < len(pattern) and pattern[pattern_index + 1] == "*":
        if pattern[pattern_index] == "." or pattern[pattern_index] == text[text_index]:
            matching1 = is_match_recurse(text, pattern, text_index, pattern_index + 2)
            matching2 = is_match_recurse(text, pattern, text_index + 1, pattern_index)
  #          print(matching1, matching2)
            return  matching1 or matching2
        else:
            # 0 occurance
   #         print(text_index, pattern_index, print(text[text_index], pattern[pattern_index]))
            return is_match_recurse(text, pattern, text_index, pattern_index + 2)
    elif pattern[pattern_index] == "." or pattern[pattern_index] == text[text_index]:
    #    print("Found match for ", text_index, pattern_index, t, p)

        return is_match_recurse(text, pattern, text_index + 1, pattern_index + 1)
    else:
     #   print("No match for ", text_index, pattern_index, t, p)
        return False



def is_match_recursion(text, pattern):
    return is_match_recurse(text, pattern, 0, 0)

fn = is_match_recursion
if __name__ == "__main__":
    assert(fn("abcd", "abcd"))
    assert(fn("", ".*"))
    assert(fn("abcd", "a.*cd"))
    assert(fn("sunaaal", "suna*l"))
    assert(fn("sunilabcdanil", "sunil.*anil"))
