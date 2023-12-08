import random
from virus import Virus

class Person(object):
    def __init__(self, _id, is_vaccinated, infection=None):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.infection = infection
        self.is_alive = True

    def did_survive_infection(self):
        if self.infection:
            survival_chance = random.random()
            if survival_chance < self.infection.mortality_rate:
                self.is_alive = False
                return False
            else:
                self.is_vaccinated = True
                self.infection = None
                return True
        else:
            return None
        
if __name__ == "__main__":
    # Define a vaccinated person and check their attributes
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # Create an unvaccinated person and test their attributes
    unvaccinated_person = Person(2, False)
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None

    # Test an infected person. An infected person has an infection/virus
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    infected_person = Person(3, False, virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection == virus

    # Resolve whether the Person survives the infection or not by looping over the people list
    people = []
    did_survive = 0
    did_not_survive = 0

    for i in range(1, 101):  # Make 100 people
        # Make a person with an infection
        person = Person(i, False, virus)

        # Append the person to the people list
        people.append(person)

        # Check survival of an infected person
        survived = person.did_survive_infection()

        # Count the people that survived and did not survive
        if person.is_alive:
            did_survive += 1
        else:
            did_not_survive += 1

    # Print the results
    print(f"People who survived: {did_survive}")
    print(f"People who did not survive: {did_not_survive}")

    # Stretch challenge: Check the infection rate of the virus in a group of uninfected people
    infection_rate = 0.3  # Example infection rate
    infected_people = sum(random.random() < infection_rate for _ in range(100))

    print(f"People infected: {infected_people}")
    print(f"People not infected: {100 - infected_people}")