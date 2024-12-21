import os
import subprocess
from github import Github
from github import Auth


# maindir = subprocess.check_output(["pwd"], text=True).strip()
maindir = "/home/window/codehub/Python_Programming/githubautomation/"

print(maindir)
name = input("Repo Name: ")
print(name)


with open(f"{maindir}/path.txt", "r") as file:
    path = file.read().strip()

print(f"{path}/{name}")
path = f"{path}/{name}"
os.system(f"mkdir {path}")


# read the token file
with open(f"{maindir}/mykey.txt", "r") as file:
    key = file.read().strip()
auth = Auth.Token(key)

# Connect to GitHub
g = Github(auth=auth)


user = g.get_user()
repo = user.create_repo(name)
os.system(
    f"cd {path} && git init && git remote add origin git@github.com:Acrsahil/{name}.git && git branch -M main && git status"
)
