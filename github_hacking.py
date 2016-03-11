#! /usr/local/bin/python3
__author__ = 'mrmrcoleman'

from github import Github
from github import GithubException
import sys

g = Github()
target_repository = None

if len(sys.argv) != 1:
    target_repository = sys.argv[1]
else:
    print("No repository specified. Exiting.")
    exit(1)

stargazers = {}
count = 0

for stargazer in g.get_repo(target_repository).get_stargazers():
   count += 1
   if stargazer.email != None:
        stargazers[stargazer.name] = stargazer.email
        print("{}, {}".format(stargazer.name, stargazer.email))

print("Found {} emails out of {} stargazers. {} percent.".format(len(stargazers), count, len(stargazers)/count))