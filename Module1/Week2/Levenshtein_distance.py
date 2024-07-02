
# Using Recursion
def recursed_levenshtein_distance(source, target, m, n):

    # Empty string
    if m == 0:
        return n
    if n == 0:
        return m
    if source[m-1] == target[n-1]:
        return recursed_levenshtein_distance(source, target, m-1, n-1)
    return 1 + min(
        # insert
        recursed_levenshtein_distance(source, target, m, n-1),
        # remove
        recursed_levenshtein_distance(source, target, m-1, n),
        # replace
        recursed_levenshtein_distance(source, target, m-1, n-1)
    )


def levenshtein_distance(source, target):
    distance = recursed_levenshtein_distance(
        source, target, len(source), len(target))
    return distance


if __name__ == "__main__":
    source = "hola"
    target = "hello"
    distance = levenshtein_distance(source, target)
    print("Levenshtein Distance:", distance)
