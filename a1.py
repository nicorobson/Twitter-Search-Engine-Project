#This program is designed to create a Twitter profile for the user and allows them to filter a search for tweets based on an entered hashtag.
#If the user fails to create a valid profile (ie. with first and last names that are both strings), they are repeatedly asked to re-do their login until valid.
#The user enters as many tweets as they want and then they are prompted to conduct a search using a hashtag.
#For the sake of this program, the tweets being searched are the ones in which the user inputs themself.
#The problem arises when/if they enter a hashtag in which no tweets contain that hashtag.
#If no tweets match the hashtag, the search is false and the user is then prompted to search for something else that may exist.
#The program will then search the tweets to see if any contain the new hashtag and will output the search results for the user.

def greeting(first_name, last_name):    
    return 'Profile: ' + str(last_name) + ', ' + str(first_name) + '\n' + 'Hello ' + str(first_name) + ' ' + str(last_name) + ', welcome to Twitter!'   
#This first function simply takes in the user input for their first and last names and returns their created profile, and a welcome message including their name.

def with_hashtag(listOfTweets, the_hashtag):    #This function takes in the list of tweets from the user, and the hashtag.
    tweets_with_hashtag = []                    #Making a list for the tweets that contain the user-entered hashtag.
    for i in listOfTweets:                      #Looping through the list of tweets, where i is each tweet.
        if the_hashtag in i:                    #If the user's hashtag is contained in a tweet, that tweet gets added to the tweets_with_hashtags list.
            tweets_with_hashtag.append(i)   
    return tweets_with_hashtag                  #Returning the list of tweets that have the hashtag.

def searchResult(listOfTweets, the_hashtag):    #This function assigns a True or False value to the conducted search based on if there are any tweets with the hashtag.
    search_result = True
    tweets_with_hashtag = []

    for i in listOfTweets:                      #Creating the same loop as in the second function to add the tweets with the hashtag to a separate list.
        if the_hashtag in i:
            tweets_with_hashtag.append(i)

    if len(tweets_with_hashtag) == 0:           #If the length of this list is 0, then there are no tweets with the hashtag.
        search_result = False                   #As a result, the search is false and no tweets have the hashtag.
    return search_result

firstName = str(input('First name: '))          #Here is where the user inputs their first and last name. These two inputs start the program.
lastName = str(input('Last name: '))

while firstName.isdigit() or lastName.isdigit():                #This while loop checks to see if the first or last name is a number, instead of a string.
    print('First or last name is invalid, please try again.')   #If either name is a number, the program asks the user to enter a valid name until they do so.
    print()
    firstName = str(input('First name: '))
    lastName = str(input('Last name: '))

print()
print(greeting(firstName, lastName) + '\n')            #This line of code calls the greeting function which prints the user's profile and a personalized welcome message.

print("Let's get started by composing some tweets..." + '\n')
print("Compose as many tweets as you want, enter '**' when you are finished")
#These two messages introduce the tweeting aspect of the program.

tweets_list = []                #This list will be reserved for every tweet entered by the user.
tweet = str(input('Tweet: '))   #The user inputs their first tweet.

if tweet != '**':               
    tweets_list.append(tweet)

while tweet != '**':                    #'**' is the condition that makes the program stop asking for tweets.
    tweet = str(input('Tweet: '))       
    tweets_list.append(tweet)           #The program will add each tweet to the tweets_list until the user enters '**'.

for i in tweets_list:                   #This for loop will loop through the list of tweets (where i is each tweet) and locates the '**' tweet.
    if i == '**':
        tweets_list.remove(i)           #Since the '**' is a stopping condition rather than an intended tweet, we remove it from the list.
print()
print('You can search for anything on Twitter by entering a hashtag.')
print('For example, #Election2020' + '\n')
#These two messages introduce the hashtag search in the program.

hashtag = str(input('Give it a try: '))         #First hashtag input.
print()
result = searchResult(tweets_list, hashtag)     #This line of code calls the function that determines if the hashtag search is true or false.
                                                #We assign this value to a variable so we can access it.
while result == False:
    print('Nobody is talking about: ' + str(hashtag) + ' right now.')       #While the search is false, the program will let the user know that their search-
    hashtag = str(input('Try searching for something else: '))              #-returned no matching tweets to their hashtag, so they can enter a new hashtag.
    print()
    result = searchResult(tweets_list, hashtag)                    #This line of code updates the result variable to True or False based on the newly entered hashtag.

if result == True:                                          #If the new search result is now true, we do the following:
    matching_tweets = []                                    #Create a new list for the tweets that match the hashtag.
    matching_tweets = with_hashtag(tweets_list, hashtag)    #Call the function that returns the list of tweets that contain the hashtag.

    print('Your search results: ')                          #This shows the user their search results.
    for j in matching_tweets:                               #Looping through each matching tweet and printing that tweet (where j is each tweet).
        print(j)
    
 
