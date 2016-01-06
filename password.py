# coding: utf-8 
def getNext(password):
    """
    Série de tests exprimés en doctest
    >>> getNext('a')
    'b'
    >>> getNext('az')
    'ba'
    >>> getNext('bc')
    'bd'
    """
    pwd = list(password)  ## Creation d'un tableau à partir de l'element passer en parametre de la fonction
    found = False
    i=len(pwd)-1

    while not found:
        if pwd[i] < 'z':
           pwd[i] = chr(ord(pwd[i])+1)  ## Si la derniere lettre est inferieur a 'z', recuperer la valeur de cette lettre, incrementer, puis reconvertir en caractere
           found = True             
        else:
           pwd[i] = 'a'
           i = i-1 
    
    return ''.join(pwd)  ## renvoi de pwd modifie selon les regles d'Edward



# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également. 
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous. 
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py" en console.
#import doctest
#doctest.testmod()
if __name__ == "__main__":
    print(getNext("Z"))
    print(getNext("9"))
