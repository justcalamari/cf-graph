import github3

gh = github3.GitHub()
org = gh.organization('conda-forge')
with open('names.txt', 'w') as f:
    for repo in org.iter_repos():
        name = repo.full_name.split('conda-forge/')[-1]
        if 'feedstock' in name and 'feedstocks' not in name:
            f.write(name.split('-feedstock')[0])
            f.write('\n')
