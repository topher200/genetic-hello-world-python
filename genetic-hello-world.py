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
    pass


  def breed(self, a, b):
    pass


  def mutate(self, chromo):
    pass
