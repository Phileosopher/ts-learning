/*
 * ch15/pthreads3.c
 ***************************************************************
 * This program is part of the source code released for the book
 *  "Hands-on System Programming with Linux"
 *  (c) Author: Kaiwan N Billimoria
 *  Publisher:  Packt
 *
 * From:
 *  Ch 15 : Multithreading Part I - The Essentials
 ****************************************************************
 * Brief Description:
 * Same as pthreads2.c: [a very simplistic (and slightly better than pthreads1.c)
 * 'Hello, world' for multithreading with Pthreads], plus, add a sleep() into
 * the worker routine.
 * Refer Ch 15 for details, thank you.
 */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include "../common.h"

#define NTHREADS	3

void * worker(void *data)
{
	long datum = (long)data;
	printf("Worker thread #%ld running ...\n", datum);
	sleep(30);
	printf("#%ld: work done, exiting now\n", datum);
	pthread_exit(NULL);
}

int main(void)
{
	long i;
	int ret;
	pthread_t tid;

	for (i = 0; i < NTHREADS; i++) {
		ret = pthread_create(&tid, NULL, worker, (void *)i);
		if (ret)
			FATAL("pthread_create() failed! [%d]\n", ret);
	}
#if 1
	pthread_exit(NULL);
#else
	exit(EXIT_SUCCESS);
#endif
}

/* vi: ts=8 */
