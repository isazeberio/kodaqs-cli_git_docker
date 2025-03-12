# Git

## Introduction

Git is a distributed version control system that helps track changes in code, enabling collaboration and effective management of software projects. It ensures that researchers can maintain a history of their work, experiment with different approaches, and revert to previous versions if needed.

Here we explain the basic concepts of Git.

### Repository

A repository (repo) is the basic unit that Git operates. It contains all the files and directories of a project, and their entire history.

* Local Repository: stored on your computer, can be synchronized (push / pull) to a remote repository.

* Remote Repository: hosted on a server / platform such as GitHub or GitLab, which allows multiple people to collaborate on the project.

### Commit

A commit is a snapshot of a repository at a specific point in time.
Each commit has a unique identifier and contains the changes (deletion / addition / update) made since the last commit.
You can browse the history of commits and go back to anywhere you want.

### Push and pull

* When you want to make the remote repository in sync with your local one and share your changes to others, you ***push*** the commits in the local repository to the remote one.

* The reverse action: when you want to sync your local repository with the remote repository, you ***pull*** commits from the remote repository to the local one.

### Merge and conflict

When pushing and pulling, commits are merged. When git cannot merge commits automatically, conflicts occur and must be resolved manually.

## Installation

To use Git, you need to install it on your computer. Git is available for all major operating systems.

### Windows

1. Install Git from here: <https://git-scm.com/downloads/win> (alternatively, <https://gitforwindows.org/>)
2. When asked about "Adjusting your PATH environment", make sure to select "Git from the command line and also from 3rd-party software". Everything else can be left as default

### macOS

Install Git from here: <https://git-scm.com/downloads/mac>

### Linux or WSL

Install Git via your distro’s package manager. For example, on Ubuntu:

```sh
sudo apt install git
```

More information can be found here: <https://git-scm.com/download/linux>

After installing Git, you can check if it was installed correctly by running:

```sh
git --version
```

## Setting up Git

After installing Git, you need to configure it with your name and email address. This information will be used to identify you as the author of the changes you make.

Open a terminal and run the following commands:

```sh
git config --global user.name "Your Name"
git config --global user.email your.email@example.com
```

<https://git-scm.com/book/ms/v2/Getting-Started-First-Time-Git-Setup> has more information on setting up Git, such as configuring your text editor used by Git.

## Getting a GUI (optional)

While Git can be used from the command line, there are several GUI clients available that make it easier to work with Git repositories. Some popular GUI clients are listed in <https://git-scm.com/downloads/guis>.

Git is also well integrated with many IDEs, such as Visual Studio Code, PyCharm, RStudio, and IntelliJ IDEA.

## GitHub and GitLab

