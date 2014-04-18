#!/bin/sh
wget  https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.7-linux-i686.tar.bz2;
tar -xvf phantomjs-1.9.7-linux-i686.tar.bz2	;
cd phantomjs-1.9.7-linux-i686/bin/;
pwd=$(pwd)
echo "$PATH";
PATH=$PATH:$pwd;
export PATH;
echo "$PATH";
sudo pip install selenium