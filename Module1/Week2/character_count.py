def character_count(string):
    chars_list = {}
    for char in string:
        if char in chars_list:
            chars_list[char] += 1
        else:
            chars_list[char] = 1
    return dict(sorted(chars_list.items(), key=lambda item: item[1]))


if __name__ == "__main__":
    assert character_count('Baby') == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
    print(character_count('smiles'))
