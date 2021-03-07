#!/bin/sh
# ch18:query_sched_allprcs.sh
# **************************************************************
#  This program is part of the source code released for the book
#   "Hands-on System Programming with Linux"
#   (c) Author: Kaiwan N Billimoria
#   Publisher:  Packt
# 
#  From:
#   Ch 18 : CPU Scheduling
# ***************************************************************
#  Brief Description:
# Query the scheduling attributes - the scheduling policy, RT (static)
# priority and CPU affinity - of all processes currently alive on the system.
# Just a simple wrapper around chrt and taskset.
# Tip: Pipe this o/p to grep for FIFO / RR tasks..
# Also note that a multithreaded process shows up as several same PIDs.
#  (resolve these using ps -eLf - to see actual PIDs of threads).
# Refer to the book Ch 18 for further details.

for p in $(ps -A -To pid)
do
	chrt -p $p 2>/dev/null
	taskset -p $p 2>/dev/null
done

