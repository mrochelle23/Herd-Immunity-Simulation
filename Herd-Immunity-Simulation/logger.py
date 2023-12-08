class Logger:
    def __init__(self, file_name):
        self.file_name = file_name
        self.log_file = open(self.file_name, 'w')

    def log_simulation_start(self, pop_size, vacc_percentage, virus_name, mortality_rate, repro_rate):
        self.log_file.write(f"Population Size: {pop_size} | Vaccination Percentage: {vacc_percentage} | Virus: {virus_name} | Mortality Rate: {mortality_rate} | Reproduction Rate: {repro_rate}\n\n")

    def log_time_step(self, step_number, new_infections, new_deaths, current_population, total_deaths, total_vaccinated):
        self.log_file.write(f"Time Step {step_number}\n")
        self.log_file.write(f"New Infections: {new_infections} | New Deaths: {new_deaths} | Current Living Population: {current_population}\n")
        self.log_file.write(f"Total Deaths: {total_deaths}  Total Vaccinated: {total_vaccinated}\n\n")

    def log_final_stats(self, total_pop, total_infected, total_deaths, total_vaccinated):
        self.log_file.write("Simulation End Stats:\n")
        self.log_file.write(f"Total Population: {total_pop}\n")
        self.log_file.write(f"Total Infected: {total_infected}\n")
        self.log_file.write(f"Total Deaths: {total_deaths}\n")
        self.log_file.write(f"Total Vaccinated: {total_vaccinated}\n\n")

    def close(self):
        self.log_file.close()