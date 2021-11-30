#rekne, zda jsou seznamy s unikatnimi prvky stejne
def jsou_stejne(s1,s2):
    return set(s1) == set(s2)

#rekne, zda jsou seznamy s opakujicimi se prvky stejne
def jsou_stejne_i_s_opakovanim(s1,s2):
    return sorted(s1) == sorted(s2)

#rekne, zda jsou prvky v seznamu ruzne
def jsou_vsechny_provky_ruzne(s1):
    return len(set(s1)) == len(s1)


