# LumberBot
## A bot that plays Telegram Lumberjack

### Written in Ubuntu with a 1366x768 resolution screen.
(Resolution is important because it actively looks for the right pixels in the screen, although this could be changed for a percentual calculation). Also had the game opened in 50% because you can freely see where the branches start.

It's a bit slow'd down by `time.sleep` calls because the quicker it goes, the more unnacurate pixel matchin gets.
I'll work on it later and figure out a better way of comparing the pixels so that it doesn't do the wrong movements. For now slowing it down and using correlation matching in Numpy did the job (sometimes there's a 0.01% difference between pixels, but essentially they are the same in that context: a branch).

To stop it, you gotta do the dirty work: hit that CTRL-C/CTRL-Z on your Terminal
(The fail safe is a **TODO**)

If the Lumberjack dies early, just keep rerunning the program until it works (you'll notice when it goes full Rambo).
The beginning of the phase is set in a weird way (doesn't match the algorithm standard) so I had to do some unusual things.

### How it works:
- Some things are pre-determined:
  - The game will only always have 6 branches in the screen (except for the beginning, it starts up with 5, but you just gotta    move twice and it'll go back to 6.
  - When branches are at the character's head level, they take two hits to be smashed.
- With that in mind, the algorithm goes like this:
  - Find what are the pixel values of each branch position (positions are always the same every two moves):
    - An image is just a matrix, where each value represents a pixel, since I converted the MSS Screenshot to a Numpy      array, the matrix is shaped W (width) x H (rows) x BGRA (A 4-dimensional vector: Blue, Green, Red, Alpha)
  - Find what is the combination of branches (L represents Left and R represents R)
  - Since there's always six at the screen, you'll have something like LLLRRR or LRLLRR
  - Move twice to the opposite side of a branch to destroy it (that's the concept of the game I guess, huh)
  - GG.

### Maximum score it got:

![Image](https://i.imgur.com/sT7GBFC.jpg)

### TODO:
  ###### Efficiency improvements.
  ######  Make code cleaner (this is a must haha, it got really ugly as things weren't working and I had to chang it up.
  ###### Make it more precise (a good way would be matching more pixels in different positions).
