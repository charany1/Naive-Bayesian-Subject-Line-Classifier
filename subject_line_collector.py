"""
This file collect subject lines from e-mail data set.

"""

import os
 ##getting file names of all files in spam classified training data set

files=os.listdir(os.getcwd()+'/spam') 

##storing  spam subjects in a "spam_subjects.txt" file in csv format=>(subject,category)
with open("spam_subjects.txt","a") as out:
	category="spam"

##Parse each file and get the subject, also remove commas from subject to avoid trouble with CSV format
	for f_name in files:
		with open(os.getcwd()+"/spam/"+f_name) as f:
			data=f.readlines()
			for line in data:
				if line.startswith("Subject:"):
					line.replace(",","")
					print(line)
					out.write("%s,%s\n".format(line[8:-1],category))


 ##getting file names of all files in easy_ham(non-spam) classified training data set
files=os.listdir(os.getcwd()+'/easy_ham') 

##storing  spam subjects in a "spam_subjects.txt" file in csv format=>(subject,category)
with open("non_spam_subjects.txt","a") as out:
	category="non_spam"

##Parse each file and get the subject, also remove commas from subject to avoid trouble with CSV format
	for f_name in files:
		with open(os.getcwd()+"/easy_ham/"+f_name) as f:
			data=f.readlines()
			for line in data:
				if line.startswith("Subject:"):
					line.replace(",","")
					print(line)
					out.write("%s,%s\n".format(line[8:-1],category))
