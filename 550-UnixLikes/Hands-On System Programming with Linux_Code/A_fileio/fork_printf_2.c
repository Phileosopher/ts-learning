/*
 * ch7:fork_printf_2.c
 ***************************************************************
 * This program is part of the source code released for the book
 *  "Hands-on System Programming with Linux"
 *  (c) Author: Kaiwan N Billimoria
 *  Publisher:  Packt
 *
 * From:
 *  Ch 7 : File IO Essentials
 ****************************************************************
 * Brief Description:
 * First call printf(3), then fork(2); that's it.
 * (Read chapter 7 and see ch7/fork_printf_1.c to get the point :-).
 * For details, please refer the book, Ch 7.
 */
#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <string.h>
#include <unistd.h>
#include "../common.h"

int main(int argc, char **argv)
{
	printf("Hello, world. ");
	fork();
}

/* vi: ts=8 */
