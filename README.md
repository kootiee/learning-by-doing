# Learning By Doing

This is the main repository for our Learning By Doing sessions (a.k.a. The Dojo Of Doom). You'll be working in your own forks, and pulling updates from this repository.

## How to start

1. Get thee to thy terminal! 
2. `cd` to a nice directory, "documents", "projects", something like that.
3. Type the following:
```bash
git clone https://github.com/the-riviera-kid/dojo-of-panic.git
```
  * This will create a new folder, containing everything in this repository.

## How to build a Virtual Environment

This is a one-time setup.

1. In the terminal, ensure you are at the top level of this repository.
2. Run the following:
```bash
virtualenv -p python3 venv
```

## How to activate your Virtual Environment

This must be done __every time__ you want to run your programs.

1. In the terminal, ensure you are at the top level of this repository.
2. Run the following:
```bash
. venv/bin/activate
```
  * Your terminal prompt should now start with `venv`, to show you it is active.
# The Most Basic Git Basics

Whole books have been written on git, and at some point, [reading one is a good idea.](https://git-scm.com/book/en/v2) However, what you need to know right now is:
* Git is a version control system. Rather than most programs where you only keep one version of a file, git lets you keep many. So, in Word, if you save your file, you overwrite the previous version, and you hope your new one is better. In Confluence, if you update a page, you can still see all the previous versions, and can go back to any of them if you need to. Git does that second thing, for your entire collection of source code.
* Your collection of code is called a *repository*. You can have several copies of the same repository, owned by different people; that's called *forking*. You all forked my repository, and now you're working in your own copies.
* You have a local copy of your fork on your machines. You have a remote copy of your fork stored online at the Github website.
* If you want to update your repository (i.e. "save" your project), there are three steps to follow to update your local repo. There is an additional step to send the changes to Github.

1. Decide what to commit
2. Add that work to your staging area
3. Commit it
4. Push to Github (optional)

## Decide What To Commit

* In your terminal, `cd` into the top level directory of your repository. This will probably be called `learning-by-doing`.
* From here, run `git status`. It will show you what changes have been made since your last commit.

## Add Your Changes To The Staging Area

* Now, use the `git add` command to add your changes to the staging area. There are several ways to do this.
* To add *all* changes, use `git add .`
* To add a whole directory and everything in it, use `git add directory_name`
* To add a single file, use `git add path/to/my/file.txt`
* You can run `git add` many times to add many files.
* You can also combine several of these options together, like:
```bash
git add my_notes.txt secret_project_folder/ README.md
```
* If you want to check what you've added to your staging area, do `git status` again.

## Commit It

* `git commit -m "Here is a lovely message describing what I did."`
* You can now run `git status` or `git log` to see that your changes have been committed.

## Push To Github

* Open your Keepass, and get your Personal Access Token for Github ready.
* `git push`
* When prompted, enter your username.
* When prompted for your password, paste your Personal Access Token in instead.
* After this, your changes should be pushed to Github, and visible on the website.
