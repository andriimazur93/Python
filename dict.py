#T8Q1
# Initialize dictionary "contactinfo" with the values 
# as shown in above examples. Hint: The key is a string 
# literal while the value is a dictionary type.

contactinfo = {}
contactinfo["Tom"] = {'Email':'tom@gmail.com', 'Phone':61234567}
contactinfo["Sally"] = {'Email':'sally@hotmail.com', 'Phone':67654321}

#T8Q5
#In gene expression, mRNA is transcribed from a DNA template. The 4
#nucleotide bases of A, T, C, G corresponds to the U, A, G, C bases
#of the mRNA. Write a function that returns the mRNA transcript given
#the sequence of a DNA strand.

# Use a dictionary to provide the mapping of DNA to RNA bases.
def mRNAtranscription(dna_template):
    dna2rna = {dna_template}
    mRNA = ''
    for base in dna_template:    
        if(base in dna_template.keys):
            mRNA.append (dna_template.values())

    return mRNA

print(mRNAtranscription("ATCGATTG"))
