"""
Hard-problem agent
By Brian Tomasik

This agent is designed to illustrate in a stylized way how the hard problem of consciousness works. It's partly inspired by Gary Drescher's account of qualia in his book _Good and Real_. For explanation and a sample run, see http://www.utilitarian-essays.com/agent-to-illustrate-hard-problem.html
"""

import random

class HardProblemAgent():
	def __init__(self):
		print "Hi there."
		self.currentNeuralPattern = ''
		self.currentColor = ''
	
	def LookAtObject(self, wavelength):
		print ""
		print "I'm going to look at an object."
		print "(Wavelength = %d.)" % wavelength
		self.currentNeuralPattern = self.LightToNeuralPattern(wavelength)
		self.currentColor = self.NeuralPatternToWord(self.currentNeuralPattern)
		self.ReportSeenColor(self.currentColor)
		self.ReportColorAssociation(self.currentNeuralPattern)

	def AskHardProblem(self):
		print ""
		if self.currentColor != 'invisible':
			print "Cool. Now, let me see if it feels like something to see %s." % self.currentColor
			print "Does it feel like something to see %s?" % self.currentColor
			print "Answer: %s" % self.QueryMyselfAboutQualia(self.currentNeuralPattern)
			print "Ok, but _why_ does it feel like something to see %s?" % self.currentColor
			print "This seems completely unexplained. It's clear that my brain can perceive colors, but why, when I ask myself whether there's something it feels like to perceive these inputs, do I realize that yes, there is something it's like? Hmm. Off to read more David Chalmers, I guess."
		else:
			print "I don't see a color. Sorry."
	
	def LightToNeuralPattern(self, wavelength):
		if wavelength >= 620 and wavelength <= 750: # red
			return '00'
		elif wavelength >= 495 and wavelength <= 570: # green
			return '01'
		elif wavelength >= 450 and wavelength < 495: # blue
			return '10'
		elif wavelength >= 380 and wavelength < 450: # purple
			return '11'
		else:
			return ''

	def NeuralPatternToWord(self, pattern):
		if pattern is '00':
			return 'red'
		if pattern is '01':
			return 'green'
		elif pattern is '10':
			return 'blue'
		elif pattern is '11':
			return 'purple'
		else:
			return 'invisible'

	def NeuralPatternToAssociation(self, pattern):
		if pattern is '00': # red
			return 'firetrucks'
		if pattern is '01': # green
			return 'grass'
		elif pattern is '10': # blue
			return 'ocean'
		elif pattern is '11': # purple
			return 'plums'
		else:
			return 'radio waves'

	def ReportSeenColor(self, colorWord):
		print "I see %s." % colorWord
	
	def ReportColorAssociation(self, pattern):
		print "It reminds me of %s." % self.NeuralPatternToAssociation(pattern)

	def QueryMyselfAboutQualia(self, pattern):
		# Does it feel like something to have this pattern?
		itFeelsLikeSomething = self.PerceivingAStimulus(pattern) and self.ThinkingGoingOn() and self.ItBelongsToMe()
		if itFeelsLikeSomething:
			return "yes"
		else:
			return "no"
	
	def PerceivingAStimulus(self, pattern):
		return pattern != ''

	def ThinkingGoingOn(self):
		return True

	def ItBelongsToMe(self):
		return True

	
if __name__ == '__main__':
	Hardy = HardProblemAgent()
	lightWavelength = random.randrange(380,750)
	Hardy.LookAtObject(lightWavelength)
	Hardy.AskHardProblem()