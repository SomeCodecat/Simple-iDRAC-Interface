@echo off

cd "path\to\the\folder\containing\both\sii\versions"

if "%1"=="" goto No1
if "%1"=="-nocolor" goto No2
if "%1"=="-n" goto No2
if not "%1"=="-nocolor" echo Unknown argument
if not "%1"=="-nocolor" goto End1
if not "%1"=="-n" echo Unknown argument
if not "%1"=="-n" goto End1


:No1
py sii.py --arguments %*
goto End1

:No2
    py sii-nocolor.py --arguments %*
goto End1

:End1