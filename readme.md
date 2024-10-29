# Herd Immunity Simulation

This project simulates the spread of a virus in a population and the effects of vaccination on herd immunity. It logs various statistics throughout the simulation, including infection rates, deaths, and vaccination progress.

## Files

- **logger.py**: Handles logging of simulation data, including the start of the simulation, time steps, and final statistics.
- **person.py**: Defines the `Person` class, representing individuals in the simulation, including their vaccination status and infection state.
- **simulation.py**: Contains the main simulation logic, creating the population, running the simulation, and logging the results.
- **virus.py**: Defines the `Virus` class, representing the virus's characteristics, such as reproduction and mortality rates.
- **simulation_log.txt**: Contains a log of the simulation run, including population statistics at various time steps.
- **.gitignore**: Specifies files and directories to be ignored by Git.

## Requirements

To run this simulation, you need Python 3 installed on your machine.

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/Herd-immunity-Simulation.git
   cd Herd-immunity-Simulation
   ```

2. **Run the simulation:**

   You can run the simulation by providing the required parameters. The command format is:

   ```bash
   python simulation.py <population_size> <vaccination_percentage> <virus_name> <mortality_rate> <reproduction_rate> <initial_infected>
   ```

   For example:

   ```bash
   python simulation.py 100000 0.9 Ebola 0.7 0.25 1
   ```

   This command simulates a population of 100,000 with 90% vaccination against the Ebola virus, which has a mortality rate of 70% and a reproduction rate of 25%, starting with 1 infected individual.

3. **View the results:**

   After running the simulation, the results will be logged in `simulation_log.txt`. You can open this file to review the statistics of the simulation.

## Classes

- **Logger**: Manages the logging of simulation events.
- **Person**: Represents individuals in the population, tracks their vaccination status and infection.
- **Virus**: Represents the virus's characteristics.
- **Simulation**: Manages the simulation process, including population creation and time steps.

## Example Log

A sample entry in `simulation_log.txt` looks like this:

```
Population Size: 100000 | Vaccination Percentage: 0.9 | Virus: Ebola | Mortality Rate: 0.7 | Reproduction Rate: 0.25

Time Step 1
New Infections: 24 | New Deaths: 17 | Current Living Population: 99983
Total Deaths: 17  Total Vaccinated: 90007

...
Simulation End Stats:
Total Population: 93312
Total Infected: 6603
Total Deaths: 11495
Total Vaccinated: 94655
```
