#!/bin/bash
awk -F: '{print $1":"$6}' /etc/passwd | sort
