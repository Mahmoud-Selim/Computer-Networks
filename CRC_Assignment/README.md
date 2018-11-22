# CRC
Implemention of  an error-detection mechanism using the standard CRC algorithm by python 

## Description
The generator Program :  reads from standard input a line of ASCII text
containing an m-bit message consisting of a string of 0s and 1s. The
second line is the k-bits polynomial, also in ASCII. It outputs to
standard output a line of ASCII text with (m+k) 0s and 1s representing
the message to be transmitted. Then it outputs the polynomial, just as
it read it in.

The verifier program : reads in the output of the generator program and
outputs a message indicating whether it is correct or not.

Alter  : function that simulates error by inverting 1 bit on the first line
depending on its argument (the bit number counting the leftmost bit
as 1) but copies the rest of the two lines correctly.
By typing 

## Getting started 
manual.pdf will get you a copy of the project up and running on your local machine for development and testing purposes

## Created by 
```
Team leader :Mahmoud Ahmed Selim
Members : Youmna Ebrahim Helmy 
        : Mohamed Gamal El said
        : Mohamed Osama Mostafa
