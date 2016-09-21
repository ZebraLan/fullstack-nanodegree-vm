#
# Database access functions for the web forum.
#

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
    query = 'select * from posts order by time desc;'

    c.execute(query)
    posts = c.fetchall()

    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    query = 'insert into posts values (%s, default, default);' % content

    c.execute(query)
    DB.commit()
