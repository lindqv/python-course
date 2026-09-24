class CPU:
    def __init__(self, model: str):
        self.model = model

class Computer:
    def __init__(self, brand: str, cpu: CPU):
        self.brand = brand
        self.cpu = cpu

cpu = CPU("i7")
computer = Computer("HP", cpu)

print(computer.brand)
print(computer.cpu.model)

# "Computer has-a CPU" makes more sense than "Computer is-a CPU", 
# since a CPU is only one of the parts of a computer.
# Using composition rather than inheritance models the real world relationship more accurately.

# Composition/inheritance pairs:
# 1. Car/engine: has-a (composition)
# 2. Manager/employee: is-a (inheritance)
# 3. Course/teacher: has-a (composition)
# 4. Phone/device: is-a (inheritance)