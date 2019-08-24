# PS-Grievance

Guten tag!

#### If you're in a hurry

- Make the fork (one time)
	- Press **Fork** button from [Keshav's](https://github.com/kestal-lab/PS-Grievance) account and select your account.
	- In your GitHub fork, press **Clone or Download** and copy the url.
	- Open the terminal and: `git clone <copied_url>`
	- `git remote add upstream https://github.com/kestal-lab/PS-Grievance`

- Submiting PR
	- `git add <filename>` or to add everything `git add .`
	- `git commit -m "<Commit msg>"`
	- `git pull upstream master`
	- Resolve merge conflicts (if any) 
	- `git push origin master`
	- On your GitHub repository, press **Compare & pull request** and then **Create Pull Request** on next page


#### Creating forks

1. Press the **Fork** button (top right corner) and select your account. This will create a repository by the same name under *Your repositories*.

2. Now go to *your fork* and press the green **Clone or download** button. Copy the url that apprears in the window and open a terminal. cd into the directory where the project will reside and type the following: `git clone <url_of_your_fork>1`
This will create a directory by the name PS-Grievance there.

3. cd into the PS-Grievance directory just created and type: `git remote -v`. This should output something like:

```console
origin https://github.com/<Your github username>/PS-Grievance.git (fetch)
origin https://github.com/<Your github username>/PS-Grievance.git (push)
```

4. This is the link to your fork and its name is *origin*. Whenever you *push* changes to *origin* it will reflect under your forked repository in your GitHub account and similary you can *pull* to get content from your repository to your local machine using the handle *origin*. But we also need to interact with the main repository from [Keshav's](https://github.com/kestal-lab/PS-Grievance) account.

5. In the same folder, type: `git remote add upstream https://github.com/kestal-lab/PS-Grievance`. Now to verify, again type: `git remote -v`. This should show:

```console
origin https://github.com/<Your github username>/PS-Grievance.git (fetch)
origin https://github.com/<Your github username>/PS-Grievance.git (push)
upstream https://github.com/kestal-lab/PS-Grievance (fetch)
upstream https://github.com/kestal-lab/PS-Grievance (push)
```
This will add a link to the main repository on Keshav's account and will be called *upstream*. (origin and upstream are conventional names) In order to get changes to from the main repo use *upstream* handle. **Never push anythihng to upstream**


#### Git push/pull and pull requests

Now suppose you have made changes in your local machine to the file in PS-Grievances folder. To share your work do the following:

1. `git status`
This will list all the files and folders where changes were made. Run this command often to keep track of whatever changes you are making while you are editing the files. There will also be other useful information displayed sometimes. 

2. 
```
git add <filename/folder>
git commit
```

This will open a text editor for you to write a commit mesaage. Give a short description/one line about what these changes do. Avoid non-sense commit messages makes it tough to refer to the commit later.

3. The changes are now saved in your local machine. We need to push it to your GitHub fork. But before that we also need to see if anyone else in the team has got their changes *merged* in the main repository. Hence do the following: `git pull upstream master`

This will get the latest content from the *upstram* (main repo) to your local machine. But since you too had changed some files it may happen that there arise what is called a *merge conflict*. This can happen if there were changes to the same file and at the same line where you made the changes. So you need to resolve them. Go to the **Merge conflicts** section below before you proceed.

4. In case there were no merge conflicts or they were solved, do: `git push origin master`
This will push all your work to your fork.

5. Now go to your GitHub account and open the PS-Grievances repository. A green button **Compare & pull request** should've come inside a highlighted box. OR there is also a pull request button below the green Clone or download button. The next page should ideally say that *Able to merge* with a large **Create pull request** button. Press the button and a confirmation page with a text box to fill in details about the PR (optional) will come. Confirm by pressing the **Create pull request** button there.


#### Merge conflicts

In case you get a merge conflict, Git will notify you with something like *Aborted. Resolve merge conflicts* when you do a git pull. To resolve them:-

1. `git status`: This will list all the files which have conflicts as *both modified*. Open all of them in text editor. The conflicting lines will be maked with

* <<<<<<<<< HEAD
* =========
* >>>>>>>>> new_content

Everything above ====== is the content before git pull and everything after it is the new content from git pull. Select which one to keep and  also remove these markers. Do the same for all the marked files.
Once done, do
`
git add file(s)
git commit files(s)
`
Add a commit msg that you resolved the confilcts and done; continue pushing to origin.


#### Some useful links

+ [GitHub udacity course](https://www.udacity.com/course/version-control-with-git--ud123)
+ Google any error, doubt. By far [Atlassian](https://www.atlassian.com/git/tutorials) is the most detailed site for git related answers.