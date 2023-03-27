# The exercise includes a file users.json containing data about users of a certain application.

# Implement a function called json_to_csv() which loads the attached users.json file, converts the file contents to the csv (comma-separated values) format, and saves it to the users.csv file.

# In the solution, use the built-in json package.


# Example:


#     [IN]: json_to_csv()


# The contents of the users.csv file after calling the function:


#     id,first_name,last_name,email,gender,is_active
#     1,Huntington,McComiskie,hmccomiskie0@admin.ch,None,False
#     2,Lukas,Cottrill,lcottrill1@linkedin.com,None,True
#     3,Heath,Rourke,hrourke2@t.co,Genderfluid,True
#     4,Lucie,Brunetti,lbrunetti3@bbb.org,Non-binary,True
#     5,Minette,Graysmark,mgraysmark4@fotki.com,None,True
#     6,Stormi,Thresher,sthresher5@umn.edu,Non-binary,True
#     7,Rochella,Berry,rberry6@moonfruit.com,Female,False
#     8,Lock,Pablo,lpablo7@networkadvertising.org,Genderqueer,False
#     9,Anton,Hugnin,ahugnin8@flickr.com,Genderqueer,True
#     10,Stephi,Jacqueme,sjacqueme9@exblog.jp,Male,False

import json
    
    
def json_to_csv():
    # Extract data
    with open('users.json', 'r') as file:
        content = json.load(file)
    
    # Transform data
    headers = ','.join(content[0].keys())
    users = [user.values() for user in content]
    rows = [','.join([str(item) for item in user]) for user in users]
    
    # Load data
    with open('users.csv', 'w') as file:
        file.write(headers + '\n')
        for row in rows:
            file.write(row + '\n')
