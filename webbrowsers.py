import webbrowser

# first we import webbrowser
search = input()
# taking input from the user
google = 'https://www.google.co.in/search?q='
# we use variable in the form of string
youtube = 'https://www.youtube.com/results?search_query='
# we  use variable in the from of string 
search_list =  [google,youtube]

# we are taking input from the user to search something in google and youtube 
for i in search_list:
# we are making loop in which goes in search_list
	webbrowser.open(i+search)  