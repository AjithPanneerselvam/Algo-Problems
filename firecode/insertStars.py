"""
Microsoft

Given a string, recursively compute a new string
where identical, adjacent characters
get separated with a "*".

Example:
insert_star_between_pairs("cac") ==> "cac"
insert_star_between_pairs("cc") ==> "c*c"
"""

def insert_star_between_pairs(a_string):
    if a_string == None:
        return None

    if len(a_string) > 1:
        if a_string[0] == a_string[1]:
            a_string = a_string[0] + "*" + insert_star_between_pairs(a_string[1:])
        else:
            a_string = a_string[0] + insert_star_between_pairs(a_string[1:])

    return a_string
