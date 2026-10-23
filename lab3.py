class BankAccount:
    def __init__(self , owner , account_number , initial_balance = 0):
        self._owner = owner
        self._account_number = account_number
        self._balance = max(0 , initial_balance)
 
    @property
    def owner(self):
        return self._owner
        
    @property
    def account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def deposit(self , amount):

        if amount <= 0:
            print(f"Ошибка, невозможно положить сумму {amount}")
            return False

        self._balance += amount
        print(f"Успешное зачисление средств: {amount} на баланс, текущий баланс: {self._balance}")

        return True
    
    def snyatAmount(self, amount):
        if amount <= 0:
            print(f"Ошибка, невозможно снять сумму {amount}")
            return False

        if amount > self._balance:
            print(f"Ошибка, невозможно снять сумму {amount}, недостаточно средств на балансе, баланс: {self._balance}")
            return False

        self._balance -= amount
        print(f"Средства {amount} успешно сняты с баланса, новый баланс: {self._balance}")

        return True

    def calculate_income(self):
        return 0

class DebitAccount(BankAccount):
    def __init__(self , owner , account_number , initial_balance = 0):
        super().__init__(owner , account_number , initial_balance)

    def calculate_income(self):
        return 0

class SavingsAccount(BankAccount):
    def __init__(self , owner , account_number , initial_balance = 0 , interest_rate = 0.05):

        #interest_rate — годовая ставка в долях единицы (например, 0.05 = 5%)
        super().__init__(owner, account_number, initial_balance)
        self._interest_rate = interest_rate

    def calculate_income(self):
        income = self._balance * self._interest_rate
        return income

    def apply_interest(self):

        #применяет начисленные проценты к балансу и возвращает сумму дохода
        income = self.calculate_income()

        if income > 0:
            self._balance += income
            print(f"{self._owner}: начислены проценты {income}. Новый баланс: {self._balance}")

        return income

class Bank:

    def __init__(self , name):
        self.name = name
        self._accounts = {}

    def add_account(self , account):

        if account.account_number in self._accounts:
            print("Ошибка, счет с тааким номером уже есть")
            return False

        self._accounts[account.account_number] = account
        print(f"Счет {account.account_number} добавлен для {account.owner}")
        return True

    def get_account(self , account_number):
        return self._accounts.get(account_number)

    def list_accounts(self):
        print(f"\n--- Счета банка '{self.name}' ---")

        if not self._accounts:
            print("Счетов нет.")
            return

        for acc in self._accounts.values():
            print(f"Владелец: {acc.owner}, №: {acc.account_number}, Баланс: {acc.get_balance()}")

        print("---------------------------------\n")

my_bank = Bank("Мой Банк")

# Создаём счета
acc1 = DebitAccount("Иван Иванов", "D001", 1000.0)
acc2 = SavingsAccount("Анна Петрова", "S001", 5000.0, interest_rate=0.07)  # 7% годовых

# Добавляем в банк
my_bank.add_account(acc1)
my_bank.add_account(acc2)

# Операции
acc1.deposit(500)
acc1.snyatAmount(200)

acc2.deposit(1000)
acc2.snyatAmount(300)

# Расчёт и начисление дохода
income_debit = acc1.calculate_income()
print(f"Доход по дебетовому счёту: {income_debit}")

income_savings = acc2.calculate_income()
print(f"Расчётный доход по сберегательному счёту: {income_savings}")
acc2.apply_interest()

# Вывод всех счетов
my_bank.list_accounts()
