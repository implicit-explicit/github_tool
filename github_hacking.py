#! /usr/local/bin/python3
__author__ = 'mrmrcoleman'

from github import Github
import inspect

g = Github("mrmrcoleman", "Mumsmaiden3")

stargazers = {}
count = 0

for stargazer in g.get_repo('mesosphere/elasticsearch-mesos').get_stargazers():
    count += 1
    if(stargazer.email != None):
        stargazers[stargazer.name] = stargazer.email
        print("{}, {}".format(stargazer.name, stargazer.email))

print("Found {} emails out of {} stargazers. {} percent.".format(len(stargazers), count, len(stargazers)/count))