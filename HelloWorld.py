class world:

	def callMe(self):
		for i in range(14):
			if(i%2 == 0):
				print("Hello World !!!")
			else:
				print("not so hello !!!!")

b = world()
b.callMe()
