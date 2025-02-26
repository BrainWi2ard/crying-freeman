from fuzzywuzzy import fuzz

def fuzzy_match(data1, data2):
    matches = {}
    for key in data1:
        if key in data2:
            match_score = fuzz.ratio(data1[key], data2[key])
            matches[key] = match_score
    return matches
