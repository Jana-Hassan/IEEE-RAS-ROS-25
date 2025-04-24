import re

def Valid_number(credit_card):
    if credit_card[0] not in {'4', '5', '6'}:
        return False
        
    if '-' in credit_card:
        group = credit_card.split('-')
        if len(group) != 4:
            return False
        for g in group:
            if len(g) != 4:
                return False
        credit_card = ''.join(group)
    
    if len(credit_card) != 16:
        return False
        
    if  credit_card.isdigit() != True:
        return False
    
    for d in set(credit_card):
        if d*4 in credit_card:
            return False
    
    return True

n = int(input())
for _ in range(n):
    credit_card = input().strip()
    if Valid_number(credit_card):
        print('Valid')
    else:
        print('Invalid')
