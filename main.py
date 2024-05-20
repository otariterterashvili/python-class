import csv

class FileHandler:
    def open(self, file_path):
        print("All other file handler", file_path)

class TextFileHandler(FileHandler):
    def open(self, file_path):
        with open(file_path, 'r') as file:
            content = file.readline()
            print(content)

            file.close()
class CSVFileHandler(FileHandler):
    def open(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
            
            file.close()

def files_reader(*args):
    for file in args:
        file_handler = FileHandler()

        if file.endswith(".txt"):
            file_handler = TextFileHandler()
        elif file.endswith(".csv"):
            file_handler = CSVFileHandler()
        
        file_handler.open(file)


# files_reader('temp.txt', 'pandas.csv', 'vip_customers.csv')

class PaymentProcessor():
    def __init__(self, amount):
        self.amount = amount
    def pay(self):
        print("default payment method")


class TBCPaymentProcessor(PaymentProcessor):
    def pay(self):
        print("TBC payment method amount ->", self.amount)

class BOGPaymentProcessor(PaymentProcessor):
    def pay(self):
        print("BOG payment method amount ->", self.amount)


order_bucket = []

order_bucket.append(TBCPaymentProcessor(10.5))
order_bucket.append(BOGPaymentProcessor(20.5))
order_bucket.append(BOGPaymentProcessor(12.80))

order_bucket.append(BOGPaymentProcessor(11.70))
order_bucket.append(TBCPaymentProcessor(9.80))
order_bucket.append(TBCPaymentProcessor(10.30))


for order in order_bucket:
    order.pay()


    
