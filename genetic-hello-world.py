TARGET = "Hello World!"
NUM_SAMPLES = 1000
NUM_SELECTED = 100


class GeneticHelloWorld():
  def generate_random_chromosomes(self):
    pass


  def fitness(self, chromo):
    ''' Fitness of a chromo is the sum of how far each of its charactors is
    from the target string.

    A string that exactly matched the target string has a fitness of 0. Lower
    fitness is better than higher.

    Tests assume that 'Hello World!' is the target string.
    TODO(topher): this restriction could be removed
    >>> ghw = GeneticHelloWorld()
    >>> ghw.fitness('Hello World!')
    0
    >>> ghw.fitness('Iello World!')
    1
    >>> ghw.fitness('Iallo World!')
    5
    >>> ghw.fitness('Hello!')
    Traceback (most recent call last):
    except ValueError: input chromo length doesn't match target
    '''
    pass


  def tourny_select_chromo(self):
    ''' Randomly select two chromosomes from the samples, then returns the one
    with the highest fitness.
    '''
    pass


  def breed(self, a, b):
    ''' Breed two chromosomes by splicng them in a random spot and combining
    them together to form two new chromos.
    '''
    pass


  def mutate(self, chromo):
    ''' Mutate a chromosome by changing a random char in the string by a small
    amount.
    '''
    pass


  def main(self):
    # Create a random sample
    # for each generation
    #   create a selected group with tourny_select_chromo() until we have enough
    #   create a solution group by breeding random chromos in selected group
    #   print the best, worst, and average fitness, and the chromo with best
    #   stop loop if best fitness == 0


    pass
