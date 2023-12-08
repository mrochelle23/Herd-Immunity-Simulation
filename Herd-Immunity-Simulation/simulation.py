import random, sys
from person import Person
from virus import Virus
from logger import Logger

class Simulation:
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.logger = Logger("simulation_log.txt")
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.population = self._create_population()
        self.current_step = 0
        self.total_interactions = 0
        self.total_deaths = 0
        self.total_vaccinated = len([p for p in self.population if p.is_vaccinated])
        self.total_infected = len([p for p in self.population if p.infection is not None])
        self.logger.log_simulation_start(pop_size, vacc_percentage, virus.name, virus.mortality_rate, virus.repro_rate)

    def _create_population(self):
        population = []
        num_vaccinated = int(self.pop_size * self.vacc_percentage)
        num_infected = self.initial_infected

        for i in range(self.pop_size):
            if num_vaccinated:
                population.append(Person(i, True))
                num_vaccinated -= 1
            elif num_infected:
                population.append(Person(i, False, self.virus))
                num_infected -= 1
            else:
                population.append(Person(i, False))

        random.shuffle(population)
        return population

    def _simulation_should_continue(self):
        living = len([p for p in self.population if p.is_alive])
        return living > 0 and self.total_vaccinated < living

    def run(self):
        while self._simulation_should_continue():
            new_infections, new_deaths = self.time_step()
            self.current_step += 1
            self.total_deaths += new_deaths
            self.logger.log_time_step(self.current_step, new_infections, new_deaths, self.current_population(), self.total_deaths, self.total_vaccinated)
        
        self.logger.log_final_stats(self.pop_size, self.total_infected, self.total_deaths, self.total_vaccinated)
        self.logger.close()

    def time_step(self):
        new_infections = 0
        new_deaths = 0
        interactions = 0

        for person in self.population:
            if person.infection:
                new_infections += 1
                self.total_infected = new_infections
                for _ in range(100):
                    random_person = random.choice(self.population)
                    if self.interaction(person, random_person):
                        interactions += 1

                survived = person.did_survive_infection()
                if not survived:
                    new_deaths += 1
                else:
                    self.total_vaccinated += 1
                    self.total_vaccinated = min(self.total_vaccinated, self.pop_size)

        self.pop_size = self.current_population()
        self.total_interactions += interactions
        return new_infections, new_deaths

    def interaction(self, infected_person, random_person):
        if not random_person.is_vaccinated and random_person.infection is None:
            if random.random() < self.virus.repro_rate:
                random_person.infection = self.virus
                return True
        return False

    def current_population(self):
        return len([p for p in self.population if p.is_alive])
    def percentage_infected(self):
        infected = len([p for p in self.population if p.infection is not None])
        return (infected / self.pop_size) * 100

    def percentage_deaths(self):
        return (self.total_deaths / self.pop_size) * 100

    def lives_saved(self):
        saved = len([p for p in self.population if p.infection is not None])
        return saved

if __name__ == "__main__":

    population_size = int(sys.argv[1])
    vaccination_percentage = float(sys.argv[2])
    virus_name = sys.argv[3]
    mortality_rate = float(sys.argv[4])
    reproduction_rate = float(sys.argv[5])
    initial_infected = int(sys.argv[6])

    virus = Virus(virus_name, reproduction_rate, mortality_rate)
    sim = Simulation(virus, population_size, vaccination_percentage, initial_infected)
    sim.run()
