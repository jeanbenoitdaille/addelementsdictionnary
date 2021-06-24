# addelementsdictionnary
Ajouter des éléments à un dictionnaire 
Pour cet exercice, nous avons du ruser un peu. Peut-être avez-vous commencé par utiliser la fonction enumerate pour récupérer directement l'indice et l'élément sur lequel on boucle ? Le problème est qu'ici, certains éléments ne sont pas valides et sont donc ignorés. Ainsi, pour garder un id d'employé continue, nous ne pouvons pas utiliser l'indice de l'élément sur lequel on boucle.

C'est la raison d'être de la variable i que nous initialisons à 1 avant de passer dans la boucle et que nous incrémentons chaque fois qu'un employé valide est détecté.

Pour détecter si un élément de la liste ne contient que des nombres, on utilise la fonction isdigit :

    if not str(element).isdigit():

Pour formatter la clé dans le dictionnaire, on utilise la fonction format :

    employes["id-{:02d}".format(i)] = element

La syntaxe :02d permet d'indiquer que nous souhaitons formater le nombre i pour qu'il contienne toujours 2 chiffres : 1 deviendra 01, 2 deviendra 02, 15 restera tel quel etc.
