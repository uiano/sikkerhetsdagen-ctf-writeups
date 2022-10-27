# Taskname
> Author: Solli

## Challenge

## Solution

You can get command injection by supplying input that will break the echo statement, and comment out the rest. 
However the command is still xored with some random junk. 

However, since we can get two passwords for each session we can use the first one to retrive a known string and use that to get the secret value.
This can then be used to decrypt the encrypted flag.

Echo your own string
`aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"; #`

Will look like this when injected:
`echo "aaaaaaaaaaaaaaaa"; #" | sha256sum`

Then also get the flag value:

`";cat flag.txt #`

`echo "";cat flag.txt #" | sha256sum`

Then use solve.py to bruteforce the possible flag
