/*
 * ch11/fork1.c
 ***************************************************************
 * This program is part of the source code released for the book
 *  "Hands-on System Programming with Linux"
 *  (c) Author: Kaiwan N Billimoria
 *  Publisher:  Packt
 *
 * From:
 *  Ch 11 : Process Creation
 ****************************************************************
 * Brief Description:
 * A very quick and simple demo of the fork(2) system call.
 * For details, please refer the book, Ch 11.
 */
#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include "../common.h"

int main(int argc, char **argv)
{
	fork();
	printf("Hello, fork.\n");
	exit(EXIT_SUCCESS);
}

/* vi: ts=8 */
