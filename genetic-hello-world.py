import string
import random

TARGET = "Hello World!"
NUM_SAMPLES = 1000
NUM_SELECTED = 100
LETTERS = string.ascii_letters + ' '

def generate_random_chromosomes():
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
  ''' Randomly select two chromosomes from the samples, then returns the one
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
  ''' Mutate a chromosome by changing a random char in the string by a small
  amount.
  '''
  pass


def main():
  # for each generation
  #   create a selected group with tourny_select_chromo() until we have enough
  #   create a solution group by breeding random chromos in selected group
  #   print the best, worst, and average fitness, and the chromo with best
  #   stop loop if best fitness == 0

  # Create a random sample of chromos
  sample = generate_random_chromosomes()

  generation = 0
  while fitness(sample[0]) != 0:
    # Generate the selected group from the sample
    selected = []
    while len(selected) < NUM_SELECTED:
      selected.append(tourny_select_chromo(sample))

    # Generate the solution group by breeding random chromos from selected
    solution = []
    while len(solution) < NUM_SAMPLES:
      solution.extend((random.choice(selected), random.choice(selected)))
              
    sample = sorted(solution, key = fitness)
    print sample
    # Print useful stats about this generation
    (min, median, max) = map(fitness,
                             [sample[0], sample[len(sample)//2], sample[-1]])
    print("{0} best string: {1}. fitness: best {2}, median {3}, worst {4}" \
            .format(generation, sample[0], min, median, max))
    generation += 1


if __name__ == "__main__":
  main()
