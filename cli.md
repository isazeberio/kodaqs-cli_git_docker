# Command line interface (CLI)

The command line interface (CLI) is a powerful tool for computational reproducibility. It allows you to interact with your computer in a way that is both efficient and reproducible. By using the CLI, you can automate tasks, create scripts, and run programs in a way that is consistent and repeatable.

Unlike graphical user interfaces (GUIs), which can be difficult to automate and reproduce, the CLI provides a simple and consistent way to interact with your computer. This makes it easier to create reproducible workflows and share them with others. By using the CLI, you can ensure that your work is transparent, reproducible, and easily accessible to others.

However, the CLI can be intimidating for beginners, especially those who are not familiar with programming or the command line. In this guide, we will provide an introduction to the CLI and show you how to use it to improve the reproducibility of your work.

## Setting up your CLI environment

Before you can start using the CLI, you need to set up your environment. This involves installing the necessary software and configuring your system to work with the CLI. Depending on your operating system, you may need to install a terminal emulator.

* On macOS, you can use the built-in Terminal app, or even better, install [iTerm2](https://iterm2.com/), which is a more feature-rich terminal emulator.

* On Linux, you can use the built-in terminal emulator for your distribution.

* On Windows however, although there exists the built-in Command Prompt or PowerShell, in order to have a consistent experience and make sure your work is reproducible cross-platform, you should install WSL (Windows Subsystem for Linux) and use a Linux distribution such as Ubuntu.
To install WSL, follow the instructions [here](https://docs.microsoft.com/en-us/windows/wsl/install).

## Basic CLI commands

The basic usage of the CLI involves typing commands and pressing `Enter` to execute them. Commands are usually followed by options and arguments that modify their behavior. Now we illustrate some of the most common commands you will use in the CLI.

To get the running example we use throughout this session, clone the repository [kodaqs-cli_git_docker](https://github.com/yfiua/kodaqs-cli_git_docker) by running the following command in your terminal (make sure you have `git` installed. Alternatively, you can download the repository as a zip file from the GitHub page, extract it to a directory of your choice)
, and enter the directory `kodaqs-cli_git_docker`:

```sh
git clone https://github.com/yfiua/kodaqs-cli_git_docker
cd kodaqs-cli_git_docker
```

### Navigating the file system

In one of the previous sessions "Computer literacy 101", we introduced the concept of the file system and how files and directories are organized on your computer. In this session, we will show you how to navigate the file system using the CLI.

The CLI provides a number of commands that allow you to navigate the file system. Here are some of the most common commands:

- `pwd`: Print the current working directory

Typing `pwd` and pressing `Enter` will show you the full path of the directory you are currently in. This is useful for keeping track of where you are in the file system.

In the example below, the output of `pwd` is `/home/yfiua/kodaqs-cli_git_docker`, which means that the current working directory is the home directory of the user `yfiua`.

- `ls`: List the contents of the current directory

Typing `ls` and pressing `Enter` will show you a list of all the files and directories in the current directory. This is useful for getting an overview of what is in the directory.

In the example below, the output of `ls` shows that there are some files including `cli.md`, `LICENSE` and `README.md` in the current directory. Note the exact output may vary from the screenshot.

Combine `ls` with the `-l`, `-s` and `-a` flags to get more detailed information about the files and directories, such as permissions, ownership, size, and modification date, and to show hidden files. In the example below, the output of

```sh
ls -als
```

shows the hidden directory `.git` in the current directory. More information about the flags can be found in the manual pages of the `ls` command by typing `man ls`.

- `cd`: Change the current directory

Typing `cd` followed by the name of a directory and pressing `Enter` will change the current directory to the specified directory. You can use both relative and absolute paths with the `cd` command.

For example, typing

```sh
cd ..
```
will move you up one level in the directory structure.
Then typing

```sh
cd kodaqs-cli_git_docker
```

will take you back to the directory you were in before.

### Creating, moving, and deleting files/directories

The CLI also provides a number of commands that allow you to create, move, and delete files and directories.
For beginners, it is recommended to first combine the use of the CLI with a GUI file explorer. This way, you can get a better understanding of how the CLI commands correspond to the actions you perform using the GUI. For example, you can create a new directory using the GUI file explorer and then try to replicate the same action using the CLI.

- `mkdir`: Create a new directory

Typing `mkdir` followed by the name of a directory and pressing `Enter` will create a new directory with the specified name in the current directory.

In the example below, the command

```sh
mkdir example
```

creates a new directory called `example` in the current directory.
Use `cd example` to move into the newly created directory.

- `cp`: Copy a file or directory

Use the `cp` command to copy a file or directory. The syntax is `cp source destination`. As usual, you can use both relative and absolute paths.

In the example below, you are in the working directory `kodaqs-cli_git_docker/example` you just created. You can copy the `README.md` file from the parent directory to the current directory using the command

```sh
cp ../README.md README.md
```

To copy a directory and its contents, use the `-r` flag with the `cp` command. Now we will copy the `example` directory to a new directory called `example_copy` using the command

```sh
cd ..
cp -r example example_copy
```

Use `ls example_copy` to verify that the directory was copied successfully.

- `mv`: Move a file or directory

Use the `mv` command to move a file or directory. The syntax is `mv source destination`. Note that the `mv` command can also be used to rename files and directories. Be cautious when using the `mv` command, as it will overwrite files if the destination already exists.

In the example below, you can move the `example_copy` directory to a new directory called `example_moved` using the command

```sh
mv example_copy example_moved
```

You do not need to use the `-r` flag with the `mv` command to move directories.
Use `ls example_moved` to verify that the directory was moved successfully.

- `rm`: Remove a file or directory

Use the `rm` command to remove a file or directory. Be cautious when using the `rm` command, as it will permanently delete files and directories without moving them to the trash.

To remove a file, use the command `rm filename`. For example, to remove the `README.md` file, use the command

```sh
rm example_moved/README.md
```

Use `ls example_moved` to verify that the file was removed successfully.
To remove a directory and its contents, use the `-r` flag with the `rm` command. For example, to remove the `example_moved` directory, use the command

```sh
rm -r example_moved
```

Use `ls` to verify that the directory was removed successfully.

### Viewing file contents

- `cat`: View the contents of a file

The `cat` command is used to view the contents of a file. The syntax is `cat filename`. For example, to view the contents of the `cli.md` file, use the command

```sh
cat cli.md
```

Besides `cat`, there are other commands that can be used to view file contents, such as `less`, `more`, and `head`.

- `less`: View the contents of a file page by page

`less` is faster for large files because it does not load the entire file into memory. The syntax is `less filename`. For example, to view the contents of the `cli.md` file page by page, use the command

```sh
less cli.md
```

Use the navigation keys `Up`, `Down`, `Page Up`, and `Page Down` to scroll through the file. Press `q` to exit `less`.

- `head` and `tail`: View the first or last few lines of a file

The `head` and `tail` commands are used to view the first or last few lines of a file. The syntax is `head filename` and `tail filename`, respectively. For example, to view the first or last few lines of the `cli.md` file, use the command

```sh
head cli.md
tail cli.md
```

You can specify the number of lines to display by using the `-n` flag with the `head` and `tail` commands. For example, to view the first or last 10 lines of the `cli.md` file, use the command

```sh
head -n 10 cli.md
tail -n 10 cli.md
```

## Creating your own scripts

One of the key benefits of the CLI is the ability to create shell scripts that automate tasks and workflows. By writing scripts, you can ensure that your work is consistent, reproducible, and easily shareable with others.

To create a script, you need to write a series of commands in a text file and save it with a `.sh` extension, for instance `script.sh`. You can then run the script from the CLI by typing `sh script.sh`, with possible arguments.

Below is an example of a script that performs a simple text analysis task: it takes a file as input and counts the number of lines in a file, as well as the number of lines containing a specific "word" (case-insensitive, can be a substring).

```sh
#!/bin/sh

echo "Number of lines in $1:" $(wc -l < $1)
echo "Number of lines containing '$2' in $1:" $(grep -ci $2 $1)
```

Save the script to a file called `word-count.sh`. You can then run the script from the CLI by typing, for instance,

```sh
sh word-count.sh cli.md cli
```

## Running programs from the CLI

In addition to creating and running your own shell scripts, you can also run programs from the CLI. This is useful for running programs that do not have a graphical user interface or for running programs in batch mode.

To run a program from the CLI, you need to know the name of the program and any options or arguments that it requires. You can then type the name of the program followed by the options and arguments and press `Enter` to run the program.

The Python script `character_count.py` is available in the `kodaqs-cli_git_docker` repository. It takes a file as input and counts the occurence of characters A-Z in the file and plots a histogram of the character counts.

To run the script, you need to have Python 3 and the `matplotlib` library installed on your system. You can run the script from the CLI by typing, for instance,

```sh
python3 character_count.py cli.md
```

Note: Always check the documentation of the program you are running to ensure that you are using the correct options and arguments.
ALWAYS be cautious when running programs from the CLI, especially if you are not familiar with the program or its options. Incorrect usage of programs can lead to data loss.
