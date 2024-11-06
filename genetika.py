import random

def generate_population(pop_size, chromosome_length):
  """
  Membuat populasi awal berisi individu acak.

  Args:
    pop_size: Ukuran populasi (jumlah individu).
    chromosome_length: Panjang kromosom (jumlah gen).

  Returns:
    Daftar berisi individu-individu dalam populasi.
  """
  population = []
  for _ in range(pop_size):
    chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
    population.append(chromosome)
  return population

def fitness_function(chromosome):
  """
  Fungsi kebugaran untuk mengevaluasi individu.

  Args:
    chromosome: Daftar berisi gen-gen individu.

  Returns:
    Nilai kebugaran (semakin tinggi semakin baik).
  """
  # Contoh fungsi kebugaran: menghitung jumlah 1 dalam kromosom
  fitness = sum(chromosome)
  return fitness

def selection(population, fitnesses, k):
  """
  Memilih individu terbaik untuk crossover berdasarkan fungsi kebugaran.

  Args:
    population: Daftar berisi individu-individu dalam populasi.
    fitnesses: Daftar berisi nilai kebugaran setiap individu.
    k: Jumlah individu terbaik yang dipilih.

  Returns:
    Daftar berisi individu terbaik yang dipilih.
  """
  selected_indices = random.sample(range(len(population)), k)
  selected_individuals = [population[i] for i in selected_indices]
  return selected_individuals

def crossover(selected_individuals, crossover_rate):
  """
  Melakukan crossover pada individu terbaik untuk menghasilkan keturunan baru.

  Args:
    selected_individuals: Daftar berisi individu terbaik yang dipilih.
    crossover_rate: Probabilitas terjadinya crossover.

  Returns:
    Daftar berisi individu hasil crossover.
  """
  offspring = []
  for i in range(0, len(selected_individuals), 2):
    parent1 = selected_individuals[i]
    parent2 = selected_individuals[i + 1]
    if random.random() < crossover_rate:
      # Menentukan titik crossover acak
      crossover_point = random.randint(1, len(parent1) - 1)
      # Membentuk offspring dengan menggabungkan gen dari parent
      offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
      offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    else:
      # Tidak terjadi crossover, salin parent
      offspring1 = parent1
      offspring2 = parent2
    offspring.append(offspring1)
    offspring.append(offspring2)
  return offspring

def mutation(population, mutation_rate):
  """
  Melakukan mutasi pada individu dalam populasi.

  Args:
    population: Daftar berisi individu-individu dalam populasi.
    mutation_rate: Probabilitas terjadinya mutasi.

  Returns:
    Daftar berisi individu hasil mutasi.
  """
  mutated_population = []
  for chromosome in population:
    mutated_chromosome = chromosome.copy()
    for i, gene in enumerate(mutated_chromosome):
      if random.random() < mutation_rate:
        mutated_chromosome[i] = 1 - gene
    mutated_population.append(mutated_chromosome)
  return mutated_population

def main():
  # Parameter algoritma
  pop_size = 100  # Ukuran populasi
  chromosome_length = 10  # Panjang kromosom
  generations = 100  # Jumlah generasi
  crossover_rate = 0.8  # Probabilitas crossover
  mutation_rate = 0.01  # Probabilitas mutasi

  # Memulai populasi awal
  population = generate_population(pop_size, chromosome_length)

  # Melakukan iterasi evolusi
  for generation in range(generations):
    # Menghitung nilai kebugaran setiap individu
    fitnesses = [fitness_function(chromosome) for chromosome in population]

    # Memilih individu terbaik
    selected_individuals = selection(population, fitnesses, 2)

    # Melakukan crossover
    offspring = crossover(selected_individuals, crossover_rate)

    # Melakukan mutasi
    mutated_population = mutation
