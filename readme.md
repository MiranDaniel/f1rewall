> [!CAUTION]
> UPGRADE TO VERSION >= 1.1.0 DUE TO SECURITY VULNERABILITY IN OLDER VERSIONS

---

# f1rewall
*The sleek, simple and scalable invite gateway for your Discord community*

---
**Made in**
![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)![](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)![](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)![](https://img.shields.io/badge/Discord_API-7289DA?style=for-the-badge&logo=discord&logoColor=white)![](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)![](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)![](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white)

**Officially supports**
![](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![](https://img.shields.io/badge/Debian-A81D33?style=for-the-badge&logo=debian&logoColor=white)![](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)![](https://img.shields.io/badge/Pop!_OS-48B9C7?style=for-the-badge&logo=Pop!_OS&logoColor=white)![](https://img.shields.io/badge/Fedora-294172?style=for-the-badge&logo=fedora&logoColor=white)![](https://img.shields.io/badge/Raspbian-A22846?style=for-the-badge&logo=raspberrypi&logoColor=white)

**Optional supported technologies**
![](https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=Cloudflare&logoColor=white)

---


F1rewall is a Discord invite gateway. It lets you easily route your Discord server invites through a controlled page with a captcha.
It generates a unique, time limited one time invite for every user.
Thanks to this, you can stop most bots from entering your server.


---


Light theme default        |  Dark theme default
:-------------------------:|:-------------------------:
<img src="https://media.discordapp.net/attachments/795438999761977394/910258446681657374/unknown.png" height="200"/> | <img src="https://cdn.discordapp.com/attachments/795438999761977394/910258701204602920/unknown.png" height="200"/>

*All websites elements can be customised easily*

---

## Setup guide:

**It is recommended to let your team's developer/sysadmin set this up.**

**This script was made for Linux/GNU, officially supported distributions are: `debian`, `ubuntu`, `pop!_os`, `fedora` and `raspbian`**

*The page is made to be easily editable by anyone with HTML/CSS/Bootstrap experience*



### 0. Getting the code

1. run `git clone https://github.com/MiranDaniel/f1rewall`
A folder called `f1rewall-master` with the source code has been created!

### 1. Creating the bot
0. Go to the Discord Developer Portal to create your bot.
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

1. Go to your Discord (app, not dev portal) settings **Advanced** section.
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

### 4. Running

1. Run `apt-get update -y && apt-get upgrade -y` to update your packages
1. Run `apt-get install python3-dev -y && apt-get install python3-venv -y` to install the required dependencies for Python
1. Run `sudo make` to install all dependencies
2. Run `./venv/bin/python3 server.py` to start the server
3. The script will now host your gateway on the port specified in config.yaml

#### Debugging

If you get the `make: command not found` error, run `sudo apt-get install build-essential` to install make.

## Network configuration

### 1. Firewall configuration

1. Configure your firewall and open the port specified in config.yaml

### 2a. DNS configuration

Remember to set a static IP and host on port 80.
If you want to stop the Apache server from running on port 80, use `sudo systemctl stop apache2`

Follow this guide to redirect your chat.<>.<> domain to your chat gateway. https://www.namecheap.com/support/knowledgebase/article.aspx/9776/2237/how-to-create-a-subdomain-for-my-domain/

You can also use the CloudFlare Argo Tunnel.

### 2b. CloudFlare tunnel configuration

Read the documentation file in `docs/clouflare_tunnel.md`

## Discord configuration

1. Make sure the gateway works
2. Disallow users on your server from making new invites, let only the bot create them
3. Put your logo in static/wordmark.png
4. Put the website background in static/background.png
5. Set the `dark_theme` value in config.yaml to set the website text color

## Customisation

Read the documentation file in `docs/customisation.md`

## Support

If you're having issues with the app please open an issue or discussion thread.

Private support can be provided. Find the contact information on https://mirandaniel.com/

## License
<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png"/>
  
```
Copyright 2021-2024 MiranDaniel


The Software is provided to you by the Licensor under
the License, as defined below, subject to the following
condition.

Without limiting other conditions in the
License, the grant of rights under the License will not
include, and the License does not grant to you, the
right to Sell the Software.

For purposes of the
foregoing, “Sell” means practicing any or all of the
rights granted to you under the License to provide to
third parties, for a fee or other consideration
(including without limitation fees for hosting or
consulting/ support services related to the Software), a
product or service whose value derives, entirely or
substantially, from the functionality of the Software.
Any license notice or attribution required by the
License must also include this Commons Cause License
Condition notice.


THE SOFTWARE IS PROVIDED "AS IS",
WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
