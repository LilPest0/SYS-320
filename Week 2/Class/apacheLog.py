import logCheck
import importlib
importlib.reload(logCheck)

# Apache events
def apache_events(filename, service, term):

    # call syslogcheck and return results
    is_found = logCheck._logs(filename, service, term)

    # found list
    found = []

    # loop thru results
    for eachFound in is_found:

        # print(eachFound)
        # split results
        sp_results = eachFound.split(" ")

        # append split value to found list
        # "GET /cgi-bin/test-cgi HTTP/1.1" 404 435 "-" "-"
        found.append(sp_results[0] + " " + sp_results[0] + " " + sp_results[1]) 

    # Remove duplicates by using set, 
    # and convert list to dictionary
    getValue = set(found)

    # Print the results
    for eachValue in getValue:
        
        print(eachValue)