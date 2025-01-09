class Bank:
    def __init__(self, name , user : list, atm :list):
        self.__name = name
        self.__user_lst = user
        self.__atm_lst = atm

    def add_atm(self , atm_lst):
        self.__atm_lst = atm_lst

    def get_atm(self, machine_id):
        for i in self.__atm_lst:
            if machine_id == i.get_machine_id():
                return i
            
    def __str__(self):
        return f'{self.__name} {[i.get_name() for i in self.__user_lst]} {[i.get_machine_id() for i in self.__atm_lst]}'
    
class User:
    def __init__(self, citizen_id: str, name: str):
        self.__citizen_id = citizen_id
        self.__name = name

    def get_citizen_id(self):
        return self.__citizen_id

    def get_name(self):
        return self.__name

    def __str__(self):
        return f'User : {self.__citizen_id} {self.__name} '
    
class Account:
    def __init__(self, account_number: str, owner: User , amount):
        self.__account_number = account_number
        self.__owner = owner
        self.__amount = amount
        self.__transection = []

    def get_acc_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def add_transection(self, trans):
        self.__transection.append(trans)

    def get_transection(self):
        return self.__transection

    def get_owner(self):
        return self.__owner
    
    def get_trans(self):
        return self.__transection
    
    def deposit_amount(self, amount):
        self.__amount += amount

    def withdraw_amount(self, amount):
        self.__amount -= amount

    def tw_amount(self, amount):
        self.__amount -= amount
    
    def td_amount(self, amount):
        self.__amount += amount
    
    def __str__(self):
        return f'Account : {self.__account_number} {self.__owner} {self.__amount} /'

    balance = property(get_balance,set_amount)

class ATMCard:
    def __init__(self, card_number: str, account: Account, pin: str = '1234'):
        self.__card_number = card_number
        self.__account = account
        self.__pin = pin

    def get_card_number(self):
        return self.__card_number

    def get_acc(self):
        return self.__account

    def get_pin(self):
        return self.__pin
    
    def __str__(self):
        return f'ATMCard : {self.__card_number} {self.__account} {self.__pin} /'

class ATMMachine:
    def __init__(self, machine_id: str, initial_amount: float = 1000000):
        self.__machine_id = machine_id
        self.__initial_amount = initial_amount
    
    def insert_card(self , card : str ,pin :str):
        for i in lst_card: #obj card
            if i.get_card_number() == card:
                if i.get_pin() != pin:
                    return "Invalid PIN"
        
                return i.get_acc()# return inst account 
        return None
        
    def deposit(self, account : Account , amount : int):
        if amount <= 0:
            return 'Error'
        
        if isinstance(account , Account):
            after_amount = account.balance
            account.deposit_amount(amount)
            self.__initial_amount += amount
            trans = Transection('D', amount , self.__machine_id ,after_amount )
            account.add_transection(trans)
            return 'Success'
        return 'Error'
        
    def withdraw(self , account : Account , amount : int = 0):
        if amount <= 0 or amount >40000:
            return 'Error'
        
        if isinstance(account , Account) and self.__initial_amount >= amount and account.balance > amount:
            after_amount = account.balance
            account.withdraw_amount(amount)
            self.__initial_amount -= amount
            trans = Transection('W', amount , self.__machine_id , after_amount)
            account.add_transection(trans)
            return 'Success'
        return 'Error'
    
    def transfer(self, account : Account , account2 : Account , amount : int = 0):
        if isinstance(account, Account) and isinstance(account2,Account):
            if account.balance > amount  and amount > 0:
                after_amount = account.balance
                after_amount2 = account2.balance
                account.tw_amount(amount)
                account2.td_amount(amount)
                trans = Transection('TW', amount , self.__machine_id , after_amount)
                account.add_transection(trans)
                trans = Transection('TD', amount , self.__machine_id , after_amount2)
                account2.add_transection(trans)
                return 'Success'
            return 'Error'
        
    def get_machine_id(self):
        return self.__machine_id

    def get_balance(self):
        return self.__initial_amount
    def __str__(self):
        return f'ATMMachine : {self.__machine_id} {self.__initial_amount} / '
    
class Transection:
    def __init__(self, Type : str , amount : int , id_atm : str , after_amount : int):
        self.__type = Type
        self.__amount = amount
        self.__id_atm = id_atm
        self.__after_amount = after_amount
        
    def get_type(self):
        return self.__type
    def get_amount(self):
        return self.__amount
    def get_atm(self):
        return self.__id_atm
    def get_after_amount(self):
        return self.__after_amount
    
    def __str__(self):
        return f'{self.__type}-ATM:{self.__id_atm}-{self.__amount}-{self.__after_amount}'
        
    # Class Code

##################################################################################


# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี,  หมายเลข ATM, จำนวนเงิน]}
user ={'1-1101-12345-05-0':['Harry Potter','1234567890',20000,'12345'],
       '1-1101-12345-06-0':['Hermione Jean Granger','0987654321',1000,'12346']}

atm ={'1001':1000000,'1002':200000}

# TODO 1 : จากข้อมูลใน user ให้สร้าง instance โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง

