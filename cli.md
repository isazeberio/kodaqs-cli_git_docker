# CLI

## Importance of CLI in the context of computational reproducibility

The command line interface (CLI) is a powerful tool for computational reproducibility. It allows you to interact with your computer in a way that is both efficient and reproducible. By using the CLI, you can automate tasks, create scripts, and run programs in a way that is consistent and repeatable.
Unlike graphical user interfaces (GUIs), which can be difficult to automate and reproduce, the CLI provides a simple and consistent way to interact with your computer. This makes it easier to create reproducible workflows and share them with others. By using the CLI, you can ensure that your work is transparent, reproducible, and easily accessible to others.

However, the CLI can be intimidating for beginners, especially those who are not familiar with programming or the command line. In this guide, we will provide an introduction to the CLI and show you how to use it to improve the reproducibility of your work.

## Setting up your CLI environment

Before you can start using the CLI, you need to set up your environment. This involves installing the necessary software and configuring your system to work with the CLI. Here are some steps you can take to set up your CLI environment:

First, depending on your operating system, you may need to install a terminal emulator.

On macOS, you can use the built-in Terminal app, or even better, install [iTerm2](https://iterm2.com/), which is a more feature-rich terminal emulator.

On Linux, you can use the built-in terminal emulator for your distribution.

On Windows however, although there exists the built-in Command Prompt or PowerShell, in order to have a consistent experience and make sure your work is reproducible cross-platform, you should install WSL (Windows Subsystem for Linux) and use a Linux distribution such as Ubuntu.
To install WSL, follow the instructions [here](https://docs.microsoft.com/en-us/windows/wsl/install).

## Basic CLI commands

### Navigating the file system

In one of the previous sessions "Computer literacy 101", we introduced the concept of the file system and how files and directories are organized on your computer. In this session, we will show you how to navigate the file system using the CLI.

The CLI provides a number of commands that allow you to navigate the file system. Here are some of the most common commands:

- `pwd`: Print the current working directory

Typing `pwd` and pressing `Enter` will show you the full path of the directory you are currently in. This is useful for keeping track of where you are in the file system.

In the example below, the output of `pwd` is `/home/yfiua/kodaqs-cli_git_docker`, which means that the current working directory is the home directory of the user `yfiua`.

- `ls`: List the contents of the current directory

Typing `ls` and pressing `Enter` will show you a list of all the files and directories in the current directory. This is useful for getting an overview of what is in the directory.

In the example below, the output of `ls` shows that there are three files `cli.md`, `LICENSE` and `README.md` in the current directory.

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



- `mv`: Move a file or directory

- `rm`: Remove a file or directory


### Viewing file contents



Viewing file contents
Searching and filtering (e.g., grep, find)
File permissions and ownership

## Running your own scripts


