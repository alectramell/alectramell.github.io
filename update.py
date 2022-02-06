import os
import sys
from git import Repo

repo = Repo('.')

#repo.index.add(['*'])
repo.index.commit('index-updates')
origin = repo.remote('origin')
repo.git.push('origin')