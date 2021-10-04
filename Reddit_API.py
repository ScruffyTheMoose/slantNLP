# Most sports related subreddits are just reposting twitter content through screenshots and links so we'll need to look at evaluating comments on the most popular threads.
# Changes to come to this module since it is not even close to being ready for implementation.

from psaw import PushshiftAPI
import datetime

class RedditAPI:
    start_date = -1

    def __init__(self, year, month, day):
        self.start_date = datetime.date(year, month, day)

    api = PushshiftAPI()

    gen = api.search_submissions(
                                after=start_date,
                                subreddit='wallstreetbets',
                                filter=['score', 'author', 'title'],
                                limit=10,
    )

    for sub in gen:
        print(sub.author)
