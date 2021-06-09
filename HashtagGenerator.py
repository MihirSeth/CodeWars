def generate_hashtag(s):
    caps = s.title()
    noSpace = caps.replace(" ",'')
    result = '#' + noSpace

    if len(result) > 140:
        return False

    elif s == '':
        return False
    
    else:
        return result


# https://www.codewars.com/kata/52449b062fb80683ec000024