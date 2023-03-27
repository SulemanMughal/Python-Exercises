# A file called hashtags.txt containing hashtags related to sport is attached to the exercise:


#     #sport #fitness #training #motivation #gym #sports #workout #fit #football #love #instagood #fitnessmotivation
#     #lifestyle #running #like #bodybuilding #healthy #instagram #health #soccer #follow #crossfit #photography #bhfyp #run
#     #nature #fun #healthylifestyle #muscle #bhfyp #fashion #fitfam #gymlife #photooftheday #team #personaltrainer #nike
#     #picoftheday #exercise #mma #sportlife #boxing #athlete #bike #basketball #happy #deporte #gymmotivation #strong
#     #cycling #yoga #style #ufc #sportmotivation #fitnessgirl #calcio #instafit


# Implement a function called clean_hashtags() that takes three arguments:

#     input_file - filename containing hashtags

#     output_file - filename to which the hashtags should be saved

#     length - the maximum length of the hashtag

# The '#' sign is not included in the length of the hashtag. For example, the hashtag '#gym' has a length of 3.

# The clean_hashtags() function loads a file called input_file and does some hashtag cleanup. The function extracts hashtags up to length characters long and also removes duplicates. It then saves the alphabetically sorted hashtags to a file called output_file, saving each hashtag in a new line.


# Example:


#     [IN]: clean_hashtags('hashtags.txt', 'clean.txt', 5)


# The contents of the clean.txt file after calling the function:


#     #bhfyp
#     #bike
#     #fit
#     #fun
#     #gym
#     #happy
#     #like
#     #love
#     #mma
#     #nike
#     #run
#     #sport
#     #style
#     #team
#     #ufc
#     #yoga

def clean_hashtags(input_file, output_file, length):
    # Read hashtags
    with open(input_file, 'r') as file:
        content = file.read()
    
    # Process hashtags
    hashtags = content.split()
    short_hashtags = [
        hashtag
        for hashtag in hashtags
        if len(hashtag) <= length + 1
    ]
    unique_short_hashtags = sorted(set(short_hashtags))
    
    # Write hashtags to the file
    with open(output_file, 'w') as file:
        for hashtag in unique_short_hashtags:
            file.write(hashtag + '\n')

