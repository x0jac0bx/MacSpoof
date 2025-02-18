# MacSpoof
Uses macchanger to spoof mac address to static or random address for pwngotchi

  Install Plugin

1. FTP into your pwnagotchi and Drag desired plugin into /usr/local/share/pwnagotchi/custom-plugins/

To FTP into your Pwnagotchi as a root user, you'll first need to initialize the root user account and also enable root FTP logins:

1. SSH into your Pwny as the pi user (as usual)
2. sudo passwd root
3. Enter pi user's password if asked (raspberry)
4. Enter a new password for root user
5. Save and exit. You'll now have a root user. Time to enable root FTP logins
6. sudo nano /etc/ssh/sshd_config
7. NOTE: sshd_config, not ssh_config

8. Change the PermitRootLogin prohibit-password line to PermitRootLogin yes and uncomment the line if it's commented (remove the # from the start of the line)
9. Save and exit
10. sudo service ssh restart

  Install macchanger
1. sudo apt install macchanger

  Make sure its working
1. SSH into your Pwny as the pi user (as usual)
1. ip a
2. should see the spoofed address under the info for wlan0

