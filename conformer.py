# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 12:28:56 2014

A script that takes a csv file, and translate it to a email-filter you can import into gmail.

Author: Kristian Botnen
Email: kristian@mbmedia.no
License: The MIT License

Introduction:

Do you get a lot of unwanted email? yes,
Do you want to stop all this from reaching your inbox? yes,
Do you get hold of a blacklist in csv format that you can not import directly to gmail? yes,
If you answered yes to all of the 3 above questions you have been in the same situation as me, and maybe this little snippet can help you out.

Future plans:

take the csv file from input parameter
take the resulting mailfilter filename as input parameter
take "wanted action" as input parameter

Installation:

soon to come...

@author: Kristian Botnen
"""
import argparse

class Conformer:
    
    def add(self, x, y):
        """This is a method to be used from the testclass.
        
        Parameters
        ----------
        x : number
            The first of the two numbers to be added together.
        y : number
            The second of the two numbers to be added together.
            
        Returns
        -------
        returnValue : number
            Returns the value of the two parameters x and y added together.
            
        """
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            returnValue = x+y
            return returnValue
        else:
            raise ValueError    
    
    def readandparse(self, input_filename, output_filename):
        data = []
                
        #Open the CSV file which contains a lot of email-addresses.
        with open(input_filename) as f:
            content = f.readlines()
        
        for line in content:
            data = line.rstrip('\r\n').split(",")
            print data
        
        #Calculate the header_id_variable
        headercount = ""        
        for x in range(len(data)):
            headercount = headercount + str(x) + ","
        
        template_header = '''<?xml version='1.0' encoding='UTF-8'?><feed xmlns='http://www.w3.org/2005/Atom' xmlns:apps='http://schemas.google.com/apps/2006'>
        	<title>Mail Filters</title>
        	<id>tag:mail.google.com,2008:filters:{idcount}</id>
        	<updated>2014-03-29T11:31:29Z</updated>
        	<author>
        		<name>Kristian Botnen</name>
        		<email>kristianbotnen@gmail.com</email>
        	</author>
        '''.format(idcount=headercount[:-1])
        
        template_body = ""
        for mailadress in data:
            print "Write:", mailadress
            inputmail=mailadress
            template_body = template_body + '''<entry>
        		<category term='filter'></category>
        		<title>Mail Filter</title>
        		<id>tag:mail.google.com,2008:filter:1</id>
        		<updated>2014-03-29T11:31:29Z</updated>
        		<content></content>
        		<apps:property name='from' value='{email}'/>
        		<apps:property name='shouldArchive' value='true'/>
        		<apps:property name='shouldTrash' value='true'/>
        		<apps:property name='sizeOperator' value='s_sl'/>
        		<apps:property name='sizeUnit' value='s_smb'/>
        	</entry>
             '''.format(email=inputmail)    
            
        
        template_footer = '''</feed>'''
        
        template = template_header + template_body + template_footer
        
        #Write the result into a new file, overwriting existing file.
        file = open(output_filename, "w")
        file.write(template)
        file.close()
        
def main():
    print "Start..."
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Name of the CSV file to read email addresses from.", type=str)
    parser.add_argument("output", help="Name of the XML file that contains the ready-to-use gmailfilters.", type=str)
    parser.parse_args()
    args = parser.parse_args()
    
    # We store the args value in variables so we can sanitize the input later if needed.
    in_filename = args.input
    out_filename = args.output
    
    conformer = Conformer()
    conformer.readandparse(in_filename, out_filename)
    print "Done..."
        
if __name__ == '__main__':
    main()