To access the Bandit server you will need to ssh into the server using the username bandit and the level number `bandit#` 

The servers game is located on port 2220 and the server name is `bandit.labs.overthewire.org`

the password for each level is found by completing the previous level (completed level passwords are stored in the `Bandit Passwords` note)

example Linux ssh command to access level 0
`ssh bandit0@bandit.labs.overthewire.org -p 2220`

### Level 0
#### Goal
The goal of this level is for you to log into the game using SSH. The host to which you need to connect is **bandit.labs.overthewire.org**, on port 2220. The username is **bandit0** and the password is **bandit0**. Once logged in, go to the [Level 1](https://overthewire.org/wargames/bandit/bandit1.html) page to find out how to beat Level 1.

### Level 0 --> 1
#### Goal
The password for the next level is stored in a file called **readme** located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.
#### Solution
`cat readme` to obtain password

### Level 1 --> 2
#### Goal
The password for the next level is stored in a file called **-** located in the home directory
#### Solution
In Linux the `-` (dash) operator is used as **redirection from/to stdin or stdout** 
**example** 
`**echo "whatever" | cat -**`

In order to read a file called `-` you need to use either the full path or use the `<` redirect
**example**
`cat < -`
`cat ./-`

### Level 2 --> 3
#### Goal
The password for the next level is stored in a file called **spaces in this filename** located in the home directory

#### Solution
You have to cat the file but the command line does not handle spaces well so you need to use an escape character `\` to tell the system to treat this next character a text character and not its typical use

`cat spaces\ in\ this\ filename `

### Level 3 -- > 4
#### Goal
The password for the next level is stored in a hidden file in the **inhere** directory

#### Solution
In Linux files that start with a dot `.` are hidden in `ls` output unless you specify you want to list all files including hidden ones with the `-a` option

- Get the name of the hidden file by listing the contents of the `inhere` directory
	`ls -a` or `ls -la`

- Now that we have the name of the file we can read the contents with `cat`
	 `cat inhere/...Hiding-From-You`

### Level 4 --> 5
#### Goal
The password for the next level is stored in the only human-readable file in the **inhere** directory. Tip: if your terminal is messed up, try the “reset” command.

#### Solution
To avoid having to open up every file which as the goal suggest not every one will be human readable we can use the `file` command to determine the type of the file we pass to it. 
We can have they system give us the type for all of the files in the directory at the same time.

- Use the `file` command to list the type of each file
	`file inhere/*`
	![[Pasted image 20250426160424.png]]
	
- Now that we know which file is human readable `ASCII text` we can `cat` just that file  to get our password
	`cat inhere/-file07`

### Level 5 --> 6
#### Goal
The password for the next level is stored in a file somewhere under the **inhere** directory and has all of the following properties:

- human-readable
- 1033 bytes in size
- not executable

#### Solution
This time a simple find command wont cut it inside of `inhere` there are several directories each with their own files inside of them
We need a better solution enter the `find` command

- Using the find command we can narrow down where our desired file lives
	`find DIRECTORY_TO_SEARCH -type f -size ###X`
	`-type f` will display files
	`-size` will allow us to specific the size of the file we want to search for where X is replaced with one of the following
	`k` kilobytes
	`M` megabytes
	`G` gigabytes
	`c` bytes
	
	`find inhere/ -type f -size 1033c` this will search in the `inhere` directory and all of the sub directories inside of it for files that are 1033 bytes
	![[Pasted image 20250426172156.png]]
- We can further ensure we have the right type of file by running the file command on the found file
	`file inhere/maybehere07/.file2`
	![[Pasted image 20250426172323.png]]
- Finally we can `cat` the file to obtain the password

### Level 6 --> 7
#### Goal
The password for the next level is stored **somewhere on the server** and has all of the following properties:

- owned by user bandit7
- owned by group bandit6
- 33 bytes in size

#### Solution
- Using the find command again we can further expand upon what was used last time and add `-user bandit7` and `-groupd bandit6` to find files that are owned by the users bandit7 and the group bandit6 thus meeting our requirements of the goal
- This time however we are going to search the whole system which can generate errors on files we dont have permissions to view to avoid display these files in our output we can redirect errors from the standard output of our screen to `/dev/null` meaning send them no where this is accomplished by adding `2>/dev/null` to the end of our find command

`find / -type f -size 33c -user bandit7 -groupd bandit6 2>/dev/null`

![[Pasted image 20250427112046.png]]

- Now we can cat that file to obtain our password

### Level 7 --> 8
#### Goal
The password for the next level is stored in the file **data.txt** next to the word **millionth**
#### Commands you may need to solve this level

[man](https://manpages.ubuntu.com/manpages/noble/man1/man.1.html), grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

#### Solution
Using `grep` we can search inside of text to display the lines where our search string exists in the output 
In Linux we can `|` pipe the output of one command into another in this case `cat` the `data.txt` file and `|` it into `grep`

`cat data.txt | grep millionth`
![[Pasted image 20250427113445.png]]

### Level 8 --> 9
#### Goal 
The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once

#### Solution
This time we need to use a few new commands in order to find the password
we can use the `uniq` command to find only the unique lines with the `-u` flag but `uniq` only works when duplicate lines are grouped together as it only looks at the lines before it so we have to `sort` them first 

`sort data.txt | uniq -u`
![[Pasted image 20250427144850.png]]

### Level 9 --> 10
#### Goal
The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several ‘=’ characters.

#### Solution
`strings data.txt`

### Level 10 --> 11
#### Goal
The password for the next level is stored in the file **data.txt**, which contains base64 encoded data
#### Solution
Use the `base64` command with the `-d` flag to decode the b64 after piping it from the `cat` command

`cat data.txt | base64 -d`

![[Pasted image 20250427151855.png]]

### Level 11 --> 12
#### Goal
The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

#### Solution
Easiest way is to use cyberchef and paste the contents of `data.txt` and use the rot13 function, but to do this from with in our ssh session we can use the following 

```bash
cat data.txt | tr "$(echo -n {A..Z} {a..z} | tr -d ' ')" "$(echo -n {N..Z} {A..M} {n..z} {a..m} | tr -d ' ')"
```
![[Pasted image 20250427153206.png]]

### Level 12 --> 13
#### Goal
The password for the next level is stored in the file **data.txt**, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)
#### Commands you may need to solve this level

grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd, mkdir, cp, mv, file
#### Solution
This level revolves around a lot of layers and converting files from one type to another and decompressing them  to finally get back to the plain text

- create a tmp directory and cd to it to begin working
	`cd $(mktemp -d)`
- copy the file to the directory
	`cp ~/data.txt .`
- reverse the hex dump into a binary and use file to determine the data type
	`xxd -r data.txt | file -`
	![[Pasted image 20250427222110.png]]
- now convert the hex to a gz file 
	`xxd -r data.txt > data2.gz`
- now uncompress the gzip file and determine the file type of the decompressed file
	`gzip -d data2.gz`
	![[Pasted image 20250427222711.png]]
- now decompress the bzip2 file
	`bzip2 -d data2`
	![[Pasted image 20250427223118.png]]
- determine the file type of the resulting file
	`file data2.out`
	![[Pasted image 20250427223216.png]]
- now that we know it is a gz file lets rename the file from .out to .gz so gzip is not angry 
	`mv data2.out data3.gz`
	`gzip -d data4.gz`
- running file on the resulting file gives us the following `POSIX tar archive (GNU)` with that we can use tar to extract the next file
	`tar -xvf data4`
- this extracts a file called `data5.bin` which according to the file command is also a tar archive
	`tar -xvf data5.bin`
- again running file on `data6.bin` results in a bzip2 file
	`bzip2 -d data6.bin`
	![[Pasted image 20250427223957.png]]
- run tar on this archive
	`tar -xvf data6.bin.out`
	![[Pasted image 20250427224127.png]]
- rename the file to data8.gz and uncompress
	`mv data8.bin data8.gz && gzip -d data8.gz`
	![[Pasted image 20250427224319.png]]
- Finally we have reached a plain text file that should be our password
	`cat data8`
	![[Pasted image 20250427224441.png]]