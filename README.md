# Tission

## Overview

Tission is a ***web platform*** which automatically shows the valid mission chats from ***Twitch*** broadcast.

It analyzes the ***donation logs*** of specified Twitch streamer in ***real time*** and classifies whether it is a valid mission or not using the pre-trained ***deep learning model***.

## Principle

The streamer must first login to both ***Twip*** and ***Tission*** platforms using his or her Twitch account.

Then Tission starts crawling donation logs from Twip and sends it to our online server in ***JSON*** format.

The server saves what is recieved and runs the pre-trained ***deep learning model*** to classify valid missions from donation logs.

If there are valid missions then it refreshes ***Tission*** web platform and shows the mission to the streamer.

The streamer can use ***OBS*** program to show Tission in some part of the screen so it can also be seen by Twitch broadcast viewers.

