import github3
import os

gh = github3.login(os.environ['USERNAME'], os.environ['PASSWORD'])
org = gh.organization('conda-forge')
with open('names.txt', 'w') as f:
    for repo in org.iter_repos():
        name = repo.full_name.split('conda-forge/')[-1]
        if 'feedstock' in name and 'feedstocks' not in name:
            print(name.split('-feedstock')[0])
            f.write(name.split('-feedstock')[0])
            f.write('\n')
