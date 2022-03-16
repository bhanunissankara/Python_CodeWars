# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
# You function receives one side of the DNA (string, except for Haskell); you need to
# return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

def DNA_strand(dna):
    DNA_Complements = {
        "A" : "T", "T" : "A", "G" : "C", "C" : "G"
    }
    return ''.join(DNA_Complements[i] for i in dna)

print(DNA_strand("AAAA"))
print(DNA_strand("ATTGC"))