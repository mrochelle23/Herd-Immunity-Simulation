class Virus(object):
    def __init__(self, name, repro_rate, mortality_rate):
        if repro_rate < 0 or repro_rate > 1:
            raise ValueError("Invalid reproductive rate. It must be between 0 and 1.")
        if mortality_rate < 0 or mortality_rate > 1:
            raise ValueError("Invalid mortality rate. It must be between 0 and 1.")

        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate

if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3