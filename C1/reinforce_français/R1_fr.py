# Écrivez une fonction courte en Python, est_multiple(n,m), qui prend deux valeurs entiéres et renvoie Ture si c'est un multiple de m, c'est-à-dire n = mi, pour un entier i, et False, sinon

""" Tout d'abord, nous devons créer deux entrées: n et m, qui recevront les deux valeurs nécessaires.

n = int(input()) - Cela signifie que tout le contenu saisi par l'utilisaateur sera converti en valeur entiére, laquelle sera stockée dans la variale N.

def es_multiple(n,m): ils s'agit d'une fonction qui recevra deux entrées, exactement comme une foncton mathematique de R^2 vers R^1

if(n%m==0): cette instruction if déclare: si je divise n par m et que l reste est nul, alors nous obtenons un nombre pair. La fonction renvoie donc Vrai. Sinon, la fonction renvoie Faux.

Enfin, nous appelons la fonction avec est_multiple(n,m). """

n = int(input())
m = int(input())

def est_multiple(n,m):
    if (n%m==0):
        return print("Vrai")
    else:
        return print("Faux")

est_multiple(n,m)

