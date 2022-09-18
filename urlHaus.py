# 
import csv
import re #re was not imported, had to import it myself
#
def urlHausOpen(filename,searchTerms): 
#change "ur1" to "url"
# No indents here. Fix: add indents

    with open(filename) as csvfile: 
        #this was a while loop, change to with. 
        # Remove single quotes within ().

        contents = csv.reader(csvfile) 
        #change "review" to "reader", change "filename" to "csvfile."
        # Removed extra =

        for _ in range(9): # Skips first 9 lines, as they are not needed
            next(contents) # returns next item in contents list

        for eachLine in contents: # "keyword" and "eachLine" were in the wrong places. I fixed this by swapping their positions. 
            # For loop was searching in keywords when it should have been looking in contents.
            for keyword in searchTerms: # "searchTerms" and "contents" were in the wrong places. I fixed this by swapping their positions

                # searches for keywords
                x = re.findall(r'' + keyword + '', eachLine[2]) # corrected the syntax from (r"keyword",eachLine[2])

            for _ in x:
# Don't edit this line. It is here to show how it is possible
# to remove the "tt" so programs don't convert the malicious
# domains to links that an be accidentally clicked on.
                the_url = eachLine[2].replace("http","hxxp")
                the_src = eachLine[7] #changed 4 to 7 to get the right field
                # prints info found
                # added missing "%s" and corrected syntax
                # changed "*"+ to "~"*
                print("""
                    URL: %s
                    Info: %s 
                    %s """ % (the_url, the_src,"~"*60)) 

                    
