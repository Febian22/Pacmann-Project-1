from tabulate import tabulate

class Transaction:
    def __init__(self):
        self.cart = [] 
    
    def add_item(self, item_name:str, item_qty:str, item_price:str):
        '''
        This function used for adding item into the cart

        parameter:
        - item_name = str
        - item_qty = isdigit; can be str or int
        - item_price = isdigit; can be str, int, or float

        return:
        None
        '''
        if item_qty.isdigit() == False:
            raise ValueError('Quantity must be a digit')
        if item_price.isdigit() == False:
            raise ValueError('Product Price must be a digit')
        
        item_dict = {'Item Name' : item_name, 'Qty': int(item_qty), 'Price per Item' : int(item_price)}
        self.cart.append(item_dict)

    def update_item_name(self, item_name, new_item_name):
        '''
        This function used to change the name of the item in the cart

        parameter:
        - item_name = str; case-sensitive
        - new_item_name = str; case-sensitive

        return:
        None
        '''
        for index, item in enumerate(self.cart):
            if item['Item Name'] == item_name:
                self.cart[index]['Item Name'] = new_item_name
                return None
        raise ValueError('Item Name is not found, make sure to input correctly (Case-Sensitive)!')
    
    def update_item_qty(self, item_name, new_item_qty):
        '''
        This function used to change the quantity of the item in the cart

        parameter:
        - item_name = str; case-sensitive
        - new_item_qty = isdigit;

        return:
        None
        '''
        if not new_item_qty.isdigit():
            raise ValueError('Item Qty must be a digit')
        
        for index, item in enumerate(self.cart):
            if item['Item Name'] == item_name:
                self.cart[index]['Qty'] = int(new_item_qty)
                return None
        raise ValueError('Item Name is not found, make sure to input correctly (Case-Sensitive)!')

    def update_item_price(self, item_name:str, new_item_price:str):
        '''
        This function used to change the price of the item in the cart

        parameter:
        - item_name = str; case-sensitive
        - new_item_price = isdigit;

        return:
        None
        '''
        if not new_item_price.isdigit():
            raise ValueError('Item price must be a digit')
        for index, item in enumerate(self.cart):
            if item['Item Name'] == item_name:
                self.cart[index]['Price per Item'] = int(new_item_price)
                return None
        raise ValueError('Item Name is not found, make sure to input correctly (Case-Sensitive)!')

    def delete_item(self,item_name:str):
        '''
        This function used to delete specified item in cart

        parameter:
        - item_name = str; case-sensitive

        return:
        None
        '''
        for index, item in enumerate(self.cart):
            if item['Item Name'] == item_name:
                self.cart.pop(index)
                return None
        raise ValueError('Item Name is not found, make sure to input correctly (Case-Sensitive)!')
    
    def reset_transaction(self):
        '''
        This function used to delete all item in cart

        parameter:
        None

        return:
        None
        '''
        self.cart.clear()
    
    def check_order(self):
        '''
        This function will print all item in the cart

        parameter:
        None

        return:
        None
        '''
        output = []
        total_price = 0
        for index, item in enumerate(self.cart):
            content = {}
            content['No'] = index + 1
            for x in item:
                content[x] = item[x]
            content['Price Total'] = content['Price per Item'] * content['Qty']
            total_price += content['Price Total']
            output.append(content)
        output.append({'No': 'End', 'Item Name' : 'Total Price', 'Price Total': total_price})
        print(tabulate(output, headers='keys', tablefmt='grid',intfmt=","))
    
    def calculate_total_price(self):
        '''
        This function used to calculate total price and store it
        in self.total_price without the need to use check_order

        parameter:
        None

        return:
        None
        '''
        self.total_price = 0
        for item in self.cart:
            self.total_price += int(item['Price per Item']) * int(item['Qty'])
        
    
    def total_price(self):
        '''
        This function will print all item in the cart and give total product prices (also applying discount)

        parameter:
        None

        return:
        None
        '''
        Transaction.calculate_total_price(self)
        if self.total_price > 500_000:
            discount = 0.1
        elif self.total_price > 300_000:
            discount = 0.08
        elif self.total_price > 200_000:
            discount = 0.05
        else:
            discount = 0
        
        print(f"Total belanjaan anda sebesar : Rp. {int(self.total_price * (1-discount))}")
    
    def check_cart(self):
        '''
        This function print tabulated (grid) cart
        '''
        print(tabulate(self.cart, headers='keys', tablefmt='grid', intfmt=','))
       
        
        
    

if __name__ == '__main__':
    try:
        transaction123 = Transaction()
        transaction123.add_item('Ayam','2','12000')
        transaction123.update_item_name('Ayam','Bebek')
        transaction123.update_item_qty('Bebek','1')
        transaction123.update_item_price('Bebek','14000')
        transaction123.add_item('Ayam','3','10000')
        transaction123.check_cart()
        transaction123.check_order()
        transaction123.total_price()

    except ValueError as e:
        print(f"Error : {e}")
