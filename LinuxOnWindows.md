# Linux on Windows

## 2018

### December

Building a pdf with Sphinx

Prerequisites

Install the following three packages for Ubunutu on Windows Sub system:

```
$ sudo apt-get install texlive-latex-recommended
$ sudo apt-get install texlive-latex-extra
$ sudo apt-get install texlive-fonts-recommended
```
The first two packages do take at least 20+ minutes to install. The final package may not have anything to update. 

After these packages install, update the sub system:

$ sudo apt-get update

With these packages installed, when you have completed the ``index.rst`` file, and added in the other documents, build the 
latex files with the following command:

$ make latex

Next, now that the latex files are ready to go, Sphinx can then build a pdf. Run the following command:

$ make pdflatex

This will take several seconds. Text will scroll past on the command line as Sphinx assembles all the latex files. When the 
build is finished, the pdf file can be located inside the /build/latex/*.pdf directory.

### November

I have been using Linux on Windows. It works, but the experience can be improved with troubleshooting content. For example what to do if you 
start out using Linux Bash on Windows, set up the Sudo account and password, but forget the credentials, and neglect to set up them up in
a password credential handler. 

Users can access a shadow file to adjust User and Root user, and change the password. 

Windows users can locate the shadow file, adjust the user hash string, re-open bash, switch to the sudo user, change the password, and then switch back to the
regular user. 

The instructions I adapted were in the following stack exchange item: https://askubuntu.com/questions/772050/reset-the-password-in-ubuntu-linux-bash-in-windows 

TODO:
Write instructions on how to access the shadow file.

