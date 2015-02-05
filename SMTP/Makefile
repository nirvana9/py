sendmail: sendmail.c
	gcc -std=c99 -Wall `libesmtp-config --cflags`   -o sendmail sendmail.c -lesmtp
clean:
	rm sendmail
