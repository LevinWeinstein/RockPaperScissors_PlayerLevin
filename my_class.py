class PlayerLevin(PlayerClass):
	# Levin Weinstein's submission
	def __init__(self,LorR):
		super().__init__(LorR)
		self.State = [1]
		self.Mod = 0
	def update(self):
		self.MakeSelection()
		if self.Choice == 0:
			self.image=self.ImgR
		if self.Choice == 1:
			self.image=self.ImgP
		if self.Choice == 2:
			self.image=self.ImgS
	def updateState(self, OpponentPlay, MyPlay):
		if self.Mod == 1:
			if  MyPlay % 3 > OpponentPlay % 3:
				self.State[0] = (MyPlay + 1) % 3
			elif MyPlay % 3 < OpponentPlay % 3:
				self.State[0] = (OpponentPlay + 1) % 3
			else:
				self.State[0] = (MyPlay + 1) % 3
			self.Mod = 0
		else:
			self.Mod = 1	
	def MakeSelection(self):
		for alice in range(0, 100):
			alice
		self.Choice = self.State[0]

