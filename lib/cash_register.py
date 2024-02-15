#!/usr/bin/env python3

class CashRegister:
	def __init__(self, discount=0):
		self.discount = discount
		self.total = 0
		self.items = []
	
	def add_item(self, item, price, quantity=1):
		self.total += price * quantity
		self.last_item_price = price
		self.last_item_quantity = quantity
		for num in range(quantity):
			self.items.append(item)
	
	def apply_discount(self):
		if self.discount == 0:
			print("There is no discount to apply.")
		else:
			self.total = self.total * ((100 - self.discount)/100)
			print(f"After the discount, the total comes to ${int(self.total)}.")

	def void_last_transaction(self):
		for num in range(self.last_item_quantity):
			self.total -= self.last_item_price
		self.items.pop()
		