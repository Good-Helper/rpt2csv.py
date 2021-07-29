import rpt2csv

with open("path\to\input.rpt") as inputFile:
	with open("path\to\output.rpt",'wb') as outputFile:
		rpt2csv.convert(inputFile,outputFile)