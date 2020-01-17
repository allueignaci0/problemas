################              
#     IGNA     #
################

def dashatize(num):
    # if no num:
    #   return None
    dashed_digits = [(x if int(x)%2 == 0 else '-' + x + '-') for x in str(abs(num))]
    string = ''.join(dashed_digits).replace('--', '-').strip('-')
    return string


