Some Important Steps
Before your work

$ git checkout master

$ git pull origin master:master

$ git checkout 'yourbranch'

$ git merge master

// now you are in your up-to-date local repo

During your work

// if you want to commit your local repo, make sure you stay in yourbranch

$ git add 'somefiles'

$ git commit -m "'description of this commit'"

Finish your work

// make sure you already commit your local repo and stay in yourbranch

$ git push origin 'yourbranch':'yourbranch'
