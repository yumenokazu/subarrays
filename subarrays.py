import itertools


def subsets(numbers, target, partial=None, result=None):
    if partial is None:
        partial = []

    if result is None:
        result = []
    s = sum(partial)

    if s >= target:
        result.append(partial)
        return

    for i in range(len(numbers)):
        n = numbers[i]
        subsets(numbers[i+1:], target, partial + [n], result)

    return _deduplicated(result)


def _deduplicated(dupes):
    for dupe in dupes:
        dupe.sort()
    dupes.sort()
    return [dupes[i] for i in range(len(dupes)) if i == 0 or dupes[i] != dupes[i - 1]]


def subarrays(numbers, target):
    r = subsets(numbers, target)
    r.sort(key=lambda x: sum(x))
    #[print("%s = %s"%(item, sum(item))) for item in r]
    first_gap_index = 0
    return r
    # :TODO:
    for i in range(1, len(r)):
        if sum(r[i]) != sum(r[i-1]):
            first_gap_index = i
            break
    combos = itertools.combinations(r[:i], 2)
    for combo in combos:
        print(combo[0])
        print(combo[1])
        print([x for x in combo[0] if x in combo[1]])


    # find non-overlapping among first sum
    # find occurrences of a sequence


def parse_string(numbers: str):
    return [int(item) for item in numbers.split(',')]


def test_subarrays():
    data = [15, 17, 17, 5, 7, 9, 11, 11, 15]
    return subarrays(data, 40)
