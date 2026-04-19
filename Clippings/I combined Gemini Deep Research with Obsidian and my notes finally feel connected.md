---
title: I combined Gemini Deep Research with Obsidian and my notes finally feel connected
source: https://www.makeuseof.com/gemini-deep-research-with-obsidian-connected-notes/?taid=69e55064ba4ee50001ee1fbb&utm_campaign=trueanthem&utm_medium=social&utm_source=twitter
author: "[[Saikat Basu]]"
published: 2026-04-19
created: 2026-04-19
description: I am using Gemini Deep Research and an Obsidian plugin to build a living knowledge base.
tags:
  - clippings
---
I am [a recent Obsidian convert](https://www.makeuseof.com/using-obsidian-as-beginner-now-understand-why-people-switch/). I already have a carefully tended folder hierarchy and a growing Graph system. With each step, I am trying to improve the research-to-note pipeline, which should help me dive deep into a topic by reading papers, following citations, and cross-referencing ideas. But I don't want to open Obsidian to dump a wall of unstructured text into a new file. Like every other notetaking enthusiast, I went in search of ways to find the insights buried under the raw material.

Then I thought about Deep Research in Gemini, and an Obsidian plugin called Gemini Scribe.

## Set up Gemini Scribe in five minutes

### You don't need a subscription

The **Gemini Scribe plugin** brings Google's Gemini AI models directly into Obsidian, turning it into an AI-powered [knowledge management system](https://www.makeuseof.com/knowledge-management-beginner-guide/). It lets you clean up, organize, and enrich your notes, and even pull in more information with a Google Search.

[Installing Gemini Scribe](https://github.com/allenhutchison/obsidian-gemini) sounds more complicated than it is. Go to Obsidian's Community Plugins tab and search "Gemini Scribe." Once installed, go to **aistudio.google.com**, grab a free API key, and paste it into the plugin settings. You can set your chat model to Gemini-2.5-pro for the best reasoning quality. But I suggest you experiment with the other models too.

A basic step is clicking **Initialize Vault Context** inside the plugin. This generates an AGENTS.md file at your vault root. The file influences the plugin's behavior in response to your prompts. Scribe reads this file before every single chat session. For instance, edit the simple Markdown file to describe your folder structure, note naming conventions, and the type of responses you want. It can be your vault’s "logic," your tagging rules, or your preferred note-taking style.

## Run Deep Research with better prompts

### Treat prompts like research briefs

![Running Gemini Deep Research.](https://static0.makeuseofimages.com/wordpress/wp-content/uploads/2026/04/gemini-deep-research.png?q=49&fit=crop&w=825&dpr=2)

Running Gemini Deep Research.

Go to Gemini, choose **Deep Research** toggle, and treat your prompt like a research report, not a search query. Writing the perfect prompt decides the quality of what ultimately lands in your Obsidian vault. Sometimes, I start with a vague idea in a new note ("Is spaced repetition the best hack for learning?"). Then, go over to Gemini and trigger the deep research.

Instead of asking for definitions, ask for comparisons, breakdowns, and limitations of a topic. If you have an old report, you can even upload it and research new findings and audit your knowledge gaps. Gemini's [Deep Research is also integrated with Google's Workspace apps](https://www.makeuseof.com/gemini-deep-research-wasnt-useful-to-me-until-i-did-this/).

As you can see, instead of prompting "explain spaced repetition," I asked: "Compare the leading mechanisms behind spaced repetition, identify where current models break down, and summarize what the research says about optimal review intervals for complex technical material."

## Import research as structured notes

### Your naming conventions matter for retrieval

![Obsidian Note with Deep Research inputs.](https://static0.makeuseofimages.com/wordpress/wp-content/uploads/2026/04/obsidian-note.png?q=49&fit=crop&w=825&dpr=2)

Obsidian Note with Deep Research inputs.

Once Deep Research finishes, export the report to Google Docs using the button at the top of the report. Copy the content and paste it into a new Obsidian note as plain markdown. Clean up the headers into the Markdown format and keep all source links intact as text. You can also press Copy to directly copy and paste it into Obsidian.

Name the note with a clear convention — something like **\[TopicName\] - Deep Research \[Date\]**. This keeps the imported research visually distinct from your own thinking inside the vault. I also add a "deepresearch" tag so I can filter these notes separately in Dataview.

## Link notes to activate context

### Connections improve AI answers

![Gemini Scribe Prompting.](https://static0.makeuseofimages.com/wordpress/wp-content/uploads/2026/04/gemini-scribe-prompting.png?q=49&fit=crop&w=825&dpr=2)

Gemini Scribe Prompting.

Before opening Scribe, manually add two or three \[\[backlinks\]\] inside the imported deep research note, pointing to existing related notes in your vault. Obsidian's own superpower is in [how you use backlinks](https://www.makeuseof.com/organize-notes-with-backlinks-for-easier-navigation/). But backlinks can also tell Scribe to read not just your current note, but every note it links to before generating a response. Now prompt Scribe:

> I just imported a Deep Research report on \[topic\]. Based on this note and its linked context, tell me what's already covered in my vault, what's genuinely new, and suggest three notes I should create to fill the gaps.

That's a fundamentally different output than asking Scribe without the linked context. The backlinks you add are like any other context window. The richer the connections you draw before running Scribe, the more precise the synthesis it returns.

After importing any Deep Research report, I go back to my old notes and run one follow-up Scribe prompt. Sometimes, it catches any drift between what the literature said when I imported the note and what it says now.

> Check whether anything published in the last six months contradicts the conclusions in this report.

## Organize your Obsidian notes

### Gemini Scribe can read, write, and clean up your vault

![Obsidian's File recovery](https://static0.makeuseofimages.com/wordpress/wp-content/uploads/2026/04/obsidian-file-recovery.png?q=49&fit=crop&w=825&dpr=2)

The Gemini Scribe agent can actively tidy up your notes by reading, writing, and even deleting files. Give it a messy list of notes on a topic, and it will scan through all of them and build a clean, structured overview table on its own.

It goes a step further, too. Before creating any file, the agent reads each note individually, summarizes its content, and in some cases links related notes into the description. The result can be a polished, connected map of your knowledge with minimal effort from you.

Since the agent can delete files, one wrong instruction could mean lost content. If that happens, recover your notes instantly by pressing **Ctrl/Cmd + P** and searching for **"File Recovery: Open Local History"** (see screenshot). Ensure File recovery is enabled from **Settings > Core plugins > File recovery > On**.

[Download from Obsidian](https://obsidian.md/download) [Download from Google Play](https://www.anrdoezrs.net/links/7251228/type/dlg/sid/UUmuoUeUpU2041982/https://play.google.com/store/apps/details?id=md.obsidian) [Download from App Store](https://apps.apple.com/us/app/obsidian-connected-notes/id1557175442) [Download from Flathub](https://flathub.org/en/apps/md.obsidian.Obsidian)

### A big picture question behind the note-taking

While using AI chatbots, I often think about how much of these reports and notes are actually mine if Gemini is doing the spadework? My answer is that the thinking I do because of what I find in my vault, the new questions, the project ideas, or the writing that come up is still mine. The research pipeline is a means to that end, not the end itself. Gemini Deep Research occasionally produces reports with confident-sounding errors on niche topics. Gemini Scribe can also mistake the mere mention of a keyword for relevance. This workflow isn't perfect, and there's more to Scribe that I couldn't include here. Still, this combination is worth trying to let your notes talk to each other.