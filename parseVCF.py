#!/usr/local/bin/python
# Khushbu Patel | 04/30/2018
# parses VCF - caculates numbers of bases that Pass or do not pass due to consensus/coverage or other issues. Also, calculates number of bases with depth ge and lt 20
# Usage: ./parseVCF.py 

infile=""
infile=raw_input("Enter the file name:") #takes file as user input from the command line
f=open(infile,"r")

count =0
count_dp20 = 0
count_af = 0
count_pass = 0
count_other = 0
depth = []
dp = 0
dp_lt20 = 0

for line in f:
	line =line.rstrip()
	if line.startswith('##'):
		continue
	
	elif line.startswith('#CHROM'):
		header = line
		
	
	else:
		array = line.split()
		depth.append(array[9])	#converting tuple to list
		
		if(array[6] == 'DP20;AF0.95'):
			count = count+1
		elif(array[6] == 'DP20'):
			count_dp20 += 1
		elif(array[6] == 'AF0.95'):
			count_af += 1
		elif(array[6] == 'PASS'):
			count_pass += 1
		else:
			count_other +=1
			
		
			
for i in depth:
	str = i.split(':')
	if(int(str[5]) >= 20):		# every 5th element after splitting is the depth; parsing str to int
		dp += 1
	else:
		dp_lt20 += 1
			
			
			
			
			
print 'Number of bases that passed =', count_pass		
print 'Number of bases that did not meet both consensus and coverage =', count
print 'Number of bases that did not meet coverage only =', count_dp20
print 'Number of bases that did not meet consensus only =', count_af
print 'Number of bases that did not pass due to other reasons =', count_other
print 'Number of bases that with depth ge 20 =', dp
print 'Number of bases that with depth less than 20 =', dp_lt20
