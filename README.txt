# Genetic Algorthm Hello World

## Introduction
	Uses an genetic algorithm to go from a list of random strings to our target.

	1. Creates a list of random strings with generate_random_chromosomes(),
	called 'samples.'

	2. Selects a subset of the samples to create a 'selected' group. First takes
	the top 10% samples (elitism), then uses tourny select to find the
	rest. Tourny select works by selecting two random samples, and using the
	one with the highest fitness score.

	3. Creates a 'solution' group by randomly taking two chromosomes from the
	selected group and breeding (combining) these together. Periodically, a
	mutiation factor is added to this new 'solution.' Repeat this process until
	we have a sufficent number of solutions.

	4. Repeat steps 2 and 3, with each generated solution set becoming the new
	generation of samples. Do this until a generation has a solution of fitness
	of 0 (matches our target).


## Usage
	# Set your parameters (taken from __init__ defaults)
  target = "Hello World!"  # Target string we're going for
  num_samples = 1000       # Have 1000 chromos in the sample group
  num_selected = 100       # Have 100 chromos in the selected group
  mutation_factor = 10     # Mutate every 10 chromosomes
  ghw = genetic_hello_world.GeneticHelloWorld(
	  target, num_samples, num_selected, mutation_factor)
		
	# Run the script until the target is found
  ghw.run()


## Changelog
  v1.00: Initial release.


## License
  Copyright Topher Brown <topher200@gmail.com>, 2010. Released under the MIT 
	license.
