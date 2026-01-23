from lisa.models import Product, Order, OrderItem

class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        self.cart = self.session.get("cart",{})

    def add(self,product_id,quantity,selling_price):
        product = Product.objects.get(id=product_id)
        if (int(quantity) > product.quantity):
            return
        self.cart[str(product_id)] = {
            "id":str(product.id),
            "name":str(product.name),
            "price":float(selling_price),
            "p_type":str(product.p_type),
            "quantity":str(quantity),
            "total_price":float(selling_price)*quantity
        }
        self.session["cart"] = self.cart
        self.session.modified = True

    def remove(self,product_id):
        if str(product_id) in self.cart:
            del self.cart[str(product_id)]
            self.session["cart"] = self.cart
            self.session.modified = True

    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True