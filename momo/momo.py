import time
subsrcibers = [
    {
        'name' : 'Jing Woo' ,
        'mobile' : '0531445623' ,
        'wallet info' : {'wallet_id':'0531445623' , 'pin':'0200'}
    },
    {
        'name' : 'Will Eye',
        'mobile' : '0592009237',
        'wallet info' : {'wallet_id':'0592009237', 'pin':'2323'}
    },
    {
        'name':'Sarah Smith',
        'mobile':'0242464744',
        'wallet info' : {'wallet_id':'0242464744', 'pin':'7771'}
    }
]


balance = 2470.00
account_pin = "0011"

def transfer_money():        
            def momo_user():
                global balance
                receiver_number = input("Enter mobile number: ")
                repeat_receiver_number = input("Enter number again: ")
                # if receiver_number in subsrciber:
                    # print(subsrciber[receiver_number['name']])
                if repeat_receiver_number == receiver_number:
                    wallet_found = False
                    for subsrciber in subsrcibers:
                        if subsrciber['mobile'] == receiver_number:
                            wallet_found = True                           
                            choice = input(f"Confrim Receiver: '{subsrciber['name']}' Press 1 to confirm: ")  
                            if choice == "1":
                                break 
                            else:
                                print("Invalid input. Transaction cancelled")    
                                return               
                        break
                    if not wallet_found:
                        print("Account not found")
                # else:
                #     print("Number mismatch")                     
                    try:
                        amount = float(input("Enter amount: "))
                        if amount <= 0:
                            print("Amount must not be zero!")
                            return
                        if amount >= balance:
                            print("Insufficient funds")
                            return
                    except ValueError:
                        print("Enter a valid amount!")
                                       
                    reference = input("Enter Reference: ")
                    pin_attempts = 0
                    # while True:
                    while pin_attempts < 3:
                        pin = input("Enter pin: ")
                        
                        # pin = input("Enter pin: ")
                        if pin == account_pin:
                            print("processing...")
                            time.sleep(1)
                            print(f"Payment of GHS{amount} has been made to {subsrciber['name']} Reference: {reference}.\nAvailable balance is {balance - amount}. ")
                            return
                        else:
                                pin_attempts += 1
                                if pin_attempts >= 3:
                                    print("Exceede all attempts. Transactioin cancelled")
                                    break
                        print("You entered a wrong pin, try again.")
                            
                else:
                    print("Number Mismatch")
                    
            def non_momo_user():...

            def send_with_care():...

            def favorite():...

            def other_networks():
                at_users = [                       
                        {
                        'name' : 'Dan Dadan' ,
                        'mobile' : '0569292782' ,
                        # 'wallet info' : {'wallet_id':'0569292782' }
                        },
                        {
                        'name' : 'Kwmame Nkrumah' ,
                        'mobile' : '0269092902' ,
                        # 'wallet info' : {'wallet_id':'0509292782' }
                        },
                        {
                        'name' : 'Adwoa Safo' ,
                        'mobile' : '0569119112' ,
                        # 'wallet info' : {'wallet_id':'0509292782' }
                        }
                    ]
                telecel_users = [
                        {
                        'name' : 'Dan Dadan' ,
                        'mobile' : '0509292782' ,
                        'wallet info' : {'wallet_id':'0509292782' }
                        },
                        {
                        'name' : 'Dan Dadan' ,
                        'mobile' : '0509292782' ,
                        'wallet info' : {'wallet_id':'0509292782' }
                        },
                        {
                        'name' : 'Dan Dadan' ,
                        'mobile' : '0509292782' ,
                        'wallet info' : {'wallet_id':'0509292782' }
                        }

                    ]

                def at_user():
                    at_user_number = input("Enter AT number: ")
                    check_number = input("Enter number again: ")   
                    if len(at_user_number) == 10 and at_user_number.startswith(("026","056")) :              
                        if check_number != at_user_number:
                            print('Number mismatch. Try Again')
                        else:    
                            for user in at_users:  
                                    if user['mobile'] == at_user_number:  
                                        # found_user = user
                                        choice = input(f"Confirm Receiver: {user['name']}\nPress 1 to confirm: ")
                                        if choice == "1":
                                            return
                                        else:
                                            print("Invalid input. Transaction cancelled.")
                                        return
                            else:
                                print("user doesn't exist")
                                return
                        try:
                            amount = float(input("Enter amount: "))
                            if amount <= 0:
                                print("Amount must not be zero!")
                                return
                            if amount >= balance:
                                print("Insufficient funds")
                                return
                        except ValueError:
                            print("Enter a valid amount!")
                    else:
                        print("You have entered an non-AT number")

                def telecel_user():
                    telecel_number = input("Enter telecel number: ")
                    repeat_telecel_number = input("Enter number again: ")
                    if repeat_telecel_number != telecel_number:
                        print("Number mismatch. Try Again")
                    else:
                        for user in telecel_users:
                            if user['mobile'] == telecel_number:
                                choice = input(f"Confirm Receiver: {user['name']}\nPress 1 to confirm: ")
                                if choice == 1:
                                    return
                     

                user_input = input("1. AT\n2. Telecel\n3. GhanaPay\n")
                if user_input == "1":
                    at_user()
                elif user_input == "2":
                    telecel_user()
                elif user_input == "3":
                    ghanapay()
                     
                # Sample at_users data structure
                
                

                
                

                
                    
                    # telecel_user()
                def ghanapay():...

                    # ghanapay()
                

            
            def banks():...

            while True:
            # print("\t   Send Money\n\t1. Momo User\n\t2. Non Momo User\n\t3. Send with care\n\t4. Favorite\n\t5. Other Networks\n\t6. Banks\n\t0. Back\n")
                choice = input("\t   Send Money\n\t1. Momo User\n\t2. Non Momo User\n\t3. Send with care\n\t4. Favorite\n\t5. Other Networks\n\t6. Banks\n\t0. Back\n")         
                
                try: 
                        if choice == "1":
                            momo_user()
                        elif choice == "2":
                            non_momo_user()
                        elif choice == "3":
                            send_with_care()
                        elif choice == "4":
                            favorite()
                        elif choice == "5":
                            other_networks()
                        elif choice == "6":
                            banks()
                        elif choice == "0":
                            break
                except ValueError:
                        print("Invalid option!")
                    
                                          
def momo_pay():...
def airtime_bundles():...
def allow_cashout():...
def financial_services():...
def my_wallet():...

user_input = input()
print("\t   Mobile Money\n\t1. Transfer Money\n\t2. MoMoPay & Pay Bill\n\t3. Airtime & Bundles\n\t4. Allow Cashout\n\t5. Financial Services\n\t6. My Wallet")

while True: 
    
    user_input = input()
    if user_input == "1":
        transfer_money()
        break



        
                    
            