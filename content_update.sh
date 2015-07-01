#!/bin/bash 
python _blogApp/blog.py build ;
git add * ;
git commit -m "global update" ;
git push origin master ;