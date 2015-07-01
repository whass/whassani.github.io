#!/bin/bash 
python _blogApp/blog.py build ;
git add * ;
git commit -m "add posts" ;
git push origin master ;
