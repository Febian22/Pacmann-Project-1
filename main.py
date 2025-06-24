from module import Transaction

'''
notes for further improvement

1. add check order [V]
2. add from module check cart without the total [V]
3. add finalize order 
4. more pretty? 
5. documentation 

'''
print('-'*40)
print('')
print('Welcome to Pacmann Super Cashier'.center(40))
print('')
print('-'*40)

transaction123 = Transaction()
cart_has_item = False


def _hold(message = ''):
    print('\n'*1)
    holder = input(f"{message}Please press anything to continue")
    print('\n'*1)
    
def main():
    print('MAIN MENU'.center(40,'-'))
    print('[1] Add Item')
    if len(transaction123.cart) != 0:
        print('[2] Update Item')
        print('[3] Delete Item')
        print('[4] Reset Cart')
        print('[5] Check Order')
        item_list = [i['Item Name'] for i in transaction123.cart]
        cart_has_item = True
    else:
        cart_has_item = False

    print('[0] Exit Super Cashier')

    user_input = input('input : ')
    if not user_input.isdigit():
        _hold('Input Error : ')
        main()

    user_input = int(user_input)
    if user_input == 0:
        return
    
    elif user_input == 1:
        print('Add Menu : ')
        item = input('Please Add Item Name (str) : ')
        if cart_has_item == True: # Checking for duplicate
            if item in item_list:
                _hold('Duplicate found : ')
                main()

        qty = input('Please Add Item Quantity (int) : ')
        if not qty.isdigit():
            _hold("Please input Correctly (int) :")
            main()
        price = input('Please Add Item Price (int) : ')
        if not price.isdigit():
            _hold ("Please input Correctly (int)")
            main()
        
        transaction123.add_item(item, qty, price)
        _hold('Item successfully added to cart!! : ')
        main()
    
    elif cart_has_item == True:
        if user_input == 2:
            print('Update Menu : ')
            transaction123.check_cart()
            target_item = input('Which item did you want to update (case-sensitive) : ')
            if target_item not in item_list:
                _hold("Item not found (Case-Sensitive) : ")
                main()
            
            target_category = input('What did you want to update? Name/Qty/Price : ')
            while target_category.lower() not in ['name','qty','price']:
                target_category = input('Wrong input, Please input correctly (Name/Qty/Price) : ')
            
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
            main()

        
        elif user_input == 3:
            print('Delete Menu : ')
            transaction123.check_cart()
            target_item = input("Which Item you want to delete? : ")
            transaction123.delete_item(target_item)
            _hold('Item successfully deleted : ')
            main()
        
        elif user_input == 4:
            print('Reset Menu : ')
            reset_confirmation = input('Are you sure you to reset the cart? (Y/N) : ')
            while reset_confirmation.lower() not in ['y','n']:
                reset_confirmation = input('Input Error : Please select Y or N ')

            if reset_confirmation.lower() == 'n':
                _hold('Reset Canceled : ')
                main()
            elif reset_confirmation.lower() == 'y':
                transaction123.reset_transaction()
                _hold('All Item in cart is Deleted : ')
                main()
        
        elif user_input == 5:
            transaction123.check_order()
            _hold()
            main()
    
    else:
        _hold('Command Error : ')
        main()

try:
    main()
except ValueError as e:
    _hold(f"Error : {e}\n")
    main()
