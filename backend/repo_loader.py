import git, os
def clone_repo(url):
    name = url.split("/")[-1]
    path = f"data/{name}"
    if not os.path.exists(path):
        git.Repo.clone_from(url, path)
    return path
