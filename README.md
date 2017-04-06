# Unique words & Top tweet times

The purpose of these two map reduce programs are to determine the unique/duplicate words used in the data set of tweets and determine
the time periods when people are most commonly tweeting. The first part corresponds to the map.py and reduce.py and the other two files
to the second part. For the second analysis it assumes certain time intervals for the posting becaues it is more informative to look
at a time interval than tweets that happen to have been posted on the exact same second of the day. It doesn't take into consideration 
the day/month/year only when a tweet is posted in a 24 hour period. The user can define how long each time period is in minutes and the
program will give the top ten most popular time interval tweets were posted. This implementation used the hadoop streaming library,
although not included in this repo.
