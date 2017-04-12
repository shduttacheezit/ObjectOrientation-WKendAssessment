log_file = open("um-server-01.txt")


def sales_reports(log_file): 
    for line in log_file: # traverse every line in log_file
        line = line.rstrip() #whitespace removed
        day = line[0:3] # day var deletes the first 3 elements
        if day == "Mon": #looking for Monday sales info
            print line


sales_reports(log_file)
