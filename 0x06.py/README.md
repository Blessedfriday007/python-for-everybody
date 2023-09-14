### EXERCISE - FILES.PY
*Write a program to read through a file and print the contents of the file (line by line) all in upper case.
Executing the program will look as follows:*

```
python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
     BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
     SAT, 05 JAN 2008 09:14:16 -0500
```
### Short explanations
- fhand is the Mnemonic variable that i used, it is the handle that i used to manipulate the files.
- rstrip() is the  command that i used to remove whitespaces from the right.
- upper() is the command i used to convert the file to uppercase.

### EXERCISE - FNAME.PY

*Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:*
```
X-DSPAM-Confidence:    0.8475
```
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data [here](http://www.py4e.com/code3/mbox-short.txt) when you are testing below enter mbox-short.txt as the file name.


### Short explanations
#### line 10
```
 if  line.lower().startswith('x-dspam-confidence:'):

the line.lower() statement was used to convert the x-dspam-confidence: to all lower case
the .startswith is a reserved word in python, it is used to check if a string starts with a given substring or not.

 ```
- rstrip(): I used it to strip off whitespaces from the right, after extracting all the floating point values.

*Executing the program will look as follow.*

```
$  Python fname.py
Enter file name: mbox-short.txt
Count: 27
Total: 20.269400000000005
Average spam confidence: 0.7507185185185187

```


Read up more documentations [here](https://www.learnpython.org/)
