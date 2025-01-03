# Git

## Introduction

Git is a distributed version control system that is used to track changes in source code during software development.

## Installation

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
The official [GitHub documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) provides a detailed guide on how to set up an SSH key. Here we provide a quick run through using Linux.

To generate an SSH key, open a terminal and run the following command:

```sh
ssh-keygen -t ed25519 -C "DESCRIPTIVE-COMMENT"
```

Accept the proposal to save the key in the default location by simply pressing Enter.
You have the option to protect the key with a passphrase. This is optional (but considered best practice).

The result is two files in the ~/.ssh directory: `id_ed25519` (private key) and `id_ed25519.pub` (public key). 
It is safe to share the public key, but the private key should be kept secret.

### Add key to ssh-agent

This is very OS specific. If you find anything not working here, check the official [GitHub documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

In a shell, check if the ssh-agent is running:

```bash
$ eval "$(ssh-agent -s)"
Agent pid 14333
```

Add your key, substituting the correct name for your key.

```bash
ssh-add ~/.ssh/id_ed25519
```

:::

### Provide the public key to GitHub

**Copy via shell:**
Open ~/.ssh/id_ed25519.pub in an editor and copy the contents to your clipboard.
Or do one of the following at the command line:

Mac OS: `pbcopy < ~/.ssh/id_ed25519.pub`
Windows: `clip < ~/.ssh/id_ed25519.pub`
Linux: `xclip -sel clip < ~/.ssh/id_ed25519.pub`

(*Linux: if needed, install xclip via apt-get or yum.*)

**Paste on GitHub**:
- Click on your profile pic in upper right corner

- Go to *Settings > SSH and GPG keys*

- Click "New SSH key"

- Paste your public key in the “Key” box. (Give it an informative title)

- Click "Add SSH key"

**Test**:
You can use
```bash
ssh -T git@github.com
```
 to test your connection to GitHub.  If you are unsure what is going on, check the [GitHub docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection). For more troubleshooting check [here](https://happygitwithr.com/ssh-keys.html).

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

To clone a repository, click on the green "Code" button. It is preferred to use the SSH URL if you have set up an SSH key. Otherwise, you can use the HTTPS URL (note that you will need to enter your GitHub username and [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) every time you push changes to the repository).
Then, open a terminal and run:

```sh
git clone <repository URL>
```

