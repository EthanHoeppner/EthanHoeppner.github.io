---
layout: gameDesignBlogPost
title: "Brazen Berry Bonanza 1.1"
date: 2017-08-09
category: gamedesign
---
The 1.1 update to Brazen Berry Bonanza is now out! Like before, the game is available on [windows](https://ethan-hoeppner.itch.io/brazen-berry-bonanza) and [android](https://play.google.com/store/apps/details?id=com.ethanhoeppner.brazenberrybonanza&hl=en), but now the game is also available on [mac](https://ethan-hoeppner.itch.io/brazen-berry-bonanza) and [iOS](https://itunes.apple.com/us/app/brazen-berry-bonanza/id1267676003?mt=8) Here's the changelog, with explanations:
- Yellow seeds now show which direction they will grow in when planted.

This change was quite an obvious one that I wish I'd thought of before. The output randomness in yellow seeds before this change was pretty annoying, and this was a nice solution to it.
- Yellow plants grow 1 tile longer than previously.

This was a simple balance change making it a bit easier to manage seed growth.
- The game now longer ends when 5 evil berries are simultaneously ripe. Now, whenever an evil berry ripens, the enemy gets one point. The game ends once the enemy gets 10 points.

This was intended to make the loss mechanic more present throughout the game. Before, it was really only something that needed to be worried about during the late-game, but with this change, it becomes an additional consideration for the player to weigh into their decisions during the early-game and mid-game.
- Seed types will now be more evenly distributed.

Originally, this change was necessary because of another mechanic I was considering. I eventually decided against including the other mechanic, but even without it I thought this change was worth keeping. With this change, you won't run into those situations where you really need a orange seed, but can't find one.
- There are now 3 special berries, blue, pink, and light green. Blue is the same as it was before, but now pink merely makes red plants recede. Green berries pause the growth of all evil plants for 12 seconds.

I essentially split the pink berry into two different berries. The blue berry had a single simple effect, but the pink had two effects together for some reason, so spliting them in half seemed like a natural way to create a new special berry.
- Special berries now spawn on a random position on the map (except for a 2-tile buffer at the edge of the map), whereas previously they would only spawn on green tiles. Additionally, special berries now spawn  independently of the number of green tiles on the map, whereas previously the spawn rate was proportional to the number of green tiles on the map.

Due to this change, the berries now have a chance of spawning in places where the player isn't connected to, providing an incentive to try and be connected to as much of the map as possible. Spawns were made independent of green tiles in order to give new player's more of a chance to interact with the special berries. I've heard from several beginners that they rarely even see special berries, so this seemed like a worthwhile change.
- The player's movement should now look more fluid. The player character should now "lean" in whatever direction the player is trying to move between tile movements.

This was a simple change, but I think it really improves the feel of the game.
- The movement and planting buttons on mobile are now closer to the horizontal center of the screen.

This should be especially helpful on smaller screens.

As I see it, there are two major problems with the game right now:

-The fact that the length of the game is so variable prevents me from implementing any [long-arc](http://keithburgun.net/arcs-in-strategy-games/) mechanics.
-The game expects the player to make too many inputs, and the inputs require particular timing. This causes a kind of "input stress", where the player has to spend too much mental effort on the particular inputs they make, leaving less time for the player to focus on plan-formation, the actually interesting part of the game.

The first problem will require some pretty huge changes. However, it's certainly soluble, and I can't say the same about the second problem. I think this is a fundamental problem of this type of game, i.e. games with a single player-character, controlled with direction buttons, played on a large grid with many expected inputs. So it seems to me this is a problem that will exist as long as I continue to work on this game.

With that in mind, right now I'm planning to work on and release a new game before I update BBB again. I don't think I'm done with BBB for good; I'm still interested in making the match length more consistent and working on implementing some long-arc mechanics. However, I think input stress is holding BBB back significantly, and so for the moment I want to focus on creating an interesting game with as little input stress as I can.
