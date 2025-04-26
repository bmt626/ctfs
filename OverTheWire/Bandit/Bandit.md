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
### Goal
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