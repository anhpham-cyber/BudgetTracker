class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True
    
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            amount = f"{item['amount']:.2f}"
            description = f"{item['description'][:23]}"
            items += f"{description:<23}:{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total
    
def create_spend_chart(categories):
    spends = []
    total_spent = 0
    for cat in categories:
        spent = 0
        for item in cat.ledger:
            if item["amount"] < 0:
                spent += -item["amount"]
        spends.append(spent)
        total_spent += spent

    percentages = [int((spent / total_spent) * 100) // 10 * 10 for spent in spends]

    chart = "Persentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for p in percentages:
            if p >= i:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        line = "     "
        for cat in categories:
            if i < len(cat.name):
                line += cat.name[i] + "  "
            else:
                line += "   "
        if i < max_len - 1:
            line += "\n"
        chart += line
    return chart


# example

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(create_spend_chart([ food, clothing]))

    


