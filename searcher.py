#Created by Alex Schultz
#This is a sample peice of code that flags senstive information based on regex
import os
import re

#Trigger workflow

test_dir="SampleSystem"
piiFound = False

regex_list={
    #High priority to find SSNs such as in the format XXX-XX-XXXX
    "SSN":re.compile("\d{3}-?\d{2}-?\d{4}"),
    #More complex SSN: ("(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-+(?!0{4})\\d{4}"),
    #This may capture any sequance of 5 numbers
    "FileLocation":re.compile("\\[^\\]+$")
}

def fileSearch(fileIn):
    piiFound = False
    #I know, I know, smack on the wrist for 3 for loops
    for i in regex_list:
        for j, line in enumerate(open(fileIn)):
            for match in re.finditer(regex_list[i], line):
                print("Found  " + i + " in " + fileIn + " on line: " + str(j+1) + " " + match.group() ) #regex_list[i])
                piiFound = True

def main():
    for i in os.listdir(test_dir):
        fileSearch(os.path.join(test_dir, i))
    if(not piiFound):
        print("Found pii above, please fix.")
main()
