# AlmostTwiter
### Overview

1. user can create and delete posts
2. user can like other posts
3. user can comment under a post
4. user can search for a specific post
___

### video Demo:

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/1spL6MmuygQ/0.jpg)](http://www.youtube.com/watch?v=1spL6MmuygQ)
___

### Description:

**Python**
app
1.  register function registers users,
    ensures user does not use an existing username. If user enters an existing username
    it redirtects to an apology page. If confirm password and password are not same
    it redirects to an apology page and dsiplays appropriate error.

2.  login function logs in user,
    It redirects user to an apology page if user enters a non existing username or
    if username and password do not match

3.  dashboard function retreives all the posts made by all the user along with
    their like/dislike status by thr user
    and displays it on the dashboard.

4.  add function adds post entered by the user into the database.

5.  liked_data function gets the id of the post whose like/dislike button was clicked.
    It then checks the database to see wether the user has already liked that post or not.
    If user has liked the post from befoire then it updates the databse and changes the liked
    status to not liked and reduces the like count
    and if user has never liked the post before then it changes the liked status to liked and increases the liked ocunt.

6.  search function searches for a post that has the letters entered by the user in the search bar
    from the database and then displays it on the dahboard.

7.  sort function retreives data from the databse either in ascending ir descending order
    of like count and displays it on the dashboard in that order.

8.  viewpost function enlarges that specific post and it also shows all the comments
    made under that post on the right side of the screen.

9.  comment function enters a comment into the databse made by the user under a post.

10. myprofile function displays only all the post entered by that user,
    all the posts liked by the user,
    all the comments made by the user.

11. delete function deletes a post or a comment from the comment and updates the web page.
    if a post deleted then it also deletes its like count, like status from every user who
    has liked that post and also deleted all the comments made under that post.

12. logout function logs out user.

helpers

1. Renders the apology template with appropriate message.

2. ensures that only logged in users can access certain URL's,


**Javascript**
script.js
1. It sends and api call to the server so that server can get the id post whose like/dislike
    button was clicked. It then receives the liked status that is wether user has liked the post
    or disliked their previously liked post.
    if the post was already liked then it changes the svg icon from liked to disliked
    and if the post was disliked from before then it changes the svg icon from disliked to liked.

2. It sends an API call tp the server to tell the server wether user wants to delete
    their post or a comment. It then receives a confirmation from the server the the post/comment has been deleted.
    It then refreshes the page by changing the web pages location so that the post/comment no longer appear on the screen.


**CSS**
styles
In this file the register page, login page, dashboard is designed using pure css

styles2
In this file the viewpost page is designed using pure css


dislike.svg is the dislike svg image src(https://www.flaticon.com/free-icon/favorite-heart-button_60993)
like.svg is the like svg image src(https://www.flaticon.com/free-icon/heart_126471)
rubbish-bin-svgrepo-com.svg is the delete svg image src(https://www.veryicon.com/icons/miscellaneous/godserver/delete-323.html)




**HTML**

1.  apology page is displayed with appropriate error message when user enters something invalid
    like incorrect username or password or using an already existing username


2.  dashboard01 page is the home page of the user. It harbours all the posts made by the user.
    It displays name and username of all the users that created the posts. It also has a like button.
    It has a search section at the top of the page and a upload section at the post.
    User can also navigate to their profile page and can even log out from the dashboard page.

3.  layou01 is the basic layout of all the pages. It displays at the top right corener
    the Register and login button when no user is logged in and Home, myprofile, logout 
    button when a user loggedin.
    It also has the main div element of the body which is modified by different page as per their requierments.

4.  login page has the username and password text boxx for the user to enter their credentials 
    so that they can be logged in. It uses the extension of layout01

5.  myprofile page has a row at the top which has three sections my posts, liked, comments.
    my posts displays all the posts made by the user.
    liked displays all the liked post.
    comments displays all the comment made by the user. It uses the extension of layout01.

6.  post page displays and enlarged of the post which was clicked and it also
    shows the comments made other user under that post.
    It has an add comment box under the section which displays all the comments.

7.  register page has a name box, username box, password box and confirm password box 
    and a submit button. It allows the user to enter their credentials so that they can 
    be registered into the database.



    
___