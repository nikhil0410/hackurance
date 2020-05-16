# from django.test import TestCase

# Create your tests here.
class abc():
	def __init__(self, name, sal):
		self.name = name
		self.sal = sal

	def increment(self, rate):
		return self.sal*(rate+1)

	# def __str__(self):
	# 	return 'This is a class for Name and Salary'
	def __repr__(self):
		return "This is for developer"


a = abc('Nikhil', 100000)
# print(a.increment(0.30))
# print(dir(a))
# print(a)

li = [1,2,3,4,5]
print(dir(li))