def convert(number):
    number = int(number)
    if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
        return 'PlingPlangPlong'
    elif number % 3 == 0 and number % 7 == 0 and number % 5 == 0:
        return 'PlingPlongPlang'
    elif number % 5 == 0 and number % 7 == 0 and number % 3 == 0:
        return 'PlangPlongPling'
    elif number % 5 == 0 and number % 3 == 0 and number % 7 == 0:
        return 'PlangPlingPlong'
    elif number % 7 == 0 and number % 5 == 0 and number % 3 == 0:
        return 'PlongPlangPling'
    elif number % 7 == 0 and number % 3 == 0 and number % 5 == 0:
        return 'PlongPlingPlang'
    elif number % 3 == 0 and number % 5 == 0:
        return 'PlingPlang'
    elif number % 5 == 0 and number % 3 == 0:
        return 'PlangPling'
    elif number % 3 == 0 and number % 7 == 0:
        return 'PlingPlong'
    elif number % 7 == 0 and number % 3 == 0:
        return 'PlongPling'
    elif number % 5 == 0 and number % 7 == 0:
        return 'PlangPlong'
    elif number % 7 == 0 and number % 5 == 0:
        return 'PlongPlang'
    elif number % 3 == 0:
        return 'Pling'
    elif number % 5 == 0:
        return 'Plang'
    elif number % 7 == 0:
        return 'Plong'
    else:
        return str(number)
