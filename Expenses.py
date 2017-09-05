import sys
import os

class Expenses:

    def __init__(self):
        self.food = 0
        self.transport = 0
        self.gym = 0
        self.input = ""
        self.proces_flag = True

    def print_list_expenses(self):
        print "{0} - food, {1} - transportation, {2} - gym\n".format(self.food, self.transport, self.gym)

    def print_total(self, operation, quantity, activity, total):
        print "{0} pesos {1} to {2} - Total: {3} pesos\n".format(quantity, operation, activity, total)

    def print_options(self):
        pass

    def read_file(self, path_file):
        #with open(...)
        if(os.path.getsize(path_file)) > 0:
            file = open(path_file, "r")
            lines = file.read().splitlines()
            self.food = int(lines[0])
            self.transport = int(lines[1])
            self.gym = int(lines[2])
            file.close()

    def save_file(self, path_file):
        file = open(path_file, "w")
        file.write("{0}\n{1}\n{2}".format(self.food, self.transport, self.gym))
        file.close()
        print "Bye!"

    # mandar variables sin lista
    def add_expense(self, operation, input_list):
        if(input_list[1].isdigit()):
            if input_list[2] == 'food':
                self.food += int(input_list[1])
                self.print_total(operation, int(input_list[1]), input_list[2], self.food)
            elif input_list[2] == 'transportation':
                self.transport += int(input_list[1])
                self.print_total(operation, int(input_list[1]), input_list[2], self.transport)
            elif input_list[2] == 'gym':
                self.gym += int(input_list[1])
                self.print_total(operation, int(input_list[1]), input_list[2], self.gym)
            else:
                print "Just 3 options: food, transportation, gym"

    def delete_expense(self, operation, input_list):
        if input_list[2] == 'food':
            self.food -= int(input_list[1])
            self.print_total(operation, int(input_list[1]), input_list[2], self.food)
        elif input_list[2] == 'transportation':
            self.transport -= int(input_list[1])
            self.print_total(operation, int(input_list[1]), input_list[2], self.transport)
        elif input_list[2] == 'gym':
            self.gym -= int(input_list[1])
            self.print_total(operation, int(input_list[1]), input_list[2], self.gym)
        else:
            print "Just 3 options: food, transportation, gym"

    def process_input(self, input_list):
        if self.input == 'List expenses':
            self.print_list_expenses()
        elif self.input == 'quit':
            self.save_file("test.txt")
            self.proces_flag = False
        else:
            if len(input_list) == 3:
                if input_list[0] == 'Add':
                   self.add_expense(input_list[0], input_list)
                elif input_list[0] == 'Delete':
                    self.delete_expense(input_list[0], input_list)
                else:
                    print "You have to write 'Add','delete', 'edit' in the Beginning"
            else:
                print "You have to write a text: 'Add # food/transportation/gym'"

if __name__ == '__main__':
    try:
        exp = Expenses()
        exp.read_file("test.txt")
        print "Welcome!\nYou have:\nFood:{0}, Transportation:{1}, Gym:{2} ".format(exp.food, exp.transport, exp.gym)
        while(exp.proces_flag):
            exp.input = raw_input("= ")
            input_list = exp.input.split()
            exp.process_input(input_list)
    except:
        print "Error: ", sys.exc_info()[0]
        raise

    #kargs
    #*args