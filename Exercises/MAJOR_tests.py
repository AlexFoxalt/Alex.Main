def check_connection(network, first, second):
    base = []

    for pare in network:
        if first not in pare and second not in pare:
            continue
        x, y = pare.split('-')
        if not base:
            base.extend([x, y])
        else:
            if x in base and y in base:
                pass
            elif x not in base and y not in base:
                pass
            elif x in base:
                base.append(y)
            elif y in base:
                base.append(x)
    print(base)
    return first in base and second in base

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
