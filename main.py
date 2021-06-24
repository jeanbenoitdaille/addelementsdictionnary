employes = {}
     
liste = [10, 2329, 5, "Pierre", 203, "Marie", 867, "Adrien"]
     
i = 1
     
for element in liste:
        if not str(element).isdigit():
            employes["id-{:02d}".format(i)] = element
            i += 1
     
print(employes)