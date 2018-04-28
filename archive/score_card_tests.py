import score_card
import random


score = score_card.score_card()

print('Exists: ' + str(score.checkIfScoresExist()))

print('creating card...')

score.createScores()

print('Exists: ' + str(score.checkIfScoresExist()))

print('Adding Scores...')

for x in range(0, 10):
	score.addScore("Test Score - " + str(random.randint(1,100)))
	
print('Reading scores...')

print(score.readScores().split('\n'))

print('Deleting score file...')

score.deleteCard()

print('Finished')