lst_usr = []
lst_acc = []
lst_card = []
lst_machine = []
lst_transection = []
def init_usr():
    for i in user.items():
        usr = User(i[0],i[1][0])
        acc = Account(i[1][1],usr,i[1][2])
        card = ATMCard(i[1][3],acc)
        
        lst_usr.append(usr)
        lst_acc.append(acc)
        lst_card.append(card)
    
def init_machine():
    for i in atm.items():
        machine = ATMMachine(i[0],i[1])
        lst_machine.append(machine)

init_usr()
init_machine()
bank = Bank('KMITL BANK', lst_usr , lst_machine)
print()
print(bank)
# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) atm_card เป็นหมายเลขของ atm_card
# TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM

# inst = lst_machine[0].insert_card(bank,'12345')
# print(inst)

# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0
# print('Deposit')
# print('Before')
# print(lst_acc[0])
# print(lst_machine[0].deposit(lst_acc[0],10000))
# id1 = lst_acc[0]
# print(id1.get_transection()[0])
# print('After')
# print(id1)
# print(lst_machine[0])
# print('-----------------')

#TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี

# print('Withdraw')
# print('Before')
# print(lst_acc[0])
# print(lst_machine[0].withdraw(lst_acc[0],20))
# print(id1.get_transection()[1])
# print('After')
# id1 = lst_acc[0]
# print(id1)
# print(lst_machine[0])
# print('-----------------')

#TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี

# print('transfer')
# print('Before')
# print(lst_acc[0])
# print(lst_acc[1])
# print(lst_machine[0].transfer(lst_acc[0],lst_acc[1],2000))
# print(id1.get_transection()[2])
# print('After')
# print(lst_acc[0])
# print(lst_acc[1])
# print(lst_machine[0])

# TEST 

atm1 = bank.get_atm('1001')
atm2 = bank.get_atm('1002')
harry_card = lst_card[0].get_card_number() #12345
hermione_card  = lst_card[1].get_card_number() #12346

# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success
harry_acc = atm1.insert_card(harry_card , '1234') #return acc
print(f"Ans : {harry_card}, {harry_acc.get_acc_number()}, {'Success' if harry_acc != None else 'Error' }")
print("-------------------------")

# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
hermione_acc = atm2.insert_card(hermione_card , '1234')
print(f"Hermione account before test : {hermione_acc.get_balance()}")
atm2.deposit(hermione_acc , 1000 )
print(f"Hermione account after test : {hermione_acc.get_balance( )}")
print("-------------------------")

# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error
print(atm2.deposit(hermione_acc , -1 ))
print("-------------------------")

# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500
hermione_acc = atm2.insert_card(hermione_card , '1234')
print(f"Hermione account before test : {hermione_acc.get_balance()}")
atm2.withdraw(hermione_acc , 500 )
print(f"Hermione account after test : {hermione_acc.get_balance( )}")
print("-------------------------")

# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error
print(atm2.withdraw(hermione_acc , 2000 ))
print("-------------------------")

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500
harry_be = harry_acc.get_balance()
hero_be = hermione_acc.get_balance()
result = atm2.transfer(harry_acc ,hermione_acc , 10000)
print(f"Hermione account before test : {harry_be}")
print(f"Hermione account after test : {harry_acc.get_balance( )}")
print(f"Hermione account before test : {hero_be}")
print(f"Hermione account after test : {hermione_acc.get_balance( )}")
#print(result)
print("-------------------------")

# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : TD-ATM:1002-10000-11500
for i in lst_acc:
    if i.get_owner() == hermione_acc.get_owner():
        for j in i.get_trans():
            print(f"Hermione transaction : {j}")
print("-------------------------")

# Test case #8 : ทดสอบการใส่ PIN ไม่ถูกต้อง 
# ให้เรียกใช้ method ที่ทำการ insert card และตรวจสอบ PIN
atm_machine = bank.get_atm('1001')
test_result = atm_machine.insert_card('12345', '9999')  # ใส่ PIN ผิด
# ผลที่คาดหวัง
# Invalid PIN
print(test_result)
print("-------------------------")

# Test case #9 : ทดสอบการถอนเงินเกินวงเงินต่อวัน (40,000 บาท)
atm_machine = bank.get_atm('1001')
account = atm_machine.insert_card('12345', '1234')  # PIN ถูกต้อง
harry_balance_before = account.get_balance()
print(f"Harry account before test: {harry_balance_before}")
print("Attempting to withdraw 45,000 baht...")
result = atm_machine.withdraw(account, 45000)
print(f"Expected result: Exceeds daily withdrawal limit of 40,000 baht")
print(f"Actual result: {result}")
print(f"Harry account after test: {account.get_balance()}")
print("-------------------------")

# Test case #10 : ทดสอบการถอนเงินเมื่อเงินในตู้ ATM ไม่พอ
atm_machine = bank.get_atm('1002')  # สมมติว่าตู้ที่ 2 มีเงินเหลือ 200,000 บาท
account = atm_machine.insert_card('12345', '1234')
print("Test case #10 : Test withdrawal when ATM has insufficient funds")
print(f"ATM machine balance before: {atm_machine.get_balance()}")
print("Attempting to withdraw 250,000 baht...")
result = atm_machine.withdraw(account, 250000)
print(f"Expected result: ATM has insufficient funds")
print(f"Actual result: {result}")
print(f"ATM machine balance after: {atm_machine.get_balance()}")
print("-------------------------")




