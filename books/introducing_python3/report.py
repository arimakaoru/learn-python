def get_description():
    """プロと同じようにランダムな天気予報を返す"""
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who know']
    return choice(possibilities)
    
