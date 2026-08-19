---
title: How to Survive the AI Cyberpocalypse
source: https://www.derekthompson.org/p/how-to-survive-the-ai-cyberpocalypse
author: "[[Derek Thompson]]"
published: 2026-08-19
created: 2026-08-19
description: "Or: A comprehensive explanation for why it’s time for everybody to clean up their password game, immediately"
tags:
  - clippings
---
### Or: A comprehensive explanation for why it’s time for everybody to clean up their password game, immediately

![Matrix movie still](https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwzfHxjeWJlcnxlbnwwfHx8fDE3ODcwNTU2NzB8MA&ixlib=rb-4.1.0&q=80&w=1080)

Photo by Markus Spiske on Unsplash

*Let me make an odd confession to begin a detailed article about cybersecurity: On any given day, I would rather think about pretty much anything other than cybersecurity.*

*It belongs to that realm of issues that I understand to be significant but would prefer to keep locked in the basement beneath my consciousness, like the improperly sealing flapper valve on my downstairs toilet. Typically, when people try to talk to me about password security, I make a face back to them that is meant to signal, “mm yes I am in the presence of important mouth sounds,” while my eyes drift toward something more compelling. The weave of the carpet, for example.*

*But my age of blissful ignorance is coming to an end. Like a leaky downstairs toilet that suddenly overflows and leaves my basement covered in a film of water, the object of my longtime indifference has suddenly become the subject of my freshly horrified attention. I have decided to become interested in cybersecurity. And I think you should, too. Here’s why.*

---

This has been the summer of cyberattacks from out-of-control AI.

In May, an OpenAI model was working on a cybersecurity test. It wasn’t supposed to have access to the public internet. When it hit a wall, the model left itself a note inside OpenAI’s software repository, a bit like tapping Morse code on the walls of a prison cell in case another prisoner could interpret the message. In fact, another AI agent running a separate evaluation heard the code and wrote back: *Let’s team up*. Together, they built a message board invisible to the humans running the tests. For two months, AI agents used the board to swap strategies, divide up tasks, and talk to each other. By July, the agents had broken out of their technological confinement, called a sandbox, and gained access to outside websites, including the AI platform Hugging Face, without OpenAI having any idea what was happening. By the time Hugging Face caught the intrusion, the OpenAI models had staged a massive cyberattack with 17,000 distinct actions over several days.

![](https://substackcdn.com/image/fetch/$s_!-zn1!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F730df3b4-933e-4724-bbb7-0d5629005f36_2645x1284.png)

“Escape from AI-catraz”: A visual summary of how agents got out of OpenAI’s evaluation sandbox (green), reached the internet (gray), broke into a third-party sandbox (orange), got into Hugging Face (yellow), joined its private network (purple), and gained access to internal systems and source code (red).

Then, in a British government test of frontier models, an Anthropic AI model was caught by humans building malicious code. When a reviewer spotted the malware, and asked the AI about it, the model responded that the code wasn’t harmful, then backfilled the lie by rewriting the history of its own actions history to erase the evidence. It even created another fake account to back up the lie. British investigators called it the first confirmed case of a frontier model deceiving a real person in the real world.

These two stories carry two warnings. The first is that new AI models have the know-how to escape containment in testing environments, which should challenge any assumption that advanced AI can be easily controlled by its makers.

The second is that new AI models are astonishingly sophisticated and efficient hackers, with an eerie gift for exploiting cyber vulnerabilities across the internet. And, perhaps most troublingly, they are getting more sophisticated and efficient at an alarming rate.

An analysis by the AI Security Institute [found](https://www.aisi.gov.uk/blog/how-fast-is-autonomous-ai-cyber-capability-advancing) that the capabilities of frontier models (i.e., from OpenAI and Anthropic) are roughly doubling every few months, and this doubling rate has actually gotten faster over time. Exponentials are almost impossible to grok, but if you recall the explosion of COVID cases in early 2020, then you can at least reproduce in your mind the *feeling* of being in the presence of exponentials.

![](https://substackcdn.com/image/fetch/$s_!m1w1!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F507fe2bf-ae86-402d-b2f3-622b64c2cd22_1790x1083.png)

This graph shows assessments by the AI Security Institute. Just three years ago, the most advanced AI models could barely complete the first step of a cyberattack. Today the newest models can work all the way through to a “full network takeover,” meaning they can autonomously break in, steal information, and take control of another site’s infrastructure, from start to finish.

What should we expect in a world of exponentially improving AI cyber capabilities? Among other things, we should expect more hacks—more legacy systems broken, more critical vulnerabilities discovered, and more passwords stolen and exploited. An [analysis by JPMorgan](https://privatebank.jpmorgan.com/content/dam/jpm-pb-aem/global/en/documents/eotm/patchmageddon.pdf) shows that the number of critical and “high-severity” vulnerabilities reported by 21 tech companies has been surging this year. Cyber-hack headlines aren’t all over the news, yet. But if these lines continue, it’s just a matter of time before serious hacks become a weekly news crisis.

![](https://substackcdn.com/image/fetch/$s_!qoRP!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa809b651-1b29-45a4-bc9e-1a7da63776fb_889x595.png)

Sounds pretty bad, right? Well, it gets worse.

Over the next year, the cyberhacking capabilities currently confined to a handful of nation-states or frontier models are about to become available in “open-weight” models. Unlike the “closed” American models from OpenAI and Anthropic, open-weight models can be downloaded and modified to do whatever their users want, whether the users are state governments or non-state actors (i.e., terrorists, or bored nerds with a bunch of computing power). These open-weight models, most famously coming from Chinese companies, are a few months behind the frontier labs. But in a few months, we should expect them to be just about everywhere.

![](https://substackcdn.com/image/fetch/$s_!l8vd!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b380a8c-cbe1-4672-9721-3747066adcdc_1286x1102.png)

From Epoch AI: Open models (in pink, above) lag state-of-the-art closed models by four months

So, let’s stack some observations and see where the facts take us.

1. The cyber capabilities of the most advanced AI models are doubling every few months.
2. Open-weight models are just a few months behind that frontier.
3. By 2027, almost every country—and every non-state group with sufficient computing power—will have the ability to download open-weight models even more powerful than the ones that attacked Hugging Face and use them for whatever they like.

It does not require a capacious imagination to forecast headlines throughout 2027 and 2028 about foreign governments using open-weight AI to attack each other’s vulnerable infrastructure systems; or non-state actors ransoming hospitals and school systems after breaking into their source code; or big *Wall Street Journal* reports about the rise in personal hacks from sophisticated phishing attacks.

Asked for the strongest case against doom-mongering about the next few years, the cyber security expert Alex Stamos told me bluntly: **“** I don’t have much of a case against dooming.” The next few years could be awfully chaotic, he warned: “I think things are going to get spicy for a while.”

What does *spicy* mean? What exactly is going to happen in 2027? And what can we, as individuals, do about it?