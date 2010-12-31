import string
import random

TARGET = "Hello World!"
LETTERS = string.ascii_letters + ' ' + '!'
NUM_SAMPLES = 1000  # Number of chromosomes to generate from breeding
NUM_SELECTED = 100  # Number of chromosomes to select for breeding
MUTATION_FACTOR = 10  # Will perform a mutation every MUTATION_FACTOR solutions

def generate_random_chromosomes():
  ''' Create a list of random chromosomes to seed our alogrithm.
  '''
  chromos = []
  while len(chromos) < NUM_SAMPLES:
    new_chromo = ''
    while len(new_chromo) < len(TARGET):
      new_chromo += random.choice(LETTERS)
    chromos.append(new_chromo)
  return chromos


def fitness(chromo):
  ''' Fitness of a chromo is the sum of how far each of its charactors is
  from the target string.

  A string that exactly matched the target string has a fitness of 0. Lower
  fitness is better than higher.

  Tests assume that 'Hello World!' is the target string.
  >>> fitness('Hello World!')
  0
  >>> fitness('Iello World!')
  1
  >>> fitness('Iallo World!')
  5
  >>> fitness('Hello!')
  Traceback (most recent call last):
    ...
  ValueError: input chromo length doesn't match target
  '''
  if len(chromo) != len(TARGET):
    print chromo
    raise ValueError("input chromo length doesn't match target")

  total_fitness = 0
  for i, char in enumerate(chromo):
    total_fitness += abs(ord(char) - ord(TARGET[i]))
  return total_fitness


def tourny_select_chromo(samples):
  ''' Randomly select two chromosomes from the samples, then return the one
  with the best fitness.
  '''
  a = random.choice(samples)
  b = random.choice(samples)
  if fitness(a) < fitness(b):
    return a
  else:
    return b


def breed(a, b):
  ''' Breed two chromosomes by splicng them in a random spot and combining
  them together to form two new chromos.
  '''
  splice_pos = random.randrange(len(a))
  new_a = a[:splice_pos] + b[splice_pos:]
  new_b = b[:splice_pos] + a[splice_pos:]
  return new_a, new_b


def mutate(chromo):
  ''' Mutate a chromosome by changing a random char to a different letter.
  '''
  pos = random.randrange(len(chromo))
  return random.choice(LETTERS).join( [chromo[:pos], chromo[pos+1:]] )


def main():
  # Create a random sample of chromos
  sample = generate_random_chromosomes()

  # Main loop: each generation select a subset of the sample and breed from them.
  generation = -1
  while fitness(sample[0]) != 0:
    generation += 1
    # Generate the selected group from sample- take the top 10% of samples and
    # tourny select to generate the rest of selected.
    ten_percent = int(len(sample)*.1)
    selected = sample[:ten_percent]
    while len(selected) < NUM_SELECTED:
      selected.append(tourny_select_chromo(sample))

    # Generate the solution group by breeding random chromos from selected
    solution = []
    while len(solution) < NUM_SAMPLES:
      solution.extend(breed(random.choice(selected), random.choice(selected)))

    # Apply a mutation to a subset of the solution set
    for i, chromo in enumerate(solution[::MUTATION_FACTOR]):
      solution[i] = mutate(solution[i])
              
    sample = sorted(solution, key = fitness)
    # Print useful stats about this generation
    (min, median, max) = map(fitness,
                             [sample[0], sample[len(sample)//2], sample[-1]])
    print("{0} best string: {1}. fitness: best {2}, median {3}, worst {4}" \
            .format(generation, sample[0], min, median, max))

  return generation


if __name__ == "__main__":
  print "Took {0} generations".format(main())
