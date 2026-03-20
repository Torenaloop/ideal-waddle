---
title: Prompts that actually use Copilot's M365 integration and not just "summarize this document"
source: https://www.reddit.com/r/microsoft_365_copilot/comments/1r4dgai/prompts_that_actually_use_copilots_m365/
author: "[[Difficult-Sugar-4862]]"
published: 2026-02-14
created: 2026-02-14
description: Reddit is where millions of people gather for conversations about the things they care about, in over 100,000 subreddit communities.
tags:
  - clippings
  - ChatGPT
  - CoPilot
  - prompts
---
Most prompt lists you see online are just generic ChatGPT prompts repackaged for Copilot. The whole point of M365 Copilot is that it can access your emails, calendar, files, and Teams, so I built prompts that actually leverage that.

Here are the ones that made a real difference:

**Cross-app prompts (these are the power moves):**   

1. "Look at my emails and Teams messages from the past week about \[project name\]. Create a RAG status update (Red/Amber/Green) covering: timeline, budget, scope, and risks. Include specific evidence for each rating."
2. "From my calendar next week, identify meetings that overlap with deadlines mentioned in my recent email threads. Flag any conflicts I need to resolve."
3. "Find all emails this week where I was CC'd but where there's an implicit ask that I respond. Summarize what's expected of me."

**Outlook-specific (beyond basic summaries):**

4\. "Review my sent emails from the past 2 weeks. Flag any where I committed to a deadline that's now less than 3 days away and I haven't followed up or delivered."

5\. "Identify email threads where I'm the bottleneck, someone is waiting on my input for more than 48 hours."

6\. "Draft follow-up emails for all threads where I asked a question more than 3 days ago and didn't receive a response."

**Teams + meetings:**

7\. "From my last 3 meetings with \[person/team\], compile: decisions made, action items assigned to me, and anything I said I'd do but haven't yet."

8\. "Compile a 1-page briefing for my meeting with \[person\] tomorrow: our recent email exchanges, shared documents, and open items."

**The key:** These work because they ask Copilot to connect information across apps — that's the capability you're paying for. If your prompt could work in ChatGPT without any M365 access, you're underusing Copilot.

What integration-specific prompts have you found useful?

You can find more prompts in my github repo [https://github.com/kesslernity/awesome-microsoft-copilot-prompts](https://github.com/kesslernity/awesome-microsoft-copilot-prompts)

---

## Comments

> **compuwatcher** • [1 points](https://reddit.com/r/microsoft_365_copilot/comments/1r4dgai/comment/o5bzjh2/) •
> 
> I used copilot memory to store my primary clients. Then before each of their weekly meetings I have copilot look at last week's loop page and all my emails and teams messages for the last 7 days.
> 
> I also get a status report for my main clients that I send to my boss.
> 
> Im a big fan of the multi sources with my prompts.
> 
> > **Difficult-Sugar-4862** • [1 points](https://reddit.com/r/microsoft_365_copilot/comments/1r4dgai/comment/o5bzsl1/) •
> > 
> > oh this is nice, thanks for sharing that, i will give it a try on my side.

> **JoyKil01** • [1 points](https://reddit.com/r/microsoft_365_copilot/comments/1r4dgai/comment/o5b9wov/) •
> 
> These are excellent.
> 
> I have to do monthly status reports per project. I use a prompt for my project ID email, calendar, teams and meeting minutes to summarize activities for the last month and what’s coming up for next month.
> 
> > **Difficult-Sugar-4862** • [2 points](https://reddit.com/r/microsoft_365_copilot/comments/1r4dgai/comment/o5ba4jk/) •
> > 
> > Happy you like them. 🤓 If you are interested i have compiled some more on a github repo. Let me know and ill share the link.

> **ExcellentWinner7542** • [1 points](https://reddit.com/r/microsoft_365_copilot/comments/1r4dgai/comment/o5bgao4/) •
> 
> I have an agent that has access to anything I have access to in the workplace and I have limited access to just that and no web searching. It's amazing what I have been able to learn about my business and what my leadership and coworkers are up to.
> 
> > **Difficult-Sugar-4862** • [1 points](https://reddit.com/r/microsoft_365_copilot/comments/1r4dgai/comment/o5bgd52/) •
> > 
> > Oh nice, how did you build it?
> > 
> > > **ExcellentWinner7542** • [1 points](https://reddit.com/r/microsoft_365_copilot/comments/1r4dgai/comment/o5bvvw6/) •
> > > 
> > > When adding docs and files I noticed you could select an option to grant access to everything I have access to. Then I selected to only use my included references and no web access.
> > > 
> > > > **Difficult-Sugar-4862** • [1 points](https://reddit.com/r/microsoft_365_copilot/comments/1r4dgai/comment/o5bwuvp/) •
> > > > 
> > > > Nice, thats a good catch

> **RB20AE** • [1 points](https://reddit.com/r/microsoft_365_copilot/comments/1r4dgai/comment/o5c2b2h/) •
> 
> Looking at prompt 1. I have just built a Copilot Studio agent that does exactly that from our weekly Highlight Reports we submit. I did have to create a Canvas app which helps PM's give the agent structured data otherwise it would be a mess. I also then have a Power Automate flow which will send a email with all the reports in and summerised every monday morning.
> 
> > **Difficult-Sugar-4862** • [1 points](https://reddit.com/r/microsoft_365_copilot/comments/1r4dgai/comment/o5c5bnq/) •
> > 
> > Oh yeah all the way to agents that is very nice. How was your experience with creating the agent itself? I dont have the license on my side to do that.

> **Echoed\_In\_Silence** • [1 points](https://reddit.com/r/microsoft_365_copilot/comments/1r4dgai/comment/o5cpxz7/) •
> 
> Awesome !!
> 
> > **Difficult-Sugar-4862** • [1 points](https://reddit.com/r/microsoft_365_copilot/comments/1r4dgai/comment/o5cq9km/) •
> > 
> > Thanks glad you like them.