# Bio-Informatics
Reposity for Bio-informatics assignment

Contig Information gainer
This software is designed to gather some useful data from a collection of fasta files, it currently 

Getting Started
To Run this software you should only need to run it in a python enviroment, this was built using the anaconda version so 
should be the most stable

Prerequisites
If you plan on using the currently in beta. and use the one that exports graphs you will need the matlib package installed to use it, 
the rest of the version don't require any packages that don't come as standard, there are no commands that are used that linux should be 
able to interpret, though this has not been thoughly teseted as this was mainly built on windows system.

Installing
There is nothing to install for this unless you don't have python, if you don't this software will not to run

To get it to run on your system you will have to make a few changes to the software though they are relatively minor, as of the moment there 
is no file picker so you will have to change the repositrys
 os.chdir(r"C:/Users/james/Downloads/jam23") is where you want the file to be saved, copy the address of where you want to save it and 
 use it to replace the contents in the ""
 C:/Users/james/Downloads/jam23/*.fa" is the location where the files that will be used are found, so again replace the contents in the ""
 with your own location, though keep the /*.fa as it what detects your fasta files.
 Appart from this the rest of the software is automated and requires no input from the user
 

Built With
python - testing enviorment 
spyder - coding enviroment
Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

Versioning
For the versions available, see the tags on this repository, there are three types avaialbe the ones which are avalialbe
Stable - all inteded aspects of the software runs is stable, Beta - mostly stable though not all the functions work as inteaded
alpha - not stable, with the inteded functions still being implemented

Authors
James Main - Initial work

License
This project is licensed under the MIT License - see the LICENSE.md file for details
