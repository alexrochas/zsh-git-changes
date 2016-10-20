# ZSH-Git-Changes
> ZShell plugin for invoke difftool on lastchanges

The main purpose of this plugin is to show based on git reflog the differences between commits after you call a **git pull**.
This way you will be able to see diferences from your repo and the pulled origin code.

## Installation with [antigen](https://github.com/zsh-users/antigen)

Add to your .zshrc

```sh
antigen bundle alexrochas/zsh-git-changes
```

## Usage example

After a **git pull**

```
~$ git-changes
```

And you configured default difftool will be invoked.

Also, by default, if not after pulling code from remote, git-changes will made diff between the last two registers in **reflog**. 

## Roadmap

* Explicity behavior with parameters (like -p for search diff between pulled code and state before pull)

## Release History

* 0.0.1
    * Work in progress.

## Meta

Alex Rocha - [about.me](http://about.me/alex.rochas)
