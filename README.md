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
Now it will ask for Name of the application and server of application<br><br>
<b>Tip: choose Miami (mia) server for good ping and fast response</b><br><br>
Now it will ask for setting up Postgresql & Redis for our app, type `n` for both or your account will be charged.<br><br>
# Adding Secrets and editing fly.toml
add secrets (variables) for your app using<br> `flyctl secrets set VAR_NAME=’value’` <br><br>
Add the below method to bulk set the secrets using single command <br>
Tip: paste this on any text editor and add the vars then paste it on your terminal.<br><br>
`flyctl secrets set \ VAR_NAME='VALUE' \ VAR_NAME='VALUE'` <br><br>
<i><b>Note:</i></b> Make Sure To Add <br>`FLASK_APP=Your App Name'` <br> in vars Or Your Bot Won't Run.<br>
You can find app name in `fly.toml` or on `fly.io/dashboard`<br><br>
Now scale the memory of your app also using<br>`flyctl scale memory 2048`<br><br>
# Deploying The App
type<br>`flyctl deploy`<br>and wait few minutes until it deploy successfully…<br><br>
Wait for 5-6 Minutes Until it deployed on `fly.io`<br><br>
Meanwhile Logs can be also view from <br>`fly.io/dashboard`<br> or type<br>`flyctl logs`<br>on terminal.