GitHub (<http://github.com>) and GitLab (<http://gitlab.com>) are web-based Git repository hosting services that provide a web-based graphical interface and desktop integration. They also provide access control and several collaboration features such as bug tracking, feature requests, task management, and wikis for every project.

For GitLab, you or your organization can host your own GitLab instance. This is useful if you want to keep your code private or if you want to have more control over the server.

In this session, we will be using GitHub for our examples, since it is the most popular Git repository hosting service, and many researchers share their code there. However, the concepts we will be discussing are applicable to GitLab as well.

### Creating a GitHub account

You can use GitHub without an account and still access public repositories, but you will need an account to create your own repositories and to access private repositories.

To create an account, go to <https://github.com/signup> and follow the instructions.

### Adding an SSH key

For security reasons, it is recommended to use SSH keys to authenticate with GitHub.
The official [GitHub documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) provides a detailed guide on how to set up an SSH key, which is OS specific. Here we provide a quick run through using Linux or WSL.

To generate an SSH key, open a terminal and run the following command:

```sh
ssh-keygen -t ed25519 -C "DESCRIPTIVE-COMMENT"
```

Accept the proposal to save the key in the default location by simply pressing `Enter`, or specify a different location and filename.
You have the option to protect the key with a passphrase. This is optional (but considered best practice).

By default, the result is two files in the `~/.ssh` directory: `id_ed25519` (private key) and `id_ed25519.pub` (public key).
It is safe to share the public key, but the private key should be kept secret.

### Adding the key to ssh-agent

To use the SSH key, you need to add it to the ssh-agent, which is a program that runs in the background and stores your keys in memory.
To start the ssh-agent, you can use the following command:

```sh
eval "$(ssh-agent -s)"
```

Add your key, substituting the correct name for your key.

```sh
ssh-add ~/.ssh/id_ed25519
```

### Provide the public key to GitHub

Open the public key file you created in the previous step and copy its contents. You can do this by opening the file in a text editor or by running the following command:

```sh
cat ~/.ssh/id_ed25519.pub
```

Then, go to the URL <https://github.com/settings/keys> and click on "New SSH key". Paste the public key into the "Key" field and give it a descriptive title. Click "Add SSH key".
You can add multiple keys to your GitHub account and use them for different devices.

To test if the SSH key was added correctly, you can run the following command:

```sh
ssh -T git@github.com
```

If you see a message like "Hi username! You've successfully authenticated, but GitHub does not provide shell access.", everything is set up correctly.

### Creating a repository

To create a new repository, click on the "+" sign in the top right corner of the GitHub page and select "New repository". Alternatively, you can go to <https://github.com/new>.
Fill in the repository name, description, and choose whether it should be public or private.
As of the time of writing, GitHub offers free plans for unlimited public repositories and private repositories.
You can also add a README file, a .gitignore file, and a license.

### Forking a repository

Forking a repository means creating a copy of someone else's repository to your own account. This is useful if you want to contribute to someone else's project or if you want to use someone else's code as a starting point for your own project.

Using the repository <https://github.com/yfiua/kodaqs-cli_git_docker/> as an example, you can fork it by going to the repository URL and click on the "Fork" button in the top right corner.
The repository will be copied to your account, and you will be able to make changes to it.

### Cloning a repository

The GitHub website provides a graphical interface to view repositories.
However, to make changes to a repository, it is convienient to clone it to your local machine.

To clone a repository, click on the green "Code" button. It is preferred to use the SSH URL if you have set up an SSH key. Otherwise, you can use the HTTPS URL (note that you will need to enter your GitHub username and [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) every time you push changes to the repository).
Go to the directory where you want to clone the repository.
Then, open a terminal and run:

```sh
git clone <repository URL>
```

In the example below, we clone the repository to a directory called `kodaqs-cli_git_docker` under the current directory `mntdisk1`.

### Making local changes

After cloning the repository, you can make changes to the files in the repository.
Now we make some changes to the local repository:

* Add a new file: `newfile.txt`. Content of the file can be anything you like.

* Edit an existing file: `git.md`.

* Delete the file: `file_to_be_deleted`.

Use command `git status` to see the changes you made.

```sh
git status
```

You can see that `git.md` is modified, and `file_to_be_deleted` is deleted. However, `newfile.txt` is untracked, meaning that Git is not tracking changes to this file. To add the new file to the repository, run:

```sh
git add newfile.txt
```

Commit the changes to the repository with a descriptive message:

```sh
git commit -a -m "Add newfile.txt, edit git.md, and delete file_to_be_deleted"
```

### Pushing changes to GitHub

After committing the changes, you can push them to GitHub.
If you are collaborating with others, it is recommended to pull changes from the repository before pushing your changes to avoid conflicts:

```sh
git pull
```

If there are no conflicts, you can push your changes to GitHub:

```sh
git push
```

## References and resources

We have covered the basics of Git and GitHub in this session. There are many more advanced features and best practices that you can learn to make the most out of Git and GitHub, for example branching, merging, rebasing, and pull requests. Here are some resources to help you learn more:

* [An introduction to Git(Hub)](https://github.com/schochastics/git_intro/tree/main) by David Schoch
* [Happy Git and GitHub for the useR](https://happygitwithr.com/) by Jenny Bryan
* [GitHub official documentation](https://docs.github.com/en)
