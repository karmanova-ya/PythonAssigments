class MathList:

    def __init__(self):
        self.list = []

    def append(self, item):
        return self.list.append(item)

    def smallest_value(self):
        return min(self.list)

    def biggest_value(self):
        return max(self.list)

    def sum_of_values(self):
        list_sum = sum(self.list)
        return list_sum

    def average(self):
        average = self.sum_of_values() / len(self.list)
        return average


my_math_list = MathList()

my_math_list.append(10)
my_math_list.append(-25)
my_math_list.append(99)
my_math_list.append(400)

assert my_math_list.smallest_value() == -25
assert my_math_list.biggest_value() == 400
assert my_math_list.sum_of_values() == 484
assert my_math_list.average() == 121.0

print(my_math_list.smallest_value())
print(my_math_list.biggest_value())
print(my_math_list.sum_of_values())
print(my_math_list.average())
