---
title: A bit of praise for Bases (as an alternative and a replacement for Notion)
source: https://www.reddit.com/r/ObsidianMD/comments/1ma5gar/a_bit_of_praise_for_bases_as_an_alternative_and_a/
author: "[[deathverified]]"
published: 2025-07-26
created: 2025-07-28
description: Reddit is where millions of people gather for conversations about the things they care about, in over 100,000 subreddit communities.
tags:
  - clippings
---
Hey everyone — Just wanted to share a use case that made my day recently and that might resonate with some of you here.

I’ve been using Notion for years to manage a personal music review database — over 3,200 records with ratings, tags, reviews, album covers, artist info, and metadata like country, year, etc. It worked okay, but between the slowness, lack of offline support, and being locked into someone else’s ecosystem, I started looking for alternatives.

Like many others, I bounced between tools but none of them stuck. At least I found obsidian but it didn’t really work as well as I wanted — Dataview was a bit too clunky and I just couldn’t set it all up to work as well as Notion did out of the box.

But then I saw Bases being announced and I decided to give it all another shot.

What I needed:

- A way to filter and sort notes based on frontmatter (e.g. “show me all albums rated 4+ from Norway”)
- Image support (album covers)
- Batch editing, scripting, and flexibility
- And most importantly: offline-first and local ownership

What I did:

- Exported everything from Notion to Markdown (without images initially).
- Asked ChatGPT for a script to clean up filenames (Notion exports include messy suffixes).
- asked for another script to convert plain-text Notion-style properties into Obsidian properties, turning things like Country: Norway into proper metadata (and even auto-linking to country pages).
- Cleaned up junk properties and leftover paths with another short script.
- Dropped it all into Obsidian and opened a Base view — and… it worked.

A few hiccups:

- Some file names broke due to illegal characters (e.g. <, >, :) in “Band - Album” titles. I asked for a script to find them and fixed them manually (~50 out of 3,200).
- No album covers yet — so I asked for another script to scrape images based on artist/album, rename them, and drop them into the folder.
- Bases doesn’t show images with ! in front, so another script removed that in all notes.

Bonus upgrades:

- I resized all covers to lower resolutions — this drastically improved scrolling and load speed.
- Then I asked for a tool that lets me paste a link to an album online, and it: Pulls metadata + Creates a new note + Downloads the cover image + Fills in frontmatter fields automatically

All I need to do now is drag the image into the cover property and I’m done. It’s fast, local, customizable, and way more fun to work with than I expected.

The only missing piece:

Bases doesn’t yet support mobile — but afaik that’s on the roadmap, and once it lands, this setup will be nearly perfect for my needs.

EDIT — I am stupid and I’ve been informed in the comments that Bases are actually available for Catalyst members on mobile. I’ll have to check it out!

EDIT 2 — I got access to Bases for mobile and IT WORKS LIKE A CHARM. Somehow it deleted my bases from pc but bulk restore worked and it’s all there and holy damn it’s perfect. Thank you, Obsidian.

⸻

TL;DR:

Moved a huge personal database (3,200+ music reviews) from Notion to Obsidian using Bases. Asked ChatGPT for a few Python scripts to handle cleanup, covers, and metadata. Now it’s local, fast, and mine. Super impressed by what Bases already enables.

---

## Comments

> **GusBusRox** • [20 points](https://reddit.com/r/ObsidianMD/comments/1ma5gar/comment/n5c4ogo/) •
> 
> Obsidian mobile has Bases. Check the Obsidian discord for instructions. Works great on iOS
> 
> track me
> 
> > **deathverified** • [9 points](https://reddit.com/r/ObsidianMD/comments/1ma5gar/comment/n5c5y60/) •
> > 
> > You are right and I am stupid! I just never tested anything in iOS using TestFlight so I need to do some reading first … thank you!
> > 
> > **deathverified** • [9 points](https://reddit.com/r/ObsidianMD/comments/1ma5gar/comment/n5ccdgn/) •
> > 
> > OMG IT WORKS LIKE A CHARM THANK YOU
> > 
> > **PhoenixRiseAndBurn** • [3 points](https://reddit.com/r/ObsidianMD/comments/1ma5gar/comment/n5gg41c/) •
> > 
> > Is there a way to bases on mobile that doesn’t involve discord?

> **peroperozz** • [5 points](https://reddit.com/r/ObsidianMD/comments/1ma5gar/comment/n5c5to5/) •
> 
> So cool! Curious to see how it looks, if you don't mind sharing a screenshot!
> 
> I'd also been waiting for Obsidian to launch Bases before migrating all my massive tables from Notion over—brought over a few of my simpler ones and am hoping to do a larger migration when I have a bit more time to sift through things. Bases is a real game-changer for me (though I'd been happily using Obsidian even before that).
> 
> > **deathverified** • [2 points](https://reddit.com/r/ObsidianMD/comments/1ma5gar/comment/n5c6f4t/) •
> > 
> > I won’t have access to my pc for a while — but I’ll post/send you a screenshot on Monday! It doesn’t have all the bells and whistles of Notion (grouping for example) but it’s looking better than I expected!
> > 
> > You will be supper happy when you get to migrating out of Notion! :D

> **nearlynarik** • [5 points](https://reddit.com/r/ObsidianMD/comments/1ma5gar/comment/n5e3ibt/) •
> 
> This is great.
> 
> I wish more people were like you and shared HOW they made something and not just show. I feel so strongly I could almost call for posts that demo only without sharing how should be banned!! I’m not that harsh, there’s a time and place 😊

> **Eolipila** • [4 points](https://reddit.com/r/ObsidianMD/comments/1ma5gar/comment/n5ef889/) •
> 
> Regarding the second bonus upgrade: I suggest you try Obsidian Web Clipper extension for your browser. Basically, it will do everything the script does, but with the flexibility of having different templates also for other sites.
> 
> > **deathverified** • [4 points](https://reddit.com/r/ObsidianMD/comments/1ma5gar/comment/n5efix6/) •
> > 
> > Thanks! I do use it - but for my other vault where i treat it as a “read later” kind of thing. I didn’t think about this use case you mentioned though. It’s smart!
> > 
> > I think I gave up on using Clipper any other way than its stock functionality because I had some issues with it — couldn’t configure the AI, couldn’t change something etc., so I just gave up :D

> **mrirav7** • [3 points](https://reddit.com/r/ObsidianMD/comments/1ma5gar/comment/n5ffifx/) •
> 
> Is it available for public? It has been almost two months since it was released for catalyst user.

> **madderbear** • [2 points](https://reddit.com/r/ObsidianMD/comments/1ma5gar/comment/n5clkyr/) •
> 
> Thanks for the post! Such a nice explanation of how you've used two different apps to meet your needs. I'm loving Bases too.

> **its\_darkknight** • [1 points](https://reddit.com/r/ObsidianMD/comments/1ma5gar/comment/n5ehtu3/) •
> 
> Is bases out?

> **Critical-Pound2844** • [1 points](https://reddit.com/r/ObsidianMD/comments/1ma5gar/comment/n5gik43/) •
> 
> I'm really liking it so far. I would like to be able to do averages, sums, and the like. Can't wait.

> **read\_it\_too\_** • [1 points](https://reddit.com/r/ObsidianMD/comments/1ma5gar/comment/n5khacp/) •
> 
> Man, this is what I have been looking for ages... Bases...

> **read\_it\_too\_** • [1 points](https://reddit.com/r/ObsidianMD/comments/1ma5gar/comment/n5kysnb/) •
> 
> What is the expected roll out date for stable version for public? If anyone has any idea?