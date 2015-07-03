#!/bin/bash 
python _blogApp/blog.py build ;
git add * ;
git commit -m "regenerate static files" ;
git push origin master ;
