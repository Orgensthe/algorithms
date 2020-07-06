

def repeatedString(s, n):

    countOfA = 0
    for character in s:
        if (character == "a"): countOfA += 1

    times = (n // len(s))
    result = times * countOfA

    for i in range(n % len(s)):
        if s[i] == "a":
            result +=1

    return result



print(repeatedString("aba",10))
