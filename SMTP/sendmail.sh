#!/bin/sh

send_mail()
{
　　(for i in "ehlo luocheng" "AUTH LOGIN" "594250682@qq.com" "NirvanaKurt91" "MAIL FROM:<${1}>" "RCPT TO:<${2}>" "data";

　　 do

　　　　 sleep 1

　　　　 echo ${i}

　　　　 sleep 2

　　 done

　　 echo "from:<${1}>"

　　 echo "subject:${3}"

　　 echo "to:<${2}>"

　　　echo ""

　　 echo "${4}"

　　 echo "."

　　 sleep 2

　　 echo "QUIT")|telnet ${5} ${6}
}

send_mail "594250682@qq.com" "3063535418@qq.com" "test" "ok!" "smtp.qq.com" "25"
