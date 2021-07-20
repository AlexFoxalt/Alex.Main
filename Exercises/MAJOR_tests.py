def caps_lock(text: str) -> str:
    text = text.split('a')
    for x in range(1,len(text),2):
        text[x] = text[x].upper()
    return ''.join(text)


print(caps_lock("Why are you asking me that?"))
