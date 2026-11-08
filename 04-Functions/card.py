def hide(card_number):
    hiden_number = card_number[:2] + [10 * '*'] + card_number[-4:]
    return hiden_number
    
