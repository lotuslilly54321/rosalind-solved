#
# RNAToAminoAcids.py
# Bat, Cat, Rat, Buntt
#

translations = {
    'UUU': 'F',
    'CUU': 'L',
    'AUU': 'I',
    'GUU': 'V',
    'UUC': 'F',
    'CUC': 'L',
    'AUC': 'I',
    'GUC': 'V',
    'UUA': 'L',
    'CUA': 'L',
    'AUA': 'I',
    'GUA': 'V',
    'UUG': 'L',
    'CUG': 'L',
    'AUG': 'M',
    'GUG': 'V',
    'UCU': 'S',
    'CCU': 'P',
    'ACU': 'T',
    'GCU': 'A',
    'UCC': 'S',
    'CCC': 'P',
    'ACC': 'T',
    'GCC': 'A',
    'UCA': 'S',
    'CCA': 'P',
    'ACA': 'T',
    'GCA': 'A',
    'UCG': 'S',
    'CCG': 'P',
    'ACG': 'T',
    'GCG': 'A',
    'UAU': 'Y',
    'CAU': 'H',
    'AAU': 'N',
    'GAU': 'D',
    'UAC': 'Y',
    'CAC': 'H',
    'AAC': 'N',
    'GAC': 'D',
    'UAA': 'Z',
    'CAA': 'Q',
    'AAA': 'K',
    'GAA': 'E',
    'UAG': 'Z',
    'CAG': 'Q',
    'AAG': 'K',
    'GAG': 'E',
    'UGU': 'C',
    'CGU': 'R',
    'AGU': 'S',
    'GGU': 'G',
    'UGC': 'C',
    'CGC': 'R',
    'AGC': 'S',
    'GGC': 'G',
    'UGA': 'Z',
    'CGA': 'R',
    'AGA': 'R',
    'GGA': 'G',
    'UGG': 'W',
    'CGG': 'R',
    'AGG': 'R',
    'GGG': 'G'
}

penicillin =  'MKNRNRMIVNCVTASLMYYWSLPALAEQSSSEIKIVRDEYGMPHIYANDTWHLFYGYGYVVAQDRLFQMEMARRSTQGTVAEVLGKDFVKFDKDIRRNYWPDAIRAQIAALSPEDMSILQGYADGMNAWIDKVNTNPETLLPKQFNTFGFTPKRWEPFDVAMIFVGTMANRFSDSTSEIDNLALLTALKDKYGVSQGMAVFNQLKWLVNPSAPTTIAVQESNYPLKFNQQNSQTAALLPRYDLPAPMLDRPAKGADGALLALTAGKNRETIAAQFAQGGANGLAGYPTTSNMWVIGKSKAQDAKAIMVNGPQFGWYAPAYTYGIGLHGAGYDVTGNTPFAYPGLVFGHNGVISWGSTAGFGDDVDIFAERLSAEKPGYYLHNGKWVKMLSREETITVKNGQAETFTVWRTVHGNILQTDQTTQTAYAKSRAWDGKEVASLLAWTHQMKAKNWQEWTQQAAKQALTINWYYADVNGNIGYHTGAYPDRQSGHDPRLPVPGTGKWDWKGLLPFEMNPKVYNPQSGYIANWNNSPQKDYPASDLFAFLWGGADRVTEIDRLLEQKPRLTADQAWDVIRQTSRQDLNLRLFLPTLQAATSGLTQSDPRRQLVETLTRWDGINLLNDDGKTWQQPGSAILNVWLTSMLKRTVVAAVPMPFDKWYSASGYETTQDGPTGSLNISVGAKILYEAVQGDKSPIPQAVDLFAGKPQQEVVLAALEDTWETLSKRYGNNVSNWKTPAMALTFRANNFFGVPQAAAEETRHQAEYQNRGTENDMIVFSPTTSDRPVLAWDVVAPGQSGFIAPDGTVDKHYEDQLKMYENFGRKSLWLTKQDVEAHKESQEVLHVQR'




aminoAcids = list(translations.keys())
RNA = list(translations.values())

def findRNA(keys, values, protein):
    possible = []
    for i in range(len(values)):
        if values[i] == protein:
            possible.append(keys[i])
    return(possible)

print(findRNA(aminoAcids, RNA, "Z"))


def posRNAParts(protein, dict):
    protein = protein + 'Z'
    keys = list(dict.keys())
    values = list(dict.values())
    possibles = []
    for c in protein:
        possible = findRNA(keys, values, c)
        possibles.append(possible)
    print(possibles)

