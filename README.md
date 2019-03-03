# LumberBot
## A bot that plays Telegram Lumberjack

I wrote it for Chrome 1366x768 in my Ubuntu (Resolution is important because it actively looks for the right pixels in the screen). Also had the game opened in 50%

It's kinda unaccurate so I had to slow it down. I'll work on it later and figure out a better way of comparing the pixels so that it doesn't do the wrong movements. For now slowing it down and using correlation matching in Numpy did the job.

To stop it, you gotta do the dirty work: hit that CTRL-C/CTRL-Z on your Terminal.
If dies early, just keep rerunning until it works, the beginning of the phase is set in a weird way so I had to do some unusual things.
