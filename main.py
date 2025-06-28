from module import Transaction

'''
main.py functioned as a simple main menu for self service super cashier
it takes user input to run Transaction class from module.py
it also has a function to make sure to catch any error from user
making sure the program works as intended
'''
print('-'*40)
print('')
print('Welcome to Pacmann Super Cashier'.center(40))
print('')
print('-'*40)

# Initiating Transaction Class
transaction123 = Transaction()
# cart_has_item = False : program just launched or the cart is empty
cart_has_item = False


def _hold(message = ''):
    ''''
    this function used to make a holder to halt the program
    '''
    print('\n'*1)
    holder = input(f"{message}Please press anything to continue")
    print('\n'*1)

def add_item():
    '''
    This contain all the code necesarry for adding item
    '''
    print('Add Menu'.center(40,'-'), end= '\n')
    item = input('Please Add Item Name (str) : ')
    item_list = [i['Item Name'] for i in transaction123.cart]
    
    #Checking for duplicate
    if cart_has_item == True:
        while item in item_list:
            item = input('Duplicate found, please input differently : ')

    #Making sure qty is an int to prevent ValueError
    qty = input('Please Add Item Quantity (int) : ')
    while not qty.isdigit():
        qty = input("Please input Correctly (int) : ")
        
    # Same for the price, making sure its an integer
    price = input('Please Add Item Price (int) : ')
    while not price.isdigit():
        price = input("Please input Correctly (int) : ")
        
    # cannot return error because of the prevention
    transaction123.add_item(item, qty, price)
    _hold('Item successfully added to cart!! : ')
    
def update_item():
    '''
    This fuction contain all the code necesarry for updating item and all its type

    can update name, price, and qty
    '''
    print('Update Menu'.center(40,'-'), end= '\n')
    transaction123.check_cart()
    item_list = [i['Item Name'] for i in transaction123.cart]
    target_item = input('Which item did you want to update (case-sensitive) : ')

    # Checking for duplicate
    while target_item not in item_list:
        target_item = input("Item not found (Case-Sensitive) : ")

    # command input [name, qty, price]
    target_category = input('What did you want to update? Name/Qty/Price : ')
    while target_category.lower() not in ['name','qty','price']:
        target_category = input('Wrong input (Name/Qty/Price) : ')
    
    if target_category.lower() == 'name':
        user_changes = input("Change item's Name to : ")
        transaction123.update_item_name(target_item,user_changes)

    elif target_category.lower() == 'qty':
        user_changes = input("Change item's Qty to : ")
        transaction123.update_item_qty(target_item,user_changes)

    elif target_category.lower() == 'price':
        user_changes = input("Change item's price to : ")
        transaction123.update_item_price(target_item,user_changes)
    
    _hold('Item sucessfully updated! : ')

def delete_item():
    '''
    this function hold code necessary to delete an item from the cart
    '''
    item_list = [i['Item Name'] for i in transaction123.cart]
    print('Delete Menu'.center(40,'-'), end= '\n')
    transaction123.check_cart()
    target_item = input("Which Item you want to delete? : ")
    while target_item not in item_list:
        target_item = input("Item name not found (case-sensitive): ")

    transaction123.delete_item(target_item)
    _hold('Item successfully deleted : ')
    
def reset_cart():
    '''
    this function used to reset every item in the cart
    '''

    print('Reset Menu : ')
    # final confirmation
    reset_confirmation = input('Are you sure you to reset the cart? (Y/N) : ')
    while reset_confirmation.lower() not in ['y','n']:
        reset_confirmation = input('Input Error, Please select Y or N : ')

    if reset_confirmation.lower() == 'n':
        _hold('Reset Canceled : ')
        
    elif reset_confirmation.lower() == 'y':
        transaction123.reset_transaction()
        _hold('All Item in cart is Deleted : ')

def main():
    '''
    this function hold the framework of all the main menu
    '''
    lc = True
    while lc:
        print('MAIN MENU'.center(40,'-'))
        print('[1] Add Item')
        if len(transaction123.cart) != 0:
            print('[2] Update Item')
            print('[3] Delete Item')
            print('[4] Reset Cart')
            print('[5] Check Order')
            print('[6] Finish Order and Check out')
            cart_has_item = True
        else:
            cart_has_item = False

        print('[0] Exit Super Cashier')

        # make sure the input can only int format
        user_input = input('input : ')
        while not user_input.isdigit():
             user_input = input('Input Error, Please enter correct command number (int) : ')

        user_input = int(user_input)
        # Terminate program
        if user_input == 0:
            lc = False
        
        elif user_input == 1:
            add_item()
        
        # if cart already has an item function 2 - 5 became available to use
        elif cart_has_item == True:
            if user_input == 2:
                update_item()
            
            elif user_input == 3:
                delete_item()
            
            elif user_input == 4:
                reset_cart()
            
            elif user_input == 5:
                transaction123.check_order()
                _hold()
            
            elif user_input == 6:
                transaction123.total_price()
                print('Thank you for your transaction at Pacmann Store')
                lc = False
        
        # for input that is int format but outside the range
        else:
            _hold('Command Error : ')

main()
