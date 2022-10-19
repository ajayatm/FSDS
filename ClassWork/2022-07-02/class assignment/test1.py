import logging
class String:

    logging.basicConfig(filename='log1.log',level=logging.INFO,format='%(levelname)s %(message)s')

    def __init__(self,string):
        self.string = string
    
    #01. Try to extract data from index one to index 300 with a jump of 3
    def getdata(self,start,end,jump):
        logging.info('Getting data from index %s to index %s with a jump of %s',start,end,jump)
        return self.string[start:end:jump]
    
    #02. Try to reverse a string without using reverse function
    def getreverse(self):
        logging.info('Getting data in reversed order')
        return self.string[::-1]
    
    #03. Try to split a string after conversion of entire string in uppercase
    def splitupper(self):
        logging.info('Getting data in split uppercase format')
        self.a = self.string.upper()
        return self.a.split()
    
    #04. try to convert the whole string into lower case
    def getlower(self):
        logging.info('Getting data in split lowercase format')
        return self.string.lower()
    
    #05. Try to capitalize the whole string
    def getupper(self):
        logging.info('Getting data in split uppercase format')
        return self.string.upper()
    
    #06. Write a diference between isalnum() and isalpha()
    def isalnum_vs_isalpha(self):
        logging.info('Getting the difference between isalnum and isalpha')
        return 'isalnum() function checks if the string contains only alphabets and numbers (alphanumeric) \
        characters. isalpha() function checks if the string contains only alphabetic characters.'

    #07. Try to give an example of expand tab
    def expandtab(self,s):
        logging.info('Expanding tabs if any')
        return s.expandtabs()
    
    #08. Give an example of strip , lstrip and rstrip
    def strip(self,s):
        logging.info('Strip example')
        return s.replace(' ','*'), s.strip().replace(' ','*'), s.lstrip().replace(' ','*'), s.rstrip().replace(' ','*')
    
    #09.  Replace a string charecter by another charector by taking your own example
    def replace(self,string,char):
        logging.info('replace with * example')
        return string.replace(char,'*')
    
    #10. Try  to give a definition of string center function with and example
    def center(self,string):
        logging.info('string center example')
        return string.center(100,'!')

try:
    stringobject = String("This is my first Python programming class and I am learning python string and its functions.")
    logging.info('Object declared')
    print(stringobject.replace('Ajay','j'))

except Exception as e:
    stringobject.logging.critical(e)
