import sys

class Expenses:
    food = 0
    transport = 0
    gym = 0
    data = ""

    def __init__(self):
        self.food = 0
        self.transport = 0
        self.gym = 0
        self.data = ""

    def print_list_expenses(self):
        self.data = raw_input("{0} - food, {1} - transportation, {2} - gym\n".format(self.food, self.transport, self.gym))

    def print_total(self, quantity, activity, total):
        self.data = raw_input("{0} pesos added to {1} - Total: {2} pesos\n".format(quantity, activity, total))

    def read_file(self):
        file = open("test.txt", "r")
        lines = file.read().splitlines()
        self.food = int(lines[0])
        self.transport = int(lines[1])
        self.gym = int(lines[2])
        file.close()

    def save_file(self):
        file = open("test.txt", "w")
        file.write("{0}\n{1}\n{2}".format(self.food, self.transport, self.gym))
        file.close()

    def process_input(self, exp):
        while (True):
            try:
                list = exp.data.split()
                if exp.data == 'List expenses':
                    exp.print_list_expenses()
                elif exp.data == 'quit':
                    print "Bye!"
                    exp.save_file()
                    break
                else:
                    if len(list) == 3:
                        if list[0] == 'Add' or 'add':
                            try:
                                if list[2] == 'food':
                                    exp.food += int(list[1])
                                    exp.print_total(int(list[1]), list[2], exp.food)
                                elif list[2] == 'transportation':
                                    exp.transport += int(list[1])
                                    exp.print_total(int(list[1]), list[2], exp.transport)
                                elif list[2] == 'gym':
                                    exp.gym += int(list[1])
                                    exp.print_total(int(list[1]), list[2], exp.gym)
                                else:
                                    print "Just 3 options: food, transportation, gym"
                                    break
                            except ValueError, TypeError:
                                print "The 2nd parameter has to be a number"
                                break

                        else:
                            print "You have to write 'Add' in the Beginning"
                            break
                    else:
                        print "You have to write a text: 'Add # food/transportation/gym'"
                        break
            except:
                print "Error: ", sys.exc_info()[0]
                file.close()
                raise

if __name__ == '__main__':
    exp = Expenses()
    exp.read_file()
    exp.data = raw_input("Welcome!\nYou have:\nFood:{0}, Transportation:{1}, Gym:{2}\n".format(exp.food, exp.transport, exp.gym))
    exp.process_input(exp)