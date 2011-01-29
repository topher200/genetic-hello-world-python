#!/usr/bin/python

import string
import random

LETTERS = string.ascii_letters + ' ' + '!' + '?'

class GeneticHelloWorld(object):
  def __init__(self, 
               target = "Hello Python World!",  # Target string we're going for
               num_samples = 1000,  # Have 1000 chromos in the sample group
               num_selected = 100,  # Have 100 chromos in the selected group
               mutation_factor = 10,):  # Mutate every 10 chromosomes
    self.target = target
    self.num_samples = num_samples  
    self.num_selected = num_selected  
    self.mutation_factor = mutation_factor  


  def generate_random_chromosomes(self,):
    ''' Create a list of random chromosomes to seed our alogrithm.
    '''
    chromos = []
    while len(chromos) < self.num_samples:
      new_chromo = ''
      while len(new_chromo) < len(self.target):
        new_chromo += random.choice(LETTERS)
      chromos.append(new_chromo)
    return chromos


  def fitness(self, chromo):
    ''' Fitness of a chromo is the sum of how far each of its charactors is
    from the target string.

    Input string must be the same length as the target string. A string that
    exactly matches the target string has a fitness of 0. Lower fitness is
    better than higher.

    Tests assume that 'Hello World!' is the target string.
    >>> ghw = GeneticHelloWorld()
    >>> ghw.fitness('Hello World!')
    0
    >>> ghw.fitness('Iello World!')
    1
    >>> ghw.fitness('Iallo World!')
    5
    '''
    total_fitness = 0
    for i, char in enumerate(chromo):
      total_fitness += abs(ord(char) - ord(self.target[i]))
    return total_fitness


  def tourny_select_chromo(self, samples):
    ''' Randomly select two chromosomes from the samples, then return the one
    with the best fitness.
    '''
    a = random.choice(samples)
    b = random.choice(samples)
    if self.fitness(a) < self.fitness(b):
      return a
    else:
      return b


  def breed(self, a, b):
    ''' Breed two chromosomes by splicng them in a random spot and combining
    them together to form two new chromos.
    '''
    splice_pos = random.randrange(len(a))
    new_a = a[:splice_pos] + b[splice_pos:]
    new_b = b[:splice_pos] + a[splice_pos:]
    return new_a, new_b


  def mutate(self, chromo):
    ''' Mutate a chromosome by changing a random char to a different letter.
    '''
    pos = random.randrange(len(chromo))
    return random.choice(LETTERS).join( [chromo[:pos], chromo[pos+1:]] )


  def run(self):
    # Create a random sample of chromos
    sample = self.generate_random_chromosomes()

    # Main loop: each generation select a subset of the sample and breed from
    # them.
    generation = -1
    while self.fitness(sample[0]) != 0:
      generation += 1
      # Generate the selected group from sample- take the top 1% of samples
      # and tourny select to generate the rest of selected.
      ten_percent = int(len(sample)*.01)
      selected = sample[:ten_percent]
      while len(selected) < self.num_selected:
        selected.append(self.tourny_select_chromo(sample))

      # Generate the solution group by breeding random chromos from selected
      solution = []
      while len(solution) < self.num_samples:
        solution.extend(self.breed(random.choice(selected),
                                   random.choice(selected)))

      # Apply a mutation to a subset of the solution set
      for i, chromo in enumerate(solution[::self.mutation_factor]):
        solution[i] = self.mutate(solution[i])

      sample = sorted(solution, key = self.fitness)
      # Print useful stats about this generation
      (min, median, max) = map(self.fitness,
                               [sample[0], sample[len(sample)//2], sample[-1]])
      print("{0} best string: {1}. fitness: best {2}, median {3}, worst {4}" \
              .format(generation, sample[0], min, median, max))

    return generation

  
def main():
  ghw = GeneticHelloWorld()
  print "Took {0} generations".format(ghw.run())


if __name__ == "__main__":
  main() 
