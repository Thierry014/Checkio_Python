class Go_card: 
    def __init__(self, balance = 100):
        self.balance = balance
        self.record = [['Inital balance','','$100']]
       

    def travel(self,money):
        self.balance -= money
        self.generate_record('Ride',f'${money}',f'${self.balance}')
    
    def topup(self,money):
        self.balance += money
        self.generate_record('Top up',f'${money}',f'${self.balance}')

    
    def show_balance(self):
        print(f'Current Balance is ${self.balance}')

    def print_statement(self):
        # add current state
        self.record.append(['Final balance','',f'${self.balance}'])
        # visualize
        for record in self.record:
            print(record[0],record[1],record[2])

    def generate_record(self,type,amount,balance):
        self.record.append([type,amount,balance])
        

    # method accepts user input 
    def swipe(self,query):
        # check query vaild or not

        
        query = query.split(' ')
        # r 12 => ['r',12]  q=>[q]
        if len(query) > 2:
            print('Bad')

        if query[0] == 'r' and query[1].isnumeric():
            self.travel(float(query[1]))
        elif query[0] == 't' and query[1].isnumeric():
            self.topup(float(query[1]))
        elif query[0] == 'b' and len(query) == 1: 
            self.show_balance()
        elif query[0] == 'q' and len(query) == 1:
            self.print_statement()
        else:
            print('Bad')

             




miki = Go_card()
miki.swipe('r 30')
miki.swipe('r 12')
miki.swipe('t 20')
miki.swipe('lol')

miki.swipe('b')
miki.swipe('q')
