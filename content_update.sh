#!/bin/bash 
python _blogApp/blog.py build ;
git add * ;
git commit -m "modify article and generate static files" ;
git push origin master ;
