# OTUS_Logs_Parsing
Parsing logs and save result as json file.
The following information is represented as a result:
- General number of requests in logs;
- Amount of requests divided by request method;
- Top 10 IP addresses the most amount of requests made from;
- Top 10 requests for which the most time was spent;
- Top 10 requests which ended with client error;
- Top 10 requests which ended with server error.

## Run
```bash
python get_stat.py [--path_to_logs/-ptl] [--path_to_report/-ptr]
```
In <path_to_logs> provide path to a specific file with logs or to a folder with log file(-s).

In <path_to_report> provide path to a **folder** where report should be generated.

## Example
```bash
python get_stat.py --path_to_logs=Logs_to_test\logs.txt --path_to_report=Logs_to_test\ $ Windows

python get_stat.py --path_to_logs=Logs_to_test/logs.txt --path_to_report=Logs_to_test/ $ Linux
```