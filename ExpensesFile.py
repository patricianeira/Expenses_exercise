
class ExpensesFile:
    def read_expenses_file(self):
        with open(self.path_file, 'r') as expenses_file:
            lines = expenses_file.read().splitlines()
            self.concepts = lines[0].split(",")
            self.quantities = lines[1].split(",")

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