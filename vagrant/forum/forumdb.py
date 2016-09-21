#
# Database access functions for the web forum.
#

import time
import psycopg2

## Database connection
DB = psycopg2.connect("dbname=forum")
c = DB.cursor()

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    try:
        posts = c.execute('select * from posts order by time desc;')
    except psycopg2.ProgrammingError as e:
        print e.message
        DB.rollback()
        posts = []

    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    t = time.strftime('%c', time.localtime())
    DB.append((t, content))
