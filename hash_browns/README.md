# Challenge Description
The challenge starts of with a link to a website: http://chal.ctf-league.osusec.org:31337
Using this link and some of the hints on the website we need to find a flag in the form of osu{n0t_a_fL4g}

Uppon landing on the webpage we find a text box with a animated submit button and the hint to inspect it

Once we inspect element and make our way to the source file we can find the javascript responsible for checking the user input. Here we find a hash of the password we need to guess.
On this page we can see the hashing algorithm that is used is sha-256. Using this information along with a passwords file such as rockyou.txt we can attempt to brute force to find the password.

## Running the code
Before running the code make sure you have access to a password list such as rockyou.txt
Similarly, the pycryptdome package also needs to be installed beforehand

To run the code type:
```python hashcarack.py [path to password list] [hash to be broken]```

## Results
Once the program finds the password whose hash matches the one supplied in the command line the password will be printed to the screen.
In our case the password was: pineapple.
Now we can go back to the Hash Browns website we started with and enter the password pineapple.
Entering in the password takes us to a new webpage with a link bouncing around the screen. </br>
At 

Clicking on this reveals the flag: osu{p1n34ppl3_h45h_Br0wN5_4r3_g00D}
