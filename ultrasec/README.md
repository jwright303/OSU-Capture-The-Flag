# Challenge Description
The challenge starts with a download link for an executable file: http://chal.ctf-league.osusec.org:1337/static/ultrasecure</br>

When executing the linux executable we are first prompted to repeate a random nonce that is supplied to us in under 0.05 seconds. If we are able to do this we are then asked to supply the password to unlock the vault and access the key. At this point the flag will be printed out to us.

### Needed Software
The software needed for this challenge is pwntools and ghidra. We will use ghidra to reverse engineer the executable, and pwntools to write our exploit.

### Ghidra
As mentioned, ghidra will be used to reverse engineer the executable. Oppening the supplied executable in ghidra we can find a few important functions. Starting with main we see it calls the check_password() function. The check_password fucntion is shown below. </br>
![Screen Shot 2022-01-11 at 9 05 43 PM Small](https://user-images.githubusercontent.com/41707123/149067305-d62f4330-df53-4b83-9e7a-174dfe1cf160.jpeg)</br>
As mentioned before we first need to quickly respond with the nonce, then supply the password for the "ultrasecure tm vault".

We can see by the screenshot that the variable holding the password is -0x, which is the signed version of 0xdeadb33f. Using all this we can create a pwntools script to automate the exploitation. 

### Running the code
To run the code simple type: ```python ultrabreaker.py```

The output will display the flag: osu{d3c0mp1ler_go_brrrr}
