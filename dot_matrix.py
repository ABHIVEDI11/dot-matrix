seq1 = "GTGATGCTGATGCTAGTCG"
seq2 = "GTGATGCTGATGCCCATCG"
plot = ''

for i in range(len(seq1)):
    base1 = seq1[i]
    for j in range(len(seq2)):
        base2 = seq2[j]
        if base1 == base2:
            plot += " * "
        else:
            plot += " _ "
    plot += "\n"

print(plot)
