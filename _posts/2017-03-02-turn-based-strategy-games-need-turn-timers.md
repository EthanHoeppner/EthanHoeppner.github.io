---
layout: gameDesignBlogPost
title: "Turn Based Strategy Games Need Turn Timers"
date: 2017-03-02
category: gamedesign
---
In my [post on Information Generalizability](http://ethanhoeppner.github.io/gamedesign/information-generalizability.html), I distinguished between two mental processes that a player uses to play a game: Analysis and Calculation. Calculation is the type of thinking that uses computation to predict the exact results of individual moves, where as analysis is the a more intuitive, automatic type of thinking. Calculation, as I argue in that post, is something to be avoided when designing games. Information Generalizability is what allows analysis to be more useful, but it doesn't necessarily make calculation less useful. A game high in information generalizability will be susceptible to analysis, but you will always do better at the game fully calculating the result of all possible moves than you will be using analysis.

**The Problem**

Analysis can never do a better job than calculation, since full calculation is guaranteed to produce the proper result, while analysis can only hope to produce the proper result most of the time at best. Analysis is a short-cut to calculation, but can never be quite as effective. As Elliot George puts it in his fantastic article [Emergence and Chaos in Games](http://elliotgeorge.net/2017/02/21/emergence-and-chaos-in-games/): "Given infinite computational power, any higher level understanding of emergent phenomena is strictly inferior to the most basic understanding of fundamental laws. Descriptions of emergent properties are necessarily less complete than a full description of the system from which emergent properties arise." Thus, in a game where there is no limit to how much the player can calculate, the ideal strategy is to ignore analysis completely and to focus only on calculation. No amount of information generalizability is sufficient to avoid calculation.

Thankfully, humans do not have infinite computational power, and analysis is much faster than computation. Therefore, analysis is a useful way of speeding up the process of coming to a decision. However, certain games give the player infinite time to make a decision, and in those games speeding up your decision making process gives you no benefit, and this is still strategically useless.

Of course, though analysis serves no purpose from a strategic perspective, it can serve a practical purpose, since you can choose to use analysis in order to make the game more fun for yourself or make sure it ends in a reasonable amount of time. Nobody spends as much time as is strategically optimal on a game of chess, since if they did they'd spend hours working through every potential consequence of each move on graph paper. That doesn't seem like very much fun for the player, and even less so for the opponent, but that's what is necessary to play optimally. So there exists a conflict between what the player knows will be fun, and what they know will be strategically optimal.

Strategy games should avoid situations where what is fun and what is strategically optimal are two different things. The fun strategy and the strategically optimal strategy should be one and the same, but if you give the player infinite time to calculate, they aren't. You force the player to choose which strategy they will go with: the fun strategy of using analysis, or the boring-but-optimal strategy of using calculation.

**Turn Timers**

The solution to this problem is to limit the amount of time that the player has to calculate. This is done by imposing a time limit on each turn of the game. By limiting the amount of time a player can spend on a turn, you ensure that the player can only do a limited amount of calculation, and you help solve the problem of the optimal strategy and fun strategy not aligning. This technique is used in competitive chess, since in a competitive environment people will do whatever it takes to win, such as spending an hour thinking about a single move if you let them.

Unfortunately, adding a turn timer to game like chess doesn't do away with calculation entirely. When playing chess-with-a-timer, analysis is important, but just as important is the calculation you do to supplement your analysis. Your intuition may tell you "it would be a good idea to attack the enemy queen right now" but you still need to calculate your way through the web of complex, interconnected positioning consequences to make sure that if you follow your intution you won't be making a silly mistake, like opening one of your own pieces to an easy attack.

The reason that this problem exists in chess is that calculation is too valuable relative to analysis. When making any decision in a game with a timer, analysis and calculation each hold a certain amount of value, and each require some amount of time. Thus, the player has to choose how much time they want to spend analyzing, and how much they want to spend calculating. If analysis isn't valuable enough relative to calculation then calculation will be an important part of the ideal strategy, as it is in chess. Thus, if you don't want the ideal strategy to involve calculation, you need to make sure the value of analysis is sufficiently large relative the value of calculation.

The way that you increase the value of analysis relative to calculation is by increasing information generalizability. If information generalizability is sufficiently high, analysis will be useful enough relative to calculation that the ideal strategy will be to rely purely on analysis, since analysis can come to decisions much faster than calculation. So, in order to truly minimize calculation, a game must have both high information generalizability and a turn timer.

**Real-Time Games**

One can seemingly sidestep this problem altogether by simply making a real-time game instead of a turn-based one. However, if a real-time strategy game includes a pause feature, like FTL, or otherwise allows the player to just stop the action of the game and take as much time as they'd like to think, it will have the same problems as a turn-based game without a timer.

The exact length of the turn timer in a turn-based game isn't a easy topic, but that is outside of the scope of this article. All I'll say for now is that the timer should be long enough to allow a good amount of analysis, but short enough to minimize the amount of calculation the player needs to do. In a real-time game, we can't exactly talk in terms of the length of the turn timer, but we can make analogous claims by talking about the pacing a game: The gameplay should be slow enough to allow for analysis, but fast enough to prevent calculation.

**Conclusion**

A game with high generalizability but no timer lacks a method of insuring analysis is used. A game with a timer but low generalizability is no better, since it is incapable of ensuring that the ideal strategy doesn't involve too much calculation. Low generalizability games with timers also run the risk of being unnecessarily stressful by forcing the player to squeeze in as much calculation as they can into the given time. Both of these elements provide part of a solution, but one without the other is not enough. A good strategy game needs both.
