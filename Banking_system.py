
import json

class Transection:
    def __init__(self,title,amount,type,note=""):
        self.title=title,
        self.amount=amount,
        self.type=type,
        self.note=note
        
    def display_info(self):
        return f"Transection:\n Expense: {self.title}\n Amount: {self.amount}\n Type: {self.type}\n Note: {self.note}"
    

class Bank:
    def __init__(self):
        self.wallet = []
        
    #add 
    def add_transecation(self,transecation):
        self.wallet.append(transecation)
        
    #remove
    def del_transection(self,title):
        for trans in self.wallet:
            if trans.title == title:
                self.wallet.remove(trans)
                return f"{title} has been removed"
        return f"{title} not found..."
    
        
    #display
    def display(self):
        if not self.wallet:
            return "Your wallet is empty"
        return "\n".join([trans.display_info() for trans in self.wallet])
    #search
    def search_wallet(self,query):
        found=[trans for trans in self.wallet if query.lower() in trans.title.lower() or query.lower() in trans.type.lower()]
        if not found:
            return "Not found"
        return "\n".join([trans.display_info() for trans in found])
        
            
        
    #save
    def save_file(self,filename="wallet.json"):
        data= [{"Expense":transecation.title,"Amount":transecation.amount,"Type":transecation.type,"Note":transecation.note} for transecation in self.wallet ]
        with open(filename, "W") as file:
            json.dump(data,file)
    #load
    def load_file(self,filename="wallet.json"):
        
       try:
           with open(filename,"r") as file:
               data=json.load(file)
               self.wallet=[Transection(trans["title"], trans["amount"], trans["type"], trans["note"]) for trans in data]
       except FileNotFoundError:
           print("We do not have the file...")
        
    def main():
        wallet = Bank()
        while True:
            print("\n=====Sium Banking System=====")
            print("1. Add Transection")
            print("2. Remove Transection")
            print("3. Display Transection")
            print("4. Search Transection")
            print("5. Save Transection")
            print("6. Load Transection")
            print("7. Exit")
            choice=input("Enter your choice(1-7): ")
            
            if choice=="1":
                title=input("Enter the title: ")
                amount=float(input("Enter the amount: "))
                type=input("Expense or Deposit: ")
                transecation=transecation(title,amount,type)
                wallet.add_transecation(transecation)
                print(f"{title} added successfully")
                
            elif choice=="2":
                title=input("Enter the title: ")
                print(wallet.del_transecation(title))
                
            elif choice=="3":
                print(wallet.display())
                
            elif choice=="4":
                query=input("Enter the query: ")
                print(wallet.search_wallet(query))
                
            elif choice=="5":
                filename=input("Enter the filename: ")
                wallet.save_file(filename)
                print("Transection saved successfully")
                
            elif choice=="6":
                filename=input("Enter the filename: ")
                wallet.load_file(filename)
                print("Transection loaded successfully")
                
            elif choice=="7":
                print("Exiting the program.Goodbye")
                break
            else:
                print("Invalid choice")
            
            
if __name__ in "__main__":
    Bank.main()
    
    