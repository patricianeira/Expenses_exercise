import sys
import os

class Expenses:

    def __init__(self):
        self.path_file = ""
        self.process_flag = True
        self.concepts = []
        self.quantities = []
        self.options = {'LIST': self.print_expenses, 'QUIT': self.save_file, 'ADD': self.add_expense, 'DELETE': self.delete_expense}

    def print_expenses(self, *args):
        for i in range(len(self.concepts)):
            print self.quantities[i], self.concepts[i]

    def print_total(self, operation, quantity, activity, total):
        print "{0} pesos {1} to {2} - Total: {3} pesos\n".format(quantity, operation, activity, total)

    def read_expenses_file(self):
        if os.stat(self.path_file).st_size != 0:
            with open(self.path_file, 'r') as expenses_file:
                lines = expenses_file.read().splitlines()
                self.concepts = lines[0].split(",")
                self.quantities = lines[1].split(",")
        else:
            print "The file is empty"

    def save_file(self, *args):
        with open(self.path_file, 'w') as expenses_file:
            for i in range(len(self.concepts)):
                if i < (len(self.concepts)-1):
                    expenses_file.write("{0},".format(self.concepts[i]))
                else:
                    expenses_file.write("{0}\n".format(self.concepts[i]))
            for i in range(len(self.quantities)):
                if i < (len(self.quantities)-1):
                    expenses_file.write("{0},".format(self.quantities[i]))
                else:
                    expenses_file.write("{0}".format(self.quantities[i]))
        print "Bye!"
        self.process_flag = False

    def add_expense(self, quantity, concept):
        if(quantity.isdigit()):
            if concept in self.concepts:
                concept_position = self.concepts.index(concept)
                self.quantities[concept_position] = int(self.quantities[concept_position]) + int(quantity)
                self.print_total("Added", int(quantity), concept, self.quantities[concept_position])
            else:
                print "The concept is incorrect"
        else:
            print("The 2nd parameter has to be a number")

    def delete_expense(self, quantity, concept):
        if(quantity.isdigit()):
            if concept in self.concepts:
                concept_position = self.concepts.index(concept)
                self.quantities[concept_position] = int(self.quantities[concept_position]) - int(quantity)
                self.print_total("Deleted", int(quantity), concept, self.quantities[concept_position])
            else:
                print "The concept is incorrect"
        else:
            print("The 2nd parameter has to be a number")

    def process_input(self, user_input):
        input_list = user_input.split()
        option, arguments = input_list[0], input_list[1:]
        if input_list[0] in self.options:
            self.options[option](*arguments)
        else:
            print "Not an option"

if __name__ == '__main__':
    try:
        exp = Expenses()
        exp.path_file = "test.txt"
        exp.read_expenses_file()
        print "Welcome!\nYou have:"
        exp.print_expenses()
        while(exp.process_flag):
            user_input = raw_input("= ")
            exp.process_input(user_input.upper())
    except:
        print "Error: ", sys.exc_info()[0]
        raise