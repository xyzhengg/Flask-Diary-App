### Flask-Diary-App

## About the app
This app was created with the purpose of connecting couples in long distance relationships, or who are 
separated for extended periods. 

It allows two users to contribute to a shared diary so they can stay connected with each others lives despite their distance and time differences. The app will display both participants posts on the same page to create a sense of unity, while also allowing each user to view only their own or their partners' posts. 

## Explanations of the technologies used
This app was created using Flask, with Python, CSS, HTML, Javascript, and Progresql

## The approach taken
1. Began with simply setting up sign up and login pages
2. Then make add entry pages
3. Worked out some of the functions I wanted to include
4. Gradually added more functions
5. Gradually added more validation info
6. Added extra functions such as viewing only your own posts
7. Added extra function of having a chat 

## Special features I made
# Sign Up/Login
1. Email validation - requires certain checks to count as an email
2. Password check
3. Check if user is already in the database or not, as each user can only have 1 account
4. Allow ability to input someones diary code to be added to their account. There is a check in place - if someonelse already sharing the dairy, you cannot join
5. Checks if diary code is valid
6. Checks for incomplete fields

# Main Page
1. Memories section shows 4 posts, but if you have elss than 4, it will just show the number of posts you have
2. Check for if you have any posts - if not, will ask you to create one
3. Same check applies in section where you view only your posts
4. Posts display based on date
5. Depending on how many posts there are for the day, the display changes/layout changes 

# View Post
1. Depending on how many images there are, the layout changes
2. If you are the writer of the post and you're the one signed in, you have rights to edit or delete the post. You cannot do this to the other person's post

# Edit Post
1. Adding files allows you to append more images
2. Can delete all images by pressing the "Delete all images" button

# View Single User Posts
1. If you're the signed in user and you have no posts, your page will allow you to create an entry. If you are viewing the other persons page, that button will not show

# Chat Function
1. If you're the one signed in, your chat bubble will appear on the right
2. Page auto-scrolls down as message list can get very long. Nav bar stays pinned at the top to easily navigate away

## Installation instructions
None at this stage - not usable unless you have my laptop!

## Unsolved problems
At this stage, all functions the app allows, work well. 