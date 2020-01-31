import random


class Machine(object):
    def __init__(self, data):
        self.data = data
        self.shuffled_files = []
        self.generated_files = []
        self.result = []

    def send_data(self, machines, machine_index, single_file):
        machines[machine_index].retrieve_data(single_file)

    def retrieve_data(self, single_file):
        self.shuffled_files.append(single_file)

    def merge_sorted_files(self):
        for f in self.shuffled_files:
            self.result.extend(f)
        self.result = sorted(self.result)

    def sample(self, num_samples):
        steps = (len(self.data) / num_samples) + 1
        return self.data[::steps]

    def integer_to_bucket(self, buckets, integer):
        for index in xrange(len(buckets)):
            if integer <= buckets[index]:
                return index
        return len(buckets)

    def create_files(self, buckets):
        self.generated_files = {}
        for integer in self.data:
            bucket = self.integer_to_bucket(buckets, integer)
            if bucket in self.generated_files:
                self.generated_files[bucket].append(integer)
            else:
                self.generated_files[bucket] = [integer]

    def shuffle_files(self, machines):
        for index, single_file in self.generated_files.iteritems():
            self.send_data(machines, index, single_file)
        

class Driver(object):
    def __init__(self, K):
        self.K = K
        self.machines = []
        
        # Generate some fake data
        for index in xrange(K):
            row = [random.randint(0, 100) for _ in xrange(5)]
            self.machines.append(Machine(row))

    def sort(self):

        samples = []
        for machine in self.machines:
            samples.extend(machine.sample(2))

        sorted_samples = sorted(samples)
        step_size = len(sorted_samples) / self.K
        buckets = sorted_samples[step_size::step_size]

        for machine in self.machines:
            machine.create_files(buckets)
            machine.shuffle_files(self.machines)

        for machine in self.machines:
            machine.merge_sorted_files()
            for r in machine.result:
                print r

Driver(10).sort()

