## Gitea Issues Exporter
A small python program that fetches Gitea issues (from a given organization/repo) and exports to CSV (Excel).

Currently, only issue title is exported. This can be easily adjusted, though (in `dump_to_csv` method).

## How to run
1. Install python if not yet installed. I'm using `python3.9`. 
2. Prepare Gitea access token. This be easily obtained in your Gitea *Settings >> Applications >> Manage Access Tokens* section.
3. Make sure you have `giteapy` pip package installed (if not, just go to https://pypi.org/project/giteapy/ and easily install this great python lib). 
4. Modify the `main.py` top part of the code with basic config variables, such as Gitea access token, repo name, organization name and Gitea URL.
5. Just run the python program from command line (or IDE if you use) - `python3.9 main.py`.
6. The program will generate `open_issues.csv` and `closed_issues.csv` in the same directory as main.py.

Enjoy. Hope it helps someone.