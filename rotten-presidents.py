#!/usr/bin/env python
# coding=utf-8
# pylint: disable=C0103,C0301,C0326,W0702
"""Rotten Presidents"""

import random
import requests
import sys

APPROVAL_RATING_URL = 'https://elections.huffingtonpost.com/pollster/api/v2/charts/trump-job-approval'
MOVIE_RATING_URL    = 'https://www.rottentomatoes.com/api/private/v2.0/browse?minTomato=%d&maxTomato=%d&maxPopcorn=%d&services=amazon%%3Bhbo_go%%3Bitunes%%3Bnetflix_iw%%3Bvudu%%3Bamazon_prime%%3Bfandango_now&certified&sortBy=tomato&type=dvd-all'

def get_approval_rating():
    """Get approval rating"""

    approval = requests.get(APPROVAL_RATING_URL)
    rating = 0

    try:
        approval_data = approval.json()
        rating = approval_data['pollster_estimates'][0]['values']['hash']['Approve']
    except:
        print 'Could not get presidential approval rating'
        sys.exit(1)

    return rating

def get_movie_rating(approval_rating):
    """Get Roten Tomatoes rating"""

    tomatoes = requests.get(MOVIE_RATING_URL % (approval_rating, approval_rating, approval_rating))
    tomatoes_data = None
    movie_rating = 0
    movie_title = ''

    try:
        tomatoes_data = tomatoes.json()
        movie = random.choice(tomatoes_data['results'])
        movie_rating = movie['tomatoScore']
        movie_title = movie['title']
    except:
        print 'Could not get movie rating'
        sys.exit(1)

    return movie_title, movie_rating

def main():
    """Main function"""

    approval_rating = get_approval_rating()
    movie_title, movie_rating = get_movie_rating(approval_rating)

    print 'President Trump\'s approval rating: %d%%' % (approval_rating + 1)
    print '"%s" Rotten Tomatoes rating: %d%%' % (movie_title, movie_rating)

if __name__ == '__main__':
    main()
