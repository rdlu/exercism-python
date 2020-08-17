def first_phrase(qty):
    ordinal_days = ['first', 'second', 'third',
                    'fourth', 'fifth', 'sixth',
                    'seventh', 'eighth', 'ninth',
                    'tenth', 'eleventh', 'twelfth']
    return "On the {} day of Christmas my true love gave to me: ".format(ordinal_days[qty-1])

def last_phrase(qty):
    return "{}a Partridge in a Pear Tree.".format("and " if qty > 1 else "")

def middle_phrases(qty):
    rows = ["twelve Drummers Drumming, ",
            "eleven Pipers Piping, ",
            "ten Lords-a-Leaping, ",
            "nine Ladies Dancing, ",
            "eight Maids-a-Milking, ",
            "seven Swans-a-Swimming, ",
            "six Geese-a-Laying, ",
            "five Gold Rings, ",
            "four Calling Birds, ",
            "three French Hens, ",
            "two Turtle Doves, ", 
            ""]
    return ''.join(rows[-qty:])


def recite_one(qty):
    return first_phrase(qty) \
        + middle_phrases(qty) \
        + last_phrase(qty)

def recite(start_qty, end_qty):
    return [recite_one(n) for n in range(start_qty, end_qty+1) ]