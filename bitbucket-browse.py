#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  BitBucketBrowse aims to list Bitbucket repositories
#  Copyright (C) 2021  Cédric Le Dillau

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""BitbucketBrowse lists repositories

This script prints all the repository urls that can be fetched from
Bitbucket Cloud as a member of those repositories.

You have to create an App password on Bitbucket portal first to let
the script execute on your behalf.
"""

from atlassian.bitbucket.cloud import Cloud
from var_dump import var_dump

print("""BitbucketBrowse  Copyright (C) 2021  Cédric Le Dillau
This program comes with ABSOLUTELY NO WARRANTY;
This is free software, and you are welcome to redistribute it
under certain conditions; See LICENSE file (GPLv3+).
""")

# Do not store password
username = ''
while username == '':
    username = input("Enter your Bitbucket cloud username: ")

# Do not store password
password = ''
while password == '':
    password = input("Enter your app password (set in Bitbucket web interface): ")

bitbucket = Cloud(
    url='https://api.bitbucket.org/',
    username=username,
    password=password,
    cloud=True)

# Code is here (check for version/branch):
#   https://github.com/atlassian-api/atlassian-python-api/blob/master/atlassian/bitbucket/server/projects/repos/__init__.py
#
try:

    for repository in bitbucket.repositories.each(role='member'):
        #print(type(repository))
        # => pydoc 'atlassian.bitbucket.cloud.repositories.Repository'
        links = repository.get_data('links')
        for l in links['clone']:
            if 'name' in l and l['name'] == 'ssh':
                print(l['href'])
    #

except KeyboardInterrupt:
    pass
