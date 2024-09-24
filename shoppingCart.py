#สร้างสินค้า โดยสินค้า 1 ชิ้นต้องมีชื่อ ราคา และจำนวน
class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def available_quantity(self):
        return self.quantity
    
    # ฟังก์ชันการลดจำนวนของสินค้าในคลัง (สินค้าคงเหลือ)
    def reduce_quantity(self,amount):
        if amount <= self.quantity:
            self.quantity -= amount
            return True
        else:
            print(f"Not enough {self.name} in stock")
            return False
        
# สร้างรถเข็นไว้ใส่สินค้า
class shoppingCart:
    def __init__(self):
        self.items = [] # self.items คือรถเข็น ส่วน [] คือ รถเข็นยังว่าง
    
    # เพิ่มสินค้าลงในรถเข็น    
    def add_product(self,product,quantity):
        if product.reduce_quantity(quantity):
            self.items.append((product,quantity)) # .append คือการเพิ่ม โดยเราจะเพิ่ม product กับ quantity ลงไปในลิสต์หรือรถเข็น
            print(f"Added {quantity} of {product.name} to the cart.")
            
    def remove_product(self,product_name):
        for item in self.items: # item คือ สินค้า1อย่าง ใน self.items หรือตะกร้า
            product, quantity = item
            if product.name == product_name:
                self.items.remove(item)
                print(f"removed {product_name} from the cart.")
                return
        print(f"Product {product_name} not found in the cart.")
    
    # แสดงสินค้าในตะกร้าหรือ self.items    
    def show_cart(self):
        if not self.items:
            print("The cart is empty.")
        else:
            print(f"Items in the cart:")
            for product, quantity in self.items:
                remaining_quantity = product.available_quantity() #จำนวนคงเหลือ
                print(f"Product: {product.name}\nQty: {quantity} units\nTotal: {product.price * quantity}\nRemaining: {remaining_quantity} units")
                
                
    # รวมเงิน
    def total_price(self):
        total = sum(product.price * quantity for product, quantity in self.items)
        return total
    

# สร้างสินค้าจาก class Product
product1 = Product("snack",20,100)
product2 = Product("candy",5,50)
product3 = Product("milk",15,50)

# สร้างรถเข็นจาก class ShoppingCart
customer1 = shoppingCart() # ลูกค้าคนที่ 1 มีรถเข็น 1 คัน

# เพิ่มสินค้าลงในรถเข็น
customer1.add_product(product1,5)
customer1.add_product(product3,5)

# แสดงสินค้าในรถเข็น (สินค้าที่จะซื้อ)
customer1.show_cart()

# แสดงราคารวมของสินค้าทั้งหมดในรถเข็น
print(f"Total price: {customer1.total_price()} USD")

