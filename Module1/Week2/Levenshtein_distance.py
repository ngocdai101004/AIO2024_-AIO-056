
#Using Recursion
def  levenshtein_distance(source, target, m, n):

    # Empty string
    if m == 0:
        return n
    if n == 0:
        return m
    if source[m-1] == target[n-1]:
        return levenshtein_distance(source, target, m-1, n-1)
    return 1 + min(
        #insert
        levenshtein_distance(source, target, m, n-1),
        #remove
        levenshtein_distance(source, target, m-1, n),
        #replace
        levenshtein_distance(source, target, m-1, n-1)
    )

if __name__ == "__main__":
    source = "hola"
    target = "hello"
    distance = levenshtein_distance(source, target, len(source), len(target))
    print("Levenshtein Distance:", distance)