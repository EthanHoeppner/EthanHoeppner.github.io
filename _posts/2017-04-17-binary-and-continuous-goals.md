---
layout: gameDesignBlogPost
title: "Binary and Continuous Goals"
date: 2017-04-17
category: gamedesign
---
**Introduction**

In [my previous article](https://ethanhoeppner.github.io/gamedesign/the-problems-with-difficulty-modification.html), I wrote about the par system and the benefits it has over a traditional win/loss format. However, as I mentioned in the article, some people reject non-binary goals. They believe that good strategy games must have a binary goal, or in other words that every match of the game must end in a “win” or “loss,” and that any games that use continuous victory conditions, or “score systems,” are fundamentally flawed. In that article I mentioned that I disagreed with this line of thought, but didn’t go into detail for the sake of brevity. In this article I will go into that detail and defend continuous goals, and in fact go farther and claim that all good single-player strategy games should use a continuous goal.

**Probability of victory**

The goal in a game that uses a win/loss system is often thought to be “to win,” however I believe that this isn’t the most accurate way of phrasing the real goal. In a sufficiently complex game, you won’t be able to say “this move will make me win.” At best you can say “this move will give me a higher likelihood of winning.” Thus, the goal the player really deals with is “how can I maximize my probability of winning.” 

Through this lense, all strategy games are about trying to maximize a continuous quantity: in a win/loss game it’s the probability of victory, and in a score system it’s the score.

**The issues with maximizing probability**

Ultimately, the problem with the win/loss system can be thought of in this way: The player attempts to maximize their probability of victory, but they aren’t told how well they did at that, instead the feedback they receive is just a single bit of information; the “win” or “loss”.

Imagine that instead of giving a “win” or a “loss,” a game simply told you the probability that your strategy had of winning the game (and to be clear, I’m talking only about single-player strategy games). This approach would have the advantage that it would allow you to assess the viability of a new strategy much faster than win/loss feedback. To see why, imagine that you are attempting to asses the value of a new strategy in some strategy game: after a single match your best guess of the win-chance of that strategy can only be either 0% or 100%. After 2 matches it isn’t much better, as your best guess will be either 0%, 50%, or 100%. Even after 10 matches, you can only get as accurate as 0%, 10%, 20%, etc. If instead the game just tells you the probability you had of winning the game, or even an approximation of it, the feedback from a single match is vastly more useful.

**Score systems**

Once we imagine that the game simply tells you how well you maximized the probability of victory, the concept of having an actual “victory” or “loss” at the end of the game seems to have lost it’s purpose. If the player is only concerned about maximizing their win-chance and they are directly told their win-chance, why do they also need to receive a “win” or “loss” at the end? It doesn’t give them any useful information.

Of course, if you get rid of the “win/loss” part, calling the value that the player is maximizing the “probability of victory” ceases to make any sense, instead they are just maximizing an arbitrary quantity. And there is no longer any reason that this quantity needs to stay between 0 and 100%, it could just as easily span between 0 and 40, or 0 and 1000. From this perspective, we can stop thinking of the quantity the player is maximizing as a probability, and instead just as some arbitrary measure of how well the player has done, or in other words, a “score”.

But of course, calculating the probability that the player had of winning would be implausibly difficult in any reasonably complex strategy game. So, in a score system, instead of having the player try to maximize the probability of an event, you just designate certain events as being worth a certain number of points.

**Criticisms of score systems**

Many people have pointed out practical flaws in currently-existing score system based games, and used these to argue that score systems are fundamentally flawed. Keith Burgun’s article [Auro’s “Single-Player Elo System”](http://www.dinofarmgames.com/auros-single-player-elo-system/) makes several of the criticisms, which I will now address:

> * Match length scales indefinitely… As a player gets better at the game, the game simply gets longer, and longer… and longer.

This issue was a big focus of my last post, [The Problems with Difficulty Modification](https://ethanhoeppner.github.io/gamedesign/the-problems-with-difficulty-modification.html). The solution, briefly, is to place a time-limit on the game, but allow for a large variation in the rate at which players can gain points (by implementing optional challenge rewards), so that strategic progress can be expressed through an increase in the efficiency of gaining points, instead of merely surviving for longer.

> * ‘Highest score ever’ becomes too difficult… What happens in high-score based games is that eventually, you get some once-in-a-lifetime crazy game that sets your ‘highest score ever’ at some super high number. The higher that number gets, the more that future games are without any reasonable, achievable goal.
> * Beat the score… now what? There’s this weird moment that happens in high score based games, which happens right when you beat the high score. Strangely, the match keeps going. Now what’s your goal? You already achieved the goal for this match, so what are you doing now?

These two criticisms are actually not talking about the same type of score system that I advocate for. The system I am arguing for is one in which there is a continuous goal of maximizing the score, but these arguments are actually talking about a system in which you have a binary goal: beating the highest score you’ve ever gotten in previous matches. These are two very different systems, and I with Keith that the one he is describing has big issues.

> * Some have suggested that you should get ‘as high a score as you can’ or even ‘survive as long as you can’. Well, that goal is 100% guaranteed to succeed, because even if your match ends the MOMENT you achieve the high score, you still got ‘as high a score as you could’.
> * Ultimately, because of all this bizarre noise, players end up having to just kind of choose their own goals. ‘Maybe I’ll go for 30,000 points this game’, they might say. Half-way through, seeing that things aren’t going so well, they might say ‘Hmm, well, let’s see if I can get 20,000.’

Both of these criticisms, I believe, are making a mistake in their interpretation of score systems. To be clear, in a score system the player never has a “goal” like a win/loss system does. Perhaps you could say that the “goal” is “to maximize score,” but there is not any such thing as “reaching” or “accomplishing” the goal in a score system. A score of X is better than a score of X-1, but there isn’t any point at which you can say “I have accomplished the goal” in a score system. This is a fundamental difference between win/loss and score systems, and trying to force a score system to fit into the mold of a win/loss system is a mistake.

**Arc lengths in score systems**

Another concern I’ve heard voiced by several people is that using a score system will lead to gameplay that is repetitive, and that there will not be any overarching strategic planning going on. Since the goal is just to get more points, the strategically ideal thing will be obvious: “do whatever will give you more points right now”. In other words, score systems will inevitably lead to a game comprised of only of “short arcs.”

I agree that many, perhaps most, existing score games are comprised mostly of short arcs, and I agree that this is a problem. However, I don’t think that this is an inherent problem of score systems, but rather just a design flaw of those individual games. Limiting the length of the game is already one step towards fixing this issue, since having a clearly distinguishable “late-game” and “early-game” can lead to strategy that varies as the game gets closer to the end. This can be further improved on by offering the player the opportunity to make trade-offs between short-term and long-term gains, thus forcing the player to have a plan of when and how to gain points. Creating a game that has interesting long-term strategic decisions isn’t the easiest thing to do, but I don’t see any good reason to think that it is harder to do in a score-based game than a win/loss one.

It is also important to note that the player is attempting to maximize their score *at the end of the game*, not necessarily in each moment. In other words, a player who has 0 points for the first 90% of the game and then gets 100 points by the end did just as well as a player who gets 100 points in the first 10% of the game and then gets no more for the remainder. Thus, a score doesn’t necessarily have to be something that you accumulate over the course of a game, but instead it could just be a measurement of the endstate of the game. This way of thinking about score systems might be more conducive to making games with good arc structures.

**Conclusion**

Many existing score-based games have big problems. These problems have lead some people to believe that score systems themselves are at fault, but I disagree. All issues with score systems that I have come across can be fixed through practical design considerations that are less extreme than switching to the win/loss format.

The win/loss format has big problems of its own, in that the real goal is to maximize the chance of victory, but the game doesn’t tell you how well you pursued that goal. The win/loss format is effectively a broken score system, and any single player strategy game that uses a win/loss system is making a significant mistake.
