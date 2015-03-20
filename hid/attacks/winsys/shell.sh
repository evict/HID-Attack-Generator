#!/bin/bash
for i in `ls -x *hid`;do
	cat $i > /dev/hidg0
	sleep 2
done
