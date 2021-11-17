# f1rewall

## Setup guide:

**It is recommended to let your teams developer/sysadmin set this up.**

*The page is made to be easily editable by anyone with HTML/CSS/Bootstrap experience*

### 1. Creating the bot


0. Got to the Discord Developer Portal to create your bot.
https://discord.com/developers/applications
1. Press "New Application" in the top right corner
2. Set a name, this can be anything (will be seen by server members)
3. Once created, click on your app in the app manager.
4. Head to the **Bot** section on left bar.
5. Press **Add bot** on the right.
6. Set the **Public bot** option to false.
7. Copy the token ***(MAKE SURE NOT TO LEAK THIS)***
8. Paste your token in the config.yaml file, follow the instructions in it
9. Go back to the **General information** section and copy the app ID
10. Insert your ID here -> https://discord.com/oauth2/authorize?client_id=INSERT_CLIENT_ID_HERE&scope=bot&permissions=1
11. Visit the link and add the bot!

Congrats! Your bot is now ready!

### 2. Configuring the bot

1. Go to your DiscordApp settings **Advanced** section.
2. Enable developer mode
3. Right click the channel you want the bot to create invites to.
4. Copy channel ID
5. Paste your ID in the config.yaml file, follow the instructions in it

Congrats! Your bot is now configured!

### 3. Setting up ReCaptcha

1. Go to https://www.google.com/recaptcha/admin/create
2. Set a name for your app
3. Select "reCAPTCHA v2"
4. Add your domain
5. Accept the terms and submit
6. Paste your site key in the config.yaml file, follow the instructions in it
7. Paste your secret key in the config.yaml file, follow the instructions in it

Congrats! Your recaptcha is now ready!