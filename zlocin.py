gen="ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTG" \
    "GAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCG" \
    "CTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCC" \
    "CCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAAT" \
    "TACAGACCTGAA"

crna=gen.find("CCAGCAATCGC")
rjava=gen.find("GCCAGTGCCG")
korencek=gen.find("TTAGCTATCGC")

kvadrat=gen.find("GCCACGG")
krog=gen.find("ACCACAA")
oval=gen.find("AGGCCTCA")

modra=gen.find("TTGTGGTGGC")
zelena=gen.find("GGGAGGTGGC")
rjava_1=gen.find("AAGTAGTGAC")

moski=gen.find("TGCAGGAACTTC")
zenska=gen.find("TGAAGGACCTTC")

belec=gen.find("AAAACCTCA")
crnec=gen.find("CGACTACAG")
azijec=gen.find("CGCGGGCCG")


if crna != -1:
    lasje="crna"
elif rjava != -1:
    lasje="rjava"
elif korencek != -1:
    lasje= "korenckasta"

if kvadrat != -1:
    obraz="kvadratne"
elif krog != -1:
    obraz="okrogle"
elif oval != -1:
    obraz="ovalne"

if modra != -1:
    oci="modre"
elif zelena != -1:
    oci="zelene"
elif rjava_1 != -1:
    oci= "rjave"

if moski != -1:
    spol="moski"
elif zenska != -1:
    spol= "zenska"

if belec != -1:
    rasa=" belec"
elif crnec != -1:
    rasa="crnec"
elif azijec != -1:
    rasa="azijec"


print ("osumljenec je %s %s ima %s oci in %s oblike obraz, barva las je %s" %(spol,rasa,oci,obraz,lasje ))


