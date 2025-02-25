(taken from `README.md`)

Without a Webserver
---

If you do not have a webserver, but have Python3 installed on your computer, you can try...

1. Download Gears from https://github.com/QuirkyCort/gears/archive/refs/heads/master.zip
2. Change to the "gears/public" directory
3. Run `python -m http.server 1337`
Do not close the window with the Python command running.

This should get the site running on http://localhost:1337 (...try http://127.0.0.1:1337 if that doesn't work).

The site may also be available to other users on the same network using http://your_IP_address:1337, where "your_IP_address" is replaced with your actual IP address.
This may not work depending on your network configuration and your firewall settings.

If you do not wish to allow other users from accessing the site, you should run `python -m http.server 1337 --bind 127.0.0.1` instead.
