#!/bin/sh

cd /home/rolles/server/
echo "=================="
echo "Selenoid reload..."
echo "=================="
./cm selenoid stop
./cm selenoid-ui stop

./cm selenoid start
./cm selenoid-ui start
echo "=================="
echo "Selenoid reloaded"
echo "=================="