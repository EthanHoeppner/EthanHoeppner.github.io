---
layout: gameDesignBlogPost
title: "Top Down Shooter Prototype"
date: 2017-02-25
category: gamedesign
---
I've been working on a prototype of a top-down shooter game for a while, and I think it's playable enough at this point to release it somewhere, so here goes. It's influenced rather heavily by Nuclear Throne, one of my favorite games, though I am designing from a strategy-game perspective. I'm sure it sounds contradictory to many people to think of a top-down shooter as a strategy game, but my concept of what a strategy game should look like is quite a bit differnent than the norm. I believe strategy games should have high [information generalizability](https://ethanhoeppner.github.io/gamedesign/information-generalizability.html) and either be real-time or have short timers limiting the time spent on each turn. I'll expand upon those assertions in future posts, but for now the game is playable in-browser [here](https://ethanhoeppner.github.io/gameFiles/topDownShooterPrototype1/bin/), or download it for windows [here](https://ethanhoeppner.github.io/gameFiles/topDownShooterPrototype1/TDS_prototype.zip).

Since this is just a prototype, there isn't a menu or tutorial yet, when the game opens you'll merely see a "Play" button. Unfortunately the game isn't completely self-explanatory, so here's some stuff you'll probably need to know to be able to play decently:

- You are the green circle that appears at the center of the screen. Use WASD to move around.
- When you left-click, you fire a shot at the closest enemy within range. Your range is displayed by the translucent white light around you. Shooting an enemy knocks them back.
- Certain weapons have additional effects. Some weapons will weaken enemies, causing all future attacks to deal extra knockback, other weapons will slow enemies, permanatly making them move at half their normal speed, and others will freeze enemies for a period of time.
- There are two extra weapons scattered throughout each section, and every weapon has limited ammo. You'll have to pick up weapons and manage ammo carefully to win.
- You can carry two weapons at once, and you can swap between them either by hitting space or by right-clicking.
- In each section of the map, there are six nests. When you move to the right of a nest, it spawns two enemies.
- Enemies have do not have health, but they can be killed by knocking them into the blue patches on the side of the level. Knocking an enemy into one of these patches destroys both the enemy and the patch.
- The map is divided into "sections" which are separated by walls which can only be opened with keys. Each wall requires 3 keys, and each section has 4 keys within it.
- At the top of the screen is a timer, which starts at 60 seconds and counts down to 1. When the timer reaches 0, the current section will begin to be filled with red tiles. Touching one of these red tiles ends the game.
- You don't have any health bar, but whenever you are hit by an enemy, the timer is shortened by several seconds. Also, if an enemy touches one of the red tiles, it is killed, but takes several seconds off the timer.
