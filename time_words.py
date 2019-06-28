""" Hackerrank   The Time in words Medium 25 Max Score
    Input Format
    The first line contains , the hours portion The second line contains , the minutes portion
    Constraints
    Output Format
    Print the time in words as described.
    Sample Input 0
    5
    47
    Sample Output 0
    thirteen minutes to six
    """

# Complete the timeInWords function below.


def timeInWords(h, m):
    dictionary_time = {
        '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
        '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'quarter',
        '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen', '20': 'twenty', '21': 'twenty one',
        '22': 'twenty two', '23': 'twenty three', '24': 'twenty four', '25': 'twenty five', '26': 'twenty six',
        '27': 'twenty seven', '28': 'twenty eight', '29': 'twenty nine', '30': 'half', '0': 'zero'
    }

    minute_temp = m
    if m > 30:
        minute_temp = m - 30

    hours = dictionary_time[str(h)]
    minutes = dictionary_time[str(minute_temp)]

    if m == 0:
        addition = " o' clock"
        res = hours + addition
        return res
    elif 1 <= m <= 30:
        addition = "past"
        if m != 30 and m != 1 and m != 15:
            res = minutes + ' minutes ' + addition + ' ' + hours
            return res
        elif m == 1:
            res = minutes + ' minute ' + addition + ' ' + hours
            return res
        else:
            res = minutes + ' ' + addition + ' ' + hours
            return res
    elif m > 30:
        m = abs(m - 60)
        addition = "to"
        minutes = dictionary_time[str(m)]
        hours = dictionary_time[str(h + 1)]
        if m != 15:
            res = minutes + ' minutes ' + addition + ' ' + hours
            return res
        else:
            res = minutes + ' ' + addition + ' ' + hours
            return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    h = int(input())
    m = int(input())
    result = timeInWords(h, m)
    # fptr.write(result + '\n')
    # fptr.close()
    print(result)