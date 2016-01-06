# coding: utf-8
import sys
sys.setrecursionlimit(100000000)
def getNext(password):
    pwd = list(password)  ## Creation d'un tableau à partir de l'element passer en parametre de la fonction
    found = False
    i=len(pwd)-1
    while not found:
        if pwd[i] < 'z':
           pwd[i] = chr(ord(pwd[i])+1)  ## Si la derniere lettre est inferieur a 'z', recuperer la valeur de cette lettre, incrementer, puis reconvertir en caractere
           if pwd[i] == "i" or pwd[i] == "l" or pwd[i] == "o":
               pwd[i] = chr(ord(pwd[i])+1)
           found = True
        else:
           if i > 0:
             pwd[i] = 'a'
             i = i-1
           else:
             raise Exception('Erreur lors de la conversion de '+password)
    return ''.join(pwd)




def hasSeries(password):
    for i in range(0,len(password)-3):
        if ord(password[i])+2 == ord(password[i+1])+1 and ord(password[i+1])+1 == ord(password[i+2]):
            return True
    return False
def hasTwoPairs(password):
    count = 0
    i = 0
    for i in range (0,len(password)-1):
         if password[i] == password[i+1]:
            count = count+1
            i = i+1
            if count >=2 :
                return True
    return False

def hasNoBadChar(password):
    for i in range(0,len(password)-1):
        if password[i] == "i" or password[i] == "o" or password[i] == 'l':
            return False
    return True

def hasOtherThanZ(password):
    for i in range(0,len(password)-1):
        if password[i] != "z":
            return True
    return False
# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également. 
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous. 
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py" en console.

if __name__ == "__main__":
    count_getNext = 0
    passwd = "quentintroncy"
    while True:
        if hasNoBadChar(passwd) and hasSeries(passwd) and hasTwoPairs(passwd):
            print()
            print(''.join(passwd)+" : "+str(count_getNext))## renvoi de pwd modifie selon les regles d'Edward
            exit(0)
        else:
            count_getNext = count_getNext+1
            print(''.join(passwd)+" : "+str(count_getNext))
            passwd = getNext(''.join(passwd))


    print(passwd)


