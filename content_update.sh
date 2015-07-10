#!/bin/bash 
python _blogApp/blog.py build ;
git add * ;
git commit -m "regenerate static files with freeze" ;
git push origin master ;
