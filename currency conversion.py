import sys
import subprocess

VND = int(sys.argv[1])

#setting exchange rate
USDtoVND = 22800
HUFtoVND = 85

#create the vars
USD = VND / USDtoVND
HUF = VND / HUFtoVND
data = "{:,}VND / ${} / {}HUF".format(VND, USD, HUF)
data = data.replace(",", ".")

#depracated by CL argument
#VND = input('How much VND you\'d like to convert? ')

#conversion and printing

def Conversion(VND):
	print
	print("{:,} Dong equals \t{} DOLLAR".format(VND, USD))
	print
	print("{:,} Dong equals \t{} FORINT".format(VND, HUF))
	print
	return 0

#write answer to clipboard
#found on StackOverflow, thanks DejaVu_Loop 
#only works on Mac afak

def writeToClipboard(data):
	p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
	p.stdin.write(data)
	p.stdin.close()
	retcode = p.wait()

#execute functions

Conversion(VND)
writeToClipboard(data)
