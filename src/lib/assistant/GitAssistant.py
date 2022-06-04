import os
import datetime


class GitAssistant :

    def __init__(self,brain) :
        self.localpath = "C:\\Users\\Acer\\Documents\\work\\bookmundi\\bookmundi\\"
        self.brain = brain

    def goto_local_path(self) :
        os.chdir(self.localpath)
        # get current directory
        self.current_dir = os.getcwd()
        print(self.current_dir)

    def exec_bash_command(self, command) :
        os.system(command)

    def check_if_git_repo(self) :
        self.exec_bash_command("git status")

    def change_branch(self, branch) :
        self.branch = branch
        self.exec_bash_command("git checkout " + branch)

    def pull_latest_changes(self) :
        command = "git pull origin " + self.branch
        self.exec_bash_command(command)
    def isBranchAvaiable(self,branch):
        return False
        availableBranch = self.exec_bash_command("git branch")
        availableBranch = availableBranch.split("\n")
        if(branch in self.exec_bash_command("git branch")):
            self.brain.say("Branch " + branch + " is already there")
            return False
        return True
    def deleteBranch(self, branch):
        self.exec_bash_command("git branch -D " + branch)

    def checkoutToNewBranch(self, branch) :
        if(self.isBranchAvaiable(branch) == False):
            # self.brain.say("Branch " + branch + " is already there. Deleting it")
            self.deleteBranch(branch)
        self.newbranch = branch
        self.brain.say("Checking out to new branch " + branch)
        self.exec_bash_command("git checkout -b " + branch)

    def push_to_remote(self) :
        self.exec_bash_command("git push origin " + self.branch)

    def getCurrentDate(self):
        return datetime.datetime.now().strftime("%Y-%m-%d")

    def deploy(self) :
        brain = self.brain
        self.goto_local_path()
        self.check_if_git_repo()
        self.change_branch("uat")
        brain.say("Changed to uat branch")
        self.pull_latest_changes()
        brain.say("Pulled latest changes")
        date = self.getCurrentDate()
        newBranch = "deploy/"+date
        self.checkoutToNewBranch(newBranch)
        brain.say("Checked out to new branch")

        self.push_to_remote()
        brain.say("Pushed to remote")
        self.brain.say("Deployment Complete")