#print(posDNA(penicillin, translations))




def rnaToProtein(rna,dict):
    codons = []
    proteins = []
    for i in range(0, len(rna)/3):
        codon = rna[i*3:(i*3)+3]
        codons.append(codon)
    for cod in range(len(codons)):
        protein = translations[codons[cod]]
        proteins.append(protein)
    return proteins

output = rnaToProtein('AUGUUUCCGAUGGGGGGCUUCAUGUACCACAUCAGAGACCUGUAUGGCCUCGUCAGAUACUCUGAGACGGGGAUUCUAGAUAAAGCCCCUUUUGACGGAGCCUUCCAGUACGGACGGAACAUCCAUGUAGUUGUGAGGCACUAUCCAACUUGGACCCAUAAAUCUCUUCGGGGAGCCCCUAGAAGUACCAGCGAGCCAAGUCUCAUACUCGUAGCAGAAAUUUCAAGCAUCGCGUCCGAUAUGGUUAUGGGUAAAACGCUGGAUCCGGGCCAACACACGAUGGCGCUAGUUAUUUUCUAUAGGUCUAGAAUCCCGGCAACUCCCAACCGAGUGCAGGGGCAGGUUCAAGGGCAGUGGUGCGGGGAGUUAAAACAGCGUCGGCGACUCGAAUCGUCCGCGCGGACUGCUAUAAGUCCUACUCGUCUCCUAAACGGGGAAAUCCGUUUCUCUGAUUGUCCGAUCCGAUACCUAUCCACCGCUAAGUACACAUCAAAUCGGCUUGCCCUUGUAUCUUAUUUCGAAGGGCACCAGAAUACAAUUAGAGCAACUAUCCAGAGUACUCGAUUGGUGGCACGCGGCUCCUACCUACCAGGUUCAUUGUGGGUAGCCCUGGUUGCCUUCGGAGUCGGCCUUCCAGGACAAUUAAAAGCAAUGGGGAAGAGAGGUCGCGGUUAUUACCUUGAUGUGGUCUUGCGAGCCCUCGAAGGGGGACGUGGGGUGACGGGUCCCCAUGAAAAUACACCAGGGUGCAUUGGACUUCAAAAAUCCCCGUCGGGUGCGACCGCCCCGCGACAGCGAUUAUUGCGCGAAUACGUACGGUUCGGCUGUUGCGAAGAAAUUUCGAUACAUGGAUUUUGCCGACUGGGCAAGCCUCGGAAGAGACACCUUGAACAGCCGCUCCGACGCCGUAUGCCCUCCGUGAGAAAUAAAGGUAUGUCUUAUCGUCCGGGCGGGGAUUGUAACCAUUUGCGGCUGUCGGAUAUAGGAAGCCAGAGUAACACAUUUGAAUUGGAAGACCUGGGUCGCUGGCGAGUCAUUUCUCUGCACUACGUUGGUCAUGCCCCGCUUUGUUUUAGUAAUCUAUACGCACCGCGCUUGAAACGACCGCCAAUCCCUGGGGUAGCGACGAUCAAAUCCCACAGUGGCCGACAGCCGAUAGCGAAGGGCGAACUGUGCUGUGUGACACAUUUGUUGAGAAGGAGCCAUGACUCAUCUGGUGAGCGCUUCAGGUACCUACUCCACGGUGGCGGCCACCACACCCGCAUCUAUCUAACUGUGUCCACCGUAUUUAACGCCGGAUGCGGCAGUGUGUGUCCACGGUGUUGCUCGCCGUUGCUGCAUAAAGACGCGUUCUGUGGUUUGGACGGGCCGGUCAGCCGUAAAGACCGCGUACGUAUUGUCACUCUUCCCGAGUUUGUCUCUGCCUCCAGCCAAAGCGUUUGGGCCGCGGAUAAGAGGUAUCAACCAGAUAGCGUGCAAAUUGAUUAUGCUUGGGGGUAUAGGGUCACGCGUUUUGGAGGCAAUACGUCGAAGACAGGUGUGCCGCCGCCGUUAUUAGAGGAGUCAAAGCCCGUAGGCCAUCCGCUCCAAAACCUGGCCGGGUAUUCGUAUGCCGAAUUGUCUCCCCCAGUGUGCCCCUUAUCCCGUAGGAGUGGGCCGAGUCCCGGGGCCACAGAAUGGAACCCUGGGAAAUCCCAGCCGAUAGGUCAAGAUAAACUUCAAUUACCGUUUUCAAAAUACAUAAGUGGUUGGGGAACAAGCGCAUCCGAUGUAGCUCUGCCGGGAAUGCGCCCGAAUGUCUUCGCUACUCCCAGUACUCGCAGGAUGAGGGUUACGUCUGUGUACGGGCGUAGAUACCAGAUCGCCACGCAUCGGUUCGCUCACCAUUACGCUGAACACUUCCCGCCUGCGGCGUCCUACCAAGUAGGGGUUAUGAUCUCAUUUCUCAGGGAACAUCGGCCGUCUCUCGACUUCAAUGACCGGGUCCAGUCUCCUAUCUUCGUUGACCCGCGCGCCUUGCUGGCCAAGGUCCCUCGGCUGGUGGUGAGAGUACCCGCUGCCAGAUACUACCUUGCUGUCCAAUCCGCACUGAGCCCAGCUAUAACGCUCGCAAGUCCCCCAUUUCGCUGCGAAUGUAAAGCUACAGAUUACAGCGCCUCGAAUUGUCCGCCAGCCACCCGGCAUGUAUACCUAACACUAUCAGCGCGGGUGGGGCAGGAUGGGUAUAUGGUGCCGGGAGGAGAUCAUUGGUCUGCGAAGGAUAAAGUCAAAGUCACCCGAGCGUGCGAAAAGCAGAGUCGUUUGACUCUUGACGGUCCCCGGGGAACUUCAAAUUUCGAGCACCUGGAAUUUACGCGCCCGGAAUGCCGACCGAAUUGCGGCUGUGAUCGACGUGUUCGGUCCCUACCCAGUAUAGUUGUAGAUUUCGUGAUCCUACGGUGCGGAGCUUGCUGGGCAGGGAACAACGAAUUGCCCAGCCUUAGUUUGAUCCAAGUGUUUUCCACUCAUUCAAGAACCCAGCUGUUUAAUUAUUAUGGUUUGGAGAAGCCAUUGCCCCCUCGUUACGUCGCGUCGCCCCCCCGGAGGAUCGCUUGGCUAGCCAUCGCCUACGAUUUUUUAUAUCCCUUCUACGAGUCGGUCCUCAAGGUUUGCGCUGUAACGGGUGACGAACUAACUUGUCAUAGGGAUCCUGCGGGGAUGUCGAAACGUGCUGAGCGGGAAUCGACGAGAGUAUCGGACACCCCUAAUUGUUAUACUUAUAAUUGGCGACCCUCCUACUUACCUAGGCGCACAGGCAGUAUGGGAUUCCCACCGACAGGCGUUCAGUCACUGCACGUAUACUUUAGACUGGUGUUCAAGGAGGACUUUGCCGUUCGGUCACAUAGGUCGGGCUUUGACUCCGGUCAAGUGAUGAUCCCCCCGAGAUUCGUAGACCAAUCUCGUGCCCAUGAUGGCAGCCACUACCCCGCGCUGAAAAAGUUAAUCCCUUACAUCACUCUUGGCCGACUUCGAGACAUUGAAGUGCAGUGCCUGCCCUUCUGCUUCGCAGUUAAGAUGAACCGUAUCCAUGUAACCAACUUGACGUGUGCGCGAGACGAGUCUGGGAAACGCUUUCGGUGUCGGCCAACCAUAUGCUUUCUGUAUAGAUCAGCGACUGAACCACGUCCGACCCCUCACGUUCUUAAUUGUGUAAGUGUCAAACACCAGUCCUGCCAAUCCGGAGCCUCAUCUACCAAAAGCUCACGAUUGCUCUCCACGCGUGGGACUCAGUGGCGCGUUAUGCGCUGGACAGGUGCCAAGCAUAUCUUUUAUCACUCUAUUCAUAAGCUAUGUACGUUAGUGAAACUAUUGUCCAGAGAUAGGUGGUGGGGGGGUGAGUUUGGAGCUGGGGUUGUCCCAUUACUCAACGCGCACCUGGUUAUGGACGUCCGAGCGUUACGUGCUACCCCCUCUCAGAUUUACCUGAGCUCGGGCGAACUUACGUGGUGCUCCACGGAGCGCGCGGGCCAGCUCUUUGUCACCAGCGGGCGUUGUGGGUUGCAGCUAUCCCUACCCGCAAUAGCAAAACACAAUCCGUCCCGAGUCCAUUAUAAUGGCAAACGCGCGUGUAGCCUGGAUUGCGUCGUUGCCCCAACCCGCAUUAUUGUUGUUUGCUUAGAUGACCUACCAAGUAAGAGCCAUGCUCCCGCACGAGCCGCCGUUCUCGUUGAAGGAUGCAUGGUUAUCCGCGGCGAGAAUGCCGAAAUGGCCUUGGUAAUAGCUCAACGGCGCGAGUCUCUGCAAAAUUUGAGAUGGAGGUCUGAGCAGACUCAUAGUAUAAGUGGCAUAUCAACGGGUCGGGCACGGGCUCAGCGUCCAUUUGAAGAUCUUCAGCCCAACGGUACGUGGCUUGAGGCUAGAAUGAUAUCAUCUGAGGAGGGGGCUGGCAACUGCGAUCCACGUCGGUCACGCUAUUGGGCCAUCCCGUGCGCCGGCCUGCAAGGCAUUUGCGGUAAUUCAAGCUUAUCAACCCAAGACGCCCAAGGUUCCAGAUUCAGAACAUCUACCGCUGAUUUUGGAUGGCGUGAAUUAUCGACCGCUAGAGCUACGACACAAACUCGUUUACAAGCAGCAAUUCUCAGAGGGGAUCUUGUCUACCUGCUAAGUAUGGCAUUUGGUCGAGUUCAAAUUACAGAAAUACAACACCUGCAACCGAUAAACGUCGCUCUUUGGGACCUUAUGGAUGGGCUGGAGGCCAGAUUCAAAACCGUAUCAUCAUGUCGAUUUAACCUUGCGUUUUUCUCAAAGCCAAUUGCGUGGGUCUGGGCACAAACCCCCACUUUUAUACCGCUUGCACGACGGUGCGUACUAACUGGCGAGGCUUCGUGUUUAUGUAAAGAAAGGGGCCCCAUUCCAUGCCCGCGGAAUGAAUUUCUUGCAUUAGCUUCAGGAUUACAGACAGGUUGCGCGCCAGUCGUUUCUGCGUUUCCAGGCAAUUGCGCUAAGCUGCACUCCCGCUUGACCAAAGUAUUGAAAGAAAACGUCUCGAGUUUCUCUGUGGACAGACGUUGUCUGAUCGUACCUAACGGGAUAUUUUCUUGGCCUAGGAAGUUCGCGCUAGAUGAUACCGGGGUGCAUACCACUCGCCUAUCCGGAUCAGCAACUACCGCUACAGCUUGGGAGUUACGGUCCUUGGGAAUCAAAAACAUGCCCGUCCCAGCCAUCAAAAGAGUCCAUGUGCGAUUAGGGUUCUUGUUGGCUAAAGAGAAAAUCGGAGAUUGGAUCCUCUUGUACUACCGGGGCGGGUCUAUAGGCGCACACUACUUUAACGGCCACUCUAUGAUGCAUAAAUAUUCGCCGAAUUCUCGGCAUGCUCAAUACAGUCAAGUACGGGUGCCUAAAUCACGAACACAACUGCAGGCUAACUACGCUCAUGCGCGGUCGCUGAGAAACGGUGCCAUCGACAGGUUAUCGAGAAUUUAUGUUCCUCGGCGUGGUCGACUACGACCCGGUCAAGUAUCCCGAGAAGCAAUAUAUGAGCGUGAGACACCUUUCCGACCAUCAGCACGGGACAGCUGUGCUCUUAGACUCGCGCUACUAUACUAUAAGAUAGUAGCGGAUUCCACCGACGCGUUUGGACCAACCUACUUAACCUCGGCCGCGGUACGUACCGGGUGUCAUGGAGGGGCUCGAGAUCCGUGCCGGGUCAAGGGUUACGCGUCCGAUUUCCGGACGAUAGCAAGGUCACCUGCAGCACUCGUAGUGAAAUUAUUUCGGCAGUUCGACGCAGCAGGGGAAAAAAAAGCCUAUUCUCUUGGAGAAUCGGUUGAUACAAUGCAUGCAACCGCUGCAUUUCCUGCUCCGUCCACCGAUCUGACCCAAGCCUUAGUCUGUUUGAUUUCACUAUAUGAUUGCGGGAAUAGCUCCAUUUGGCUGCCGGAGGUUGUCGAGGACUCACCGUUACUUGGAGCGAGUCAAAGCGCCCGUCCUUGCAUCGGGCUAUUGCGGCGUUUCGACGGGGGAUACGUAAUGUUAGAGGGCGGAGACAAUGUGCCUGUUCUGCCGGGCUAUUAUUGUGACACGCGGCGCGCCAAAUGCGUGAUGCCUGCACUGCUAGCCGCAGGUCCUUCGCUCCCGGACCUUGCCUUUCGGCCACAUGGGCCCCCUCGCCCGGGUCUCUUUAAGAGAGUGUUGACGCGGAUCCUUUCGGUUCGGCUUGCGAUCCGCCCCGUGCUGGACUGCACACGACCUUGGAGCUACGUAAGUCGGAAACAUACAUUUACUGGAAGAGGAAGCGAAGCCGCGCUGCCCGUGUUCGGAAUAGUGCUUCGUCAAGUAAAUGACGUAAACGCCGCGGUUGCAGCCACGGCGAAAACGUGCCUGCCCAACAUCGUGAAUACGGGUGCGAACCGCAGCCGGAAUAGGUUUCGCUCGAGGAGGAAAAUUCACCAGGUAAACAAACGACACCAGACCAUUGACCACUAUCCGGUACACAUAGUGACUCGCGAUUGCCUCGCACUAGGGAGGGGAACUGAUGAGCUAGCUCCCUACCAACGUCCUUGUGGCCCAACUGGACGCACCGCAACAGGGGGACCAUACUAUGUCGUGGGUACGGCGGAUAUAGAGCAAAUUGCGCGGCUAGUGUGCCUCUGUUGGUCAUACGUCGUGCUUAGGUCGCACACCGAUCAGAGCUAUUCCCCAUCGUUUGUCAGCUGCUACCCUCUGGAAGUCAGUAGCCCCGCGUCGGAGGUGACCGGCAUUAAGCUGCGGCUCCCUAUAGCGCGAAAUGCGGAAGUGGAGUUGUCCUCGUCUCAAAGUCACCACCACAACUUGCCCUGGACUAUAUUCGACAGGGGCGCGUGGCGGUGGGUACGAGUUUCGGGAUCAUCCCAGCCGGAUGUCACCACGGUAGCUUCGUCCUCUCCGGCUCCCAUGGCCCUGGCGAGGGUAGAUGUUAGGACUGGUGAGGAUCGGAUUCGUUCUCACUCAAAGCCAAGAUCUAACCAUCCCAAGACCUGCAUAAUAAGUCUUCUGCUAACCAUUGUACAGGGGAGAGUUGUGCGGAUAUCCGCCAAUAUUGUUGCUCAGGUGCCUGGAGGUAAGCUUGCGGAACAAAUCGCUUCCGCGCCACGACGUUCUAUAUCCCGCAAGGUCUGGCUAUUGAAACACUGUUCUAGGCCGUUGAGAUAUCUGCAAGCAUACCCUGCCUACCCCCGGAUAGUCAAGUGUUGCCAGUCCACCCUCUCUGACUCGAAUCACGAUCGUCUGUGUCGGAUGAUGAAGGCUUGCGCUGUUCCAUACCAUAAAGAUGCUCAGGGGAACAGGGUCUGGACCGAAGAUUUGACCAUGUCGGGGUUAAUGAAUCUACCAACGCAAAUGCGCUACGGGUGGGAGCGUAUUCGUACUUUACUACUAUUCCUUAGCAGACAGAGAGCGAAUCCUCAUUACCGAGAUAGCUCUACUCACCGGGAUUUUUUUGAAGUAAUUUCUCAGCUACCCAGAGCGUUGCUACGCUUGAUUCACUGCGAUAACUCGCGGCGUUUCGAUGUAAGGGGUCGCGGGCAAGAACGAAUACUCAACCUUUGCAUGCGCAACACUAGGUGCUCUAUGUGGAGUGGCUCGUUAUUAACUUGCCUACAAGGCUUGUGCGCAGGAUACCACGCUGCUCAGCGCACCAAGCGCCCCCUGUGCAUAGCCAGCGUCCCGUGUGGUAACGUUUGUAUACCCUCCUCUUUAUGGAAAAUUCAUUACCACGGGUCUACAGUGUCGCUCCAGGGUUACCCCGUCGCUGAUGUAAUUCCGUUAAGCGUCAGUUUCCGGCUCGGGGACACCUGGCAAUUGGCCUGCACAGUCACUUGGACCUACCCACCUGAACAGAAAAGCCGAUACGACAUCGCAAAUGCUACCUGGAACAUCCUGCCAGUUGCACAACCACGUGGGCGUACACGGUCUGUCGUUCCGUCCUACGGUCAUCACUCUGACGCCGAACCCAGUCACGAUCCACAGGUGUCGCUUGAAGUGUCGGUAACACUCCUGUGUGAGCCUAGUCUAGGUAUAGAAAUUCCCGAUUUCCCUCUUCGUACGAAAACUCUCGCCUCUUCGCGACACAUACAGGUACGAACUUUACGAUACUCAAGCACGUCGGCGAUUGUCUCCGAUCAUCCAAUAACGCGUCGCCAACGAUCCAGGCUCCUGCUGGGCGGCAUUCUUGGGGUUGCCACGAAUACAGUUGUAUCAAGUGCUUUGGGUAGCGCCACACUUCCGCACAGGCGGUUGCGAUGUUCAGCGGCUAGCGUUGUAGUUUCAUGGAGCGCCACAAUCGUCGCACCUCGAGGGCCGCCCGGCCUAUUAGAACACGUUGAAAAGAAUGACGUGCAUUCAGUCGCGGCGUCCCUUGAGGUGACCAUCUCGUAUGCACAACUAGUGCCGGGGUUGAAUGGCGAAGGGAAAAAGUUUUGGAUUGGAGAGGCUUUGUCAUUCGGCCUAUACAAUAACCGGCACCUACCGGAAUUGCGCCCGUACAAUGAUUCUGUACGGAGGAAGGUGAUCUUCGCAAGGCCUCUACCAACGUCAGUUUCAAAUACCGUCUUGUACCUGGCACCACACUAUCCGCAAUUGGCUAGGCAGGGGCCUUACGGCCUUACGAUCGAUUCAACAAGAUUCGGGUGGGCUUGUUUUACUUGGCCUGCGAUUACGAUAGGGCGGCAACCAGACGAAUACCGUAUAAGGGAAACUAGAAGUUUAGUUUGGAGCGAAGAGGACGGUCCCGCCGAGGCCGUGCGUAUAUGUGGUCCUUCUGGUGUCAACAGCUGCAGCCCCGCAGAAUCUUUUCCUGAGCUCAGCCGCAAUCUCAAUCUCAAUUACAGCGACCCGGGACCGUAUUGGAUUGUACUUCUACGCGAACAAGGAGAGGUACUAGAGCUGAUUCGAGCUGUAUGGUUACAUCUGUCUGUUUACGAUAGACAAGGGCGUAUCGUAAAAGACCCGAUGCCUCAAAUUCCAGGUAAGUCCUAUCUUAUUCCGGUUACUGACCCAAAACCAAGGGACAGAACGUAUCAGCAUAAUUCCAUGCGCUGGUCGAUUAGUCGGCGAAAGAGUAGCUGCCGUCCGAGUCAACAACACCCGUUUACUUCGUCAUCAAUCUGUAAGCCUUCGAAUUUUCUACAUGCGAUCGUGUACGGACUGGCCAACAAAACAUUUGCCCAUUACUCACCAUGGGCGAUAGUGUUGUGGAGGCCUAUAAUCACCGUACUCUCUAGGCUCUGGACUUCGGGCUAUAGUUCAAUUCUGACUCCGUUAAUGAGCGCCAGUGUUCGUAGACUAGCGCUGCAGUCUUACAUAAUUCGAGUGUGUUCAUAUAAGUCACUAAUCGCGAUCGCGGUCAGGCUUAUUCGUGCGUUGCAAUGCUUUUGGUGGUCGAAAAAGAGUGGGCGGCGUUUAUCACUAACCCCGGAGGUUAUGAAAAUUGUAAUAUUGCUGUCUCUCGUAGUGUUUUUGCAAGCAUCGGGGCAGCUUAUAUUCCACCGAGCGCGGGACCUAACGAUCGUGUCGAGCUACCAUCUACAUAGUGAAUCCAGGCUACGUCAUUAUGGUCUCUACGUGGUGCUCGAGGUUCGUCGGAAAAUUCAUAGCUAA',translations)
answ = ''
for i in range(len(output)):
    answ = answ + output[i]
#print(answ)





#print(aminoAcids[RNA.index('Stop')])