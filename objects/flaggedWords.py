class flaggedWords:
	def __init__(self, fileName="flaggedwords.txt"):
		"""
		Initialize chat flaggedWords

		:param fileName: name of the file containing flaggedWords. Default: flaggedWords.txt
		"""
		self.flaggedWords = []
		self.loadFlaggedWords(fileName)

	def loadFlaggedWords(self, fileName="flaggedWords.txt"):
		"""
		Load flaggedWords from a file

		:param fileName: name of the file containing flaggedWords. Default: flaggedWords.txt
		:return:
		"""
		# Reset chat flaggedWords
		self.flaggedWords = []

		# Open flaggedWords file
		with open(fileName, "r") as f:
			# Read all lines
			data = f.readlines()

			# Process each line
			for line in data:
				# Get old/new word and save it in dictionary
				line = line.replace("\n", "")
				self.flaggedWords.append(line)