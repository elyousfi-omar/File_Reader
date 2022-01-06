import pyttsx3
import PyPDF2
import sys

def text_to_audio(filename):
	"""Converts a text or a pdf file to audio
	
	Args:
		filename (string): The file to read
	Returns:
		An audio by the computer's default driver
	"""
	extension = filename.split(".")[-1]
	audio = pyttsx3.init()
	file = open(filename, 'rb')

	if extension == "txt":
		to_read = file.read().decode("utf-8")

	elif extension == "pdf":
		read_pdf = PyPDF2.PdfFileReader(file)
		nb_pages = read_pdf.getNumPages()
		page = read_pdf.getPage(0)

		to_read = page.extractText()
	
	audio.say(to_read)
	audio.runAndWait()


if __name__ == '__main__':
	globals()["text_to_audio"](sys.argv[1])


