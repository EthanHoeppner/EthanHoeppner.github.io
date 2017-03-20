---
layout: gameDesignBlogPost
title: "Top Down Shooter Prototype"
date: 2017-02-25
category: gamedesign
---
I've been working on a prototype of a top-down shooter game for a while, and I think it's playable enough at this point to release it somewhere, so here goes. It's influenced rather heavily by Nuclear Throne, one of my favorite games, though I am designing from a strategy-game perspective. I'm sure it sounds contradictory to many people to think of a top-down shooter as a strategy game, but my concept of what a strategy game should look like is quite a bit different than the norm. I believe strategy games should have high [information generalizability](https://ethanhoeppner.github.io/gamedesign/information-generalizability.html) and either be real-time or have short timers limiting the time spent on each turn. I'll expand upon those assertions in future posts, but for now you can play the game in-browser [here](https://ethanhoeppner.github.io/gameFiles/topDownShooterPrototype1/bin/), or download it for windows [here](https://ethanhoeppner.github.io/gameFiles/topDownShooterPrototype1/TDS_prototype.zip).

Since this is just a prototype there isn't a menu or tutorial yet, when the game opens you'll merely see a "Play" button. Unfortunately the game isn't completely self-explanatory, so here's some stuff you'll probably need to know to be able to play:

- You are the green circle at the center of the screen. Use WASD to move around.
- When you left-click, you fire a shot at the enemy closest to your cursor within range. Your range is displayed by the translucent white circle around you. Shooting an enemy knocks them back.
- Certain weapons have additional effects. Some weapons will weaken enemies, causing all future attacks to deal extra knockback, other weapons will slow enemies, permanatly making them move at half their normal speed, and others will freeze enemies for a period of time. Weakening is denoted by a red square around the enemy, slowing with a yellow icon above the enemy, and freezing with a blue square.
- There are two extra weapons scattered throughout each section, and every weapon has limited ammo.
- You can carry two weapons at once, and you can swap between them either by hitting space or by right-clicking.
- In each section of the map, there are six nests. When you move to the right of a nest, it spawns two enemies.
- Enemies have do not have health, but they can be killed by knocking them into the blue patches on the wals of the level. Knocking an enemy into one of these patches destroys both the enemy and the patch.
- The map is divided into "sections" which are separated by walls which can only be opened with keys. Each wall requires 3 keys, and each section has 4 keys in it.
- At the top of the screen is a timer, which starts at 60 seconds. When the timer reaches 0, the current section will begin to be filled with red tiles. Touching one of these red tiles ends the game.
- You don't have any health bar, but whenever you are hit by an enemy, the timer is shortened by several seconds. Also, if an enemy touches one of the red tiles it is killed, but takes several seconds off the timer.

Unfortunately, the game doesn't have a victory condition at the moment. There are only 5 sections in the level, so for now if you reach the end of the fifth section you can say that you won.

**Edit: 3/20/2017**
Since this post, I've decided to stop working on this game for now. Many of the changes I find myself wanting to make are large enough that it would be quicker to just scrap the project and restart than it would be to continue working forward from here, and at the moment I have other games that I think take precedence over this one. I may eventually return to this concept, but for now I'm shelving it.

However, I did make some significant changes after posting the first build of the game here, and there's a newer version of this prototype that you can play [here](https://ethanhoeppner.github.io/gameFiles/topDownShooterPrototype1/build2/). Here's a brief rundown of the big changes in this build:
- The game is about 25% slower now
- Sections are longer, and you need 5 keys to progress to each one, but there are also 7 keys in each section
- You can now see what enemies will be spawned, before they are actually spawned
