# f1rewall

The free-code Discord invite gateway for your community!

***This branch hosts the f1rewall 2.0 version. Still under development, feel free to contribute :)***

---

Current version: `2.0.0-alpha.3`

---

## README contents

- Basic information
- README contents
- Setup guide
  - Requirements
    - Creating a Discord Bot
  - Basic setup
  - Linux Server Configuration
    - systemd service
    - firewall configuration
- TODO / Planned features
  - Admin dashboard
  - Gateway
  - Interactive setup
  - Other
- Support
- Donate
- License


---

## Setup guide

### Requirements

#### Creating a Discord bot

Go to the [Discord Developer Portal](https://discord.com/developers/applications) to create your bot.
Press **New Application** in the top right corner.

Set a name and create your bot.

Click on your app in the app manager and head to the bot section.
Create a bot and set the **Public Bot** option to false.
Copy the bot token (you will need this later).

Go back to the General Information tab and copy the bot ID.
Insert the bot ID in this URL to invite your bot https://discord.com/oauth2/authorize?client_id=INSERT_CLIENT_ID_HERE&scope=bot&permissions=1




### Basic setup

Use this command to clone the repository and then access the code directory

```bash
git clone https://github.com/MiranDaniel/f1rewall f1rewall
cd f1rewall
```

If Python **3** is not installed, install it and the pip package manager

Install the requirements

```bash
pip3 install -r requirements.txt
```

Run the interactive setup file

```bash
python3 setup.py
```

You can now use Gunicorn to host the server, run it using

```bash
gunicorn --bind 0.0.0.0:80 wsgi:app
```

### Linux server configuration

#### systemd service

To automatically run Gunicorn on system startup create a systemd service
```bash
sudo nano /etc/systemd/system/f1rewall.service
```
And place in this text, replace `<DIR>` with the script directory, you can find it using the `pwd` command
```bash
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=<DIR>
ExecStart=/usr/local/bin/gunicorn --bind 0.0.0.0:80 wsgi:app --capture-output
Restart=always
RestartSec=5s


[Install]
WantedBy=multi-user.target
```

Enable and start the service
```bash
sudo systemctl enable f1rewall
sudo systemctl start f1rewall
```

#### firewall configuration

Remember to open port 80 to let users see your website.
Install ufw
```text
sudo apt install ufw
```

Open the port 80, remember to also open **port 22** to not cut yourself off **SSH**!
```text
sudo ufw allow 80
```

*Optional config for SSH users*
```text
sudo ufw allow 20
```

Enable ufw
```text
sudo ufw enable
```


---

## Todo / planned features

### Admin dashboard

- Charts and graphs on the dashboard analytics view to better show the times when users are joining etc.
- More analytics to show
- Better bug reporting
- Direct developer contact form integrated
- Integrated documentation
- Auto check updates
- Linux server security check summary under Health tab
- User permissions
- Editable configuration from the web view
- Color theme toggles

### Gateway

- Integrated Google Analytics

### Interactive setup

- Set logo/background from setup
- Pre-flight check
  - is port 80 open?
  - are requirements installed?
- Support for terminals without ANSI

### Other

- Docker image
- Theme system (user workshop)

---

## Support

If you're having issues with the app please open an issue or a discussion thread.

Contact the maintainer at https://mirandaniel.com/ for more private support, setup and additional development services.

---

## Donate

- Ethereum: `0x20D3c078958A2b866F9F423a722aF5a92bc7e08b`
- Polygon: `0x20D3c078958A2b866F9F423a722aF5a92bc7e08b`
- *Other EVM*: `0x20D3c078958A2b866F9F423a722aF5a92bc7e08b`
- Monero: `42dN1SjyQNFMu3hPjJZqXa4Z8oMMLLiPzHmC4q8h3DXWS2gHxpjACxcWyAReJGqN4RX79VTE8pEn6SVxgjCJTXhg5ECB9Qe`

---

## License

```text
Copyright 2021-2022 MiranDaniel


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
