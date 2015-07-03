#!/bin/bash 
python _blogApp/blog.py build ;
git add * ;
git commit -m "regenerate static files afiter updating idex and hire pages" ;
git push origin master ;
