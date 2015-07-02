#!/bin/bash 
python _blogApp/blog.py build ;
git add * ;
git commit -m "change navigation bar and add my photo" ;
git push origin master ;
