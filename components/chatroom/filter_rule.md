## rules for sql injection ##
this WAF aims to handle attacks gracefully,at this stage   
our website should be able to handle xss attack and sql injection.  
As for sql injection,this could be found on login and registration  
section.Therefore,the most efficiency approach is to find check   
if there are some "dangerous" characters from the input.The solution is   
reject any query that contains [.\\+?-;=/] and space characters,and make a series of limitations on the  
size of username and password.  
To be specific,the length username must in the range of 5 to 16,   
the password should contain lowercase,uppercase and the size must in the range of 8 to 16.

## rules of xss attack ##
as for the properties of our website,the only place which needs to be care of
csrf attack is the discussion forum and from the url (since all the request of our website is post,so it is not needed)
invalid url will be redirect to 404 error page.   
we replace "<" and ">" by "&lt;" and "&gt;" in the user input section,
after a series of testing,it works totally fine.

