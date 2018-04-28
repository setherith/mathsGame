import os.path

class score_card:
	"""Keeping score..."""
	def __init__(self):
		self.path = "./score.txt"
		
	def addScore(self, score):
		file = open(self.path, 'a')
		file.write(score + '\n')
		
	
	def readScores(self):
		file = open(self.path, 'r')
		return file.read()
		
	def createScores(self):
		if self.checkIfScoresExist():
			return
		else:
			open(self.path, 'w')
		
	def checkIfScoresExist(self):
		return os.path.isfile(self.path)
	
	def deleteCard(self):
		os.remove(self.path)
