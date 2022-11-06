# Scripts for analysis logs nginx

Repo has 2 sripts for analysis written on python and bash.
Analysis only log file in this dir with name access.log
### In every solved tasks:
1. Total requests by type;
2. Top 10 most frequent requests;
3. Top 5 largest requests that failed in a client 4XX error.<br>
Also bash script output count request.
### Output format
Bash script output only analysis_logs_sh.txt
Python script output analysis_logs_py.txt or analysis_logs_py.json, depending on whether or not flag --json is 
specified at startup.
### Getting start
For run bush script `./script.sh`<br>
For run python script `python script.py` for save result in .txt and `python script.py --json` for save in .json

