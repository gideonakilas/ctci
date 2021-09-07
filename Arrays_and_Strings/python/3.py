
def urlify(string, trueLength):
    url = list(string)
    for i in range(len(url)):
        if url[i] == ' ':
            url[i] = '%20'

    return ''.join(url)


print(urlify("Mr John Smith ", 13))
print(urlify("Mr John  Smith ", 14))
print(urlify("Mr John Smith ", 13))
print(urlify("Mr John Smith ", 13))
print(urlify("Mr John Smith ", 13))
