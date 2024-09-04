# Given: Two positive integers k (k≤7) and N (N≤2k). 
# In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. 
# Tom has two children in the 1st generation, each of whom has two children, and so on. 
# Each organism always mates with an organism having genotype Aa Bb.

#Return: The probability that at least N
#Aa Bb organisms will belong to the k -th generation of Tom's family tree (don't count the Aa Bb mates at each level). 
#Assume that Mendel's second law holds for the factors.
########################################################################################################################

# Read the file (formated in txt)
with open("D:/BO/DA-08/.ipynb_checkpoints/Rosalind_practice/rosalind_lia.txt", "r") as file:
    data = file.read().split(' ')

#Make factorial function for calculating combination
def factorial(value):
    if value <= 0:
        return 1
    return value * factorial(value - 1)
#print(factorial(4))

# Calculate probability of at least N organism AaBb which belongs to kth-generation
prop_list = []
def probability(k,N):
    organism_each_generation = 2**k
    prob_AaBb = 0.25
    # While-loop calculates probability based on Binomial Distribution Formula
    while N <= organism_each_generation:
       com = factorial(organism_each_generation)/(factorial(N)*factorial(organism_each_generation-N)) 
       prob = com * (prob_AaBb**N) * ((1-prob_AaBb)**(organism_each_generation-N))
       prop_list.append(prob)
       N += 1
    total = round(sum(prop_list),3)
    return total

#Print the probability
print(probability(int(data[0]),int(data[1])))
