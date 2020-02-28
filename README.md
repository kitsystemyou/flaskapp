---
page_type: sample
description: "This is a simple audio separation app that demonstrates how to use spleeter by Deezer."
languages:
- python
products:
- azure
- azure-app-service
---

# Python Flask app for Azure App Service (Linux)

This repository has python, flask code of web site:"Vocal and Band Separation"
It's is made for Azure App Service on Linux.
**Need:ffmpeg in Linux**

# Construct
+ / first page

Main page. An User need to select upload file(.mp3 only).
Audio file should be small and <.mp3> file.

+ /result
Result page. An User can listen original and separated audio if appropriate file are uploaded.

# Vocal Separation LIbrary
[spleeter](https://github.com/deezer/spleeter) by [Deezer](https://www.deezer.com/us/offers/hifi).
