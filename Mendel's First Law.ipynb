{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b4e497e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.06666666666666667, 0.13333333333333333, 0.13333333333333333, 0.13333333333333333, 0.06666666666666667, 0.13333333333333333, 0.13333333333333333, 0.13333333333333333, 0.06666666666666667]\n",
      "0.9999999999999999\n",
      "[1.0, 1.0, 1.0, 1.0, 0.75, 0.5, 1.0, 0.5, 0.0]\n",
      "0.783333\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Define genotypes as numpy arrays\n",
    "AA = np.array([[0, 0]])\n",
    "Aa = np.array([[0, 1]])\n",
    "aa = np.array([[1, 1]])\n",
    "\n",
    "# Initialize an empty list to store the probabilities of choosing pairs of organisms\n",
    "prob_2_ors = []\n",
    "\n",
    "def probability(k, m, n):\n",
    "    input = [k, m, n]  # List containing the count of each genotype\n",
    "    \n",
    "    # Calculate the probability of choosing pairs of organisms\n",
    "    for gt in range(len(input)):\n",
    "        for gt2 in range(len(input)):\n",
    "            t = k + m + n  # Total number of organisms\n",
    "            if gt != gt2:\n",
    "                # Probability when choosing different types\n",
    "                proba = (input[gt] / t) * (input[gt2] / (t - 1))\n",
    "            else:\n",
    "                # Probability when choosing the same type\n",
    "                proba = (input[gt] / t) * ((input[gt2] - 1) / (t - 1))\n",
    "            prob_2_ors.append(proba)\n",
    "    \n",
    "    # Print the list of probabilities of choosing pairs of organisms\n",
    "    print(prob_2_ors)\n",
    "    # Print the sum of these probabilities\n",
    "    print(sum(prob_2_ors))\n",
    "\n",
    "    # Initialize an empty list to store the probabilities of each genotype combination\n",
    "    prob_each_gen = []\n",
    "\n",
    "    # Calculate the probability of each genotype combination producing offspring with genotype AA\n",
    "    for kg in [AA, Aa, aa]:\n",
    "        for kg2 in [AA, Aa, aa]:\n",
    "            matrix = kg * (kg2.T)  # Cross the genotypes\n",
    "            each_gen = np.sum(matrix == 0) / 4  # Calculate probability of AA offspring\n",
    "            prob_each_gen.append(each_gen)\n",
    "    \n",
    "    # Print the list of probabilities of each genotype combination producing AA offspring\n",
    "    print(prob_each_gen)\n",
    "\n",
    "    # Initialize an empty list to store the final probabilities\n",
    "    list = []\n",
    "\n",
    "    # Calculate the final probability of having offspring with genotype AA\n",
    "    for n in range(0, 9):\n",
    "        probas = prob_2_ors[n] * prob_each_gen[n]\n",
    "        list.append(probas)\n",
    "    \n",
    "    # Return the final probability rounded to 6 decimal places\n",
    "    return round(sum(list), 6)\n",
    "\n",
    "# Call the function with example values\n",
    "print(probability(2, 2, 2))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4bbca9aa",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
