# File to audio

This function reads a pdf or a text file using pyttsx3 library. (I will add more file formats)
In order to test the function using cmd, run the following command:
> python file_reader.py "filename"

## Libraries

### pyttsx3:
pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
To download: pip install pyttsx3
Documentation: https://pyttsx3.readthedocs.io/en/latest/

### PyPDF2:
A Pure-Python library built as a PDF toolkit. It is capable of:
- extracting document information (title, author, …) <br>
- splitting documents page by page <br>
- merging documents page by page <br> 
- cropping pages <br>
- merging multiple pages into a single page <br>
- encrypting and decrypting PDF files and more! <br>

By being Pure-Python, it should run on any Python platform without any dependencies on external libraries. It can also work entirely on StringIO objects rather than file streams, allowing for PDF manipulation in memory. It is therefore a useful tool for websites that manage or manipulate PDFs.
To download: pip install PyPDF2
Documentation: https://pythonhosted.org/PyPDF2/
