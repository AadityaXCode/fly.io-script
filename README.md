# fly.io-script

# Deploy Any Bot/UserBot on fly.io

<a style="color:red;" href="https://fly.io/"> Fly.io </a> is free and perfect alternative to Heroku, but its not easy as that. 
we have to use terminal for deploying our Bot/Userbot. 
Read this guide to deploy bot on fly.io

# Creating Account and adding Credit Card on Fly
first of all, create an account on Fly and add credit card on billing section 
<b>(you won't be charged until upgrading your plan to Launch Plan) </b>

# Now install its CLI on your Operating System (Termux)
» <b>Android (Termux)</b><br>
first do:<br>
`pkg install root-repo` <br>
then run the below command <br>
`pkg install flyctl`

# Authenticating Terminal with Fly
run: <br>`flyctl auth login` <br>it will redirect to login page, login with Your Fly.io Account.

# Clone and Launch any Bot/UserBot in terminal
Git clone this repo from GitHub or just copy and paste <br>
`git clone https://github.com/itzrexmodz/fly.io-script` <br><br>
Then run: <br>
`nano app.py` <br> edit the App.py and paste the repo which you want to deploy. <br><br>
then do: <br> `cd fly.io-script` <br><br>
Now, Launch the `fly.io-script` into <a href="https://fly.io"> Fly.io </a> server using <br> `flyctl launch`<br> 
<b>(it will ask for overwriting the Procfile, just type `n` there) </b><br><br>
Now it will ask for Name of the application and server of application<br>
<b>Tip: choose Miami (mia) server for good ping and fast response</b><br><br>
