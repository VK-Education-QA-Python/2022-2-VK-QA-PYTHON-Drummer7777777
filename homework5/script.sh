echo 'Count request:' > analysis_logs_sh.txt && cat access.log | wc -l >> analysis_logs_sh.txt && echo '_____________________________________________' >> analysis_logs_sh.txt;
echo 'Count request for type:' >> analysis_logs_sh.txt && cat access.log | awk '{print $6}' | sort | uniq -c | sort -nk1 >> analysis_logs_sh.txt && echo '_____________________________________________' >> analysis_logs_sh.txt;
echo 'Top 10 popular request:' >> analysis_logs_sh.txt && cat access.log | awk '{print $7}' | sort | uniq -c | sort -rnk1 | head -n10 >> analysis_logs_sh.txt && echo '_____________________________________________' >> analysis_logs_sh.txt;
echo 'Top 5 big request:' >> analysis_logs_sh.txt && cat access.log | sort -rnk10 | awk '$9 ~ /^4/ {print $0}' | sed -n '1,5p' | awk '{print "url:"$7"\n", "status code:"$9"\n", "bytes sent:"$10"\n", "ip address:"$1"\n"}' >> analysis_logs_sh.txt;
#cat access.log | sort -rnk10 | awk '$9 ~ /^5/ {print $0}' | awk '{print $1}' | uniq -c;
