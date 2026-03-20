---
title: "An Obsidian kick start for students"
source: "https://brunoamaral.eu/an-obsidian-kick-start-for-students/"
author:
  - "[[Bruno Amaral]]"
published: 2025-09-19
created: 2025-09-29
description: "It's not about taking notes; it's about making notes as a way to help knowledge stick. Obsidian connects notes automatically, and the process of giving structure to loose bits while writing helps me learn better."
tags:
  - "clippings"
---
My first time using Obsidian was confusing and useless. I gave up in an hour.

On another try, and copying some ideas from friends, I came up with a nice system that I think is simple and adaptable to many areas.

And this year, I am starting an MA class on Artificial Intelligence for Public Relations, which gave me the idea of making a simpler version to share with students. It already includes some content on AI terms and their meaning. You can download it below.

## How the system works

### Entities

Notes are created based on a set of entities:

1. Clippings
2. Definitions
3. Literature Notes
4. Meetings
5. Organisations
6. Persons
7. Prompts

There are a few others, but they aren't important.

What makes an `Entity` is the existence of a Template. On Obsidian, you can apply a template to a new note by writing `/template` and hitting enter before you start adding content. The template with apply some placeholders and properties to save you time.

The starter pack above already has templates for each entity. It also has a trigger to organise the notes in the right folder when you apply the template.

If I need to change a note from one type of entity to another, I simply change the note property `Kind` to the name of the entity and move it to the right folder. In the screenshot below, you will notice that on the left-hand side notes are styled based on the kind of entity associated with them. Any stray note will stand out to make it easier to file under the right folder.

![](https://brunoamaral.eu/content/images/size/w600/2025/09/image-12.png)

An actual example, I am working on implementing an LLM specific for Clinical Trials using ideas developed by João Nabais. There are also two literature notes linked to this plan, a mention of the Organisation, and a relevant clipping.

Let's look at each entity and what they mean.

**Clippings** are notes created from webpages using the [Obsidian Web Clipper](https://obsidian.md/clipper?ref=brunoamaral.eu). Nothing special for now, we are just saving something that may be useful.

![](https://brunoamaral.eu/content/images/size/w600/2025/09/image-8.png)

An actual example, I am working on implementing an LLM specific for Clinical Trials using ideas developed by João Nabais. There are also two literature notes linked to this plan, a mention of the Organisation, and a relevant clipping.

**Definitions** are exactly that, a glossary of terms with their examples and sources. And I make a lot of use of the `aliases` option so that both "AI" and "Artificial Intelligence" can both be linked automatically by Obsidian.

![](https://brunoamaral.eu/content/images/size/w600/2025/09/image.png)

An actual example, I am working on implementing an LLM specific for Clinical Trials using ideas developed by João Nabais. There are also two literature notes linked to this plan, a mention of the Organisation, and a relevant clipping.

The **literature notes,** can be created manually or fetched from [Zotero](https://zotero.org/?ref=brunoamaral.eu).

![](https://brunoamaral.eu/content/images/size/w600/2025/09/image-2.png)

An actual example, I am working on implementing an LLM specific for Clinical Trials using ideas developed by João Nabais. There are also two literature notes linked to this plan, a mention of the Organisation, and a relevant clipping.

Notice the format of the Literature Note title: `@amaralCommunicationStrategySolving2019`. This is because the note was fetched from Zotero using the [Zotero Integration](https://github.com/mgmeyers/obsidian-zotero-integration?ref=brunoamaral.eu) plugin. This idea comes from [Alexandra Phelan's workflow for working with Zotero and Obsidian](https://medium.com/@alexandraphelan/an-updated-academic-workflow-zotero-obsidian-cffef080addd?ref=brunoamaral.eu).

The **Meetings** are self-explanatory, and they make more sense when you create a **Person** note. The screenshot below shows a person and their linked mentions. One of those linked mentions is a meeting note where they are mentioned.

For meetings, I follow the format YYMMDD, `250930 {title}`, to help sort by date. ([An idea I got from Rui Carmo](https://taoofmac.com/space/blog/2024/11/27/1900?ref=brunoamaral.eu).)

![](https://brunoamaral.eu/content/images/size/w600/2025/09/image-4.png)

An actual example, I am working on implementing an LLM specific for Clinical Trials using ideas developed by João Nabais. There are also two literature notes linked to this plan, a mention of the Organisation, and a relevant clipping.

And since this is PR, there is also an **Organisation** entity.

![](https://brunoamaral.eu/content/images/size/w600/2025/09/image-5.png)

An actual example, I am working on implementing an LLM specific for Clinical Trials using ideas developed by João Nabais. There are also two literature notes linked to this plan, a mention of the Organisation, and a relevant clipping.

With **Persons** and **Organisations**, we can create stakeholder graphs by connecting notes.

![](https://brunoamaral.eu/content/images/size/w600/2025/09/image-6.png)

An actual example, I am working on implementing an LLM specific for Clinical Trials using ideas developed by João Nabais. There are also two literature notes linked to this plan, a mention of the Organisation, and a relevant clipping.

As for **prompts**, they are just a collection of copy-paste instructions for LLMs.

![](https://brunoamaral.eu/content/images/size/w600/2025/09/image-7.png)

An actual example, I am working on implementing an LLM specific for Clinical Trials using ideas developed by João Nabais. There are also two literature notes linked to this plan, a mention of the Organisation, and a relevant clipping.

### How it works

When I am trying to learn something, I will start from books or articles and create a **Literature note** for each. I write down what I learned and some quotes from the book. Basic stuff.

Concepts that I realise are important will get their own **Definition** note, and a link back to the Literature Note where I got it from.

When I am working on a problem, an article, or anything that requires connecting a lot of thoughts, I start with a draft on Obsidian.

![](https://brunoamaral.eu/content/images/size/w600/2025/09/image-9.png)

An actual example, I am working on implementing an LLM specific for Clinical Trials using ideas developed by João Nabais. There are also two literature notes linked to this plan, a mention of the Organisation, and a relevant clipping.

The graph on the right can also be expanded to include neighbour nodes and help me find related notes I may have forgotten. Or, I can click the nodes to navigate through the relationships and discover connections manually.

![](https://brunoamaral.eu/content/images/size/w600/2025/09/image-10.png)

When I mouse over the literature notes, I get their reference and link, and can also see a preview of the content if I wait a little longer.

![](https://brunoamaral.eu/content/images/size/w600/2025/09/image-11.png)

## Why it works for learning

Some subjects I can grasp just by reading and saving a few clippings for later reference. For complex topics, I need to write things down in a number of ways. Handwritten notes, pdf files, photos, social media posts, and whatever else I think may help.

Obsidian is made of text files, and I can throw all those bits and pieces into notes that will connect with each other. Obsidian connects them automatically by finding the note's title or aliases. It's the "unlinked mentions" section on the footer of the note.

It's the process of giving structure to these loose bits and writing a note, or a blog post, that helps me learn better. It's not about *taking* notes; it's about *making* notes as a way to help knowledge stick to the brain.

## Why it works for AI

Obsidian uses a text format called [Markdown](https://www.markdownguide.org/?ref=brunoamaral.eu) to style notes and give them structure. Turns out that LLMs can handle markdown pretty well.

This means that if I need to pass extra context to a prompt I can just drag and drop the notes into any AI chat; as a result, I save time writing the prompt and get a much better output.

I have also been testing Claude these past few weeks. The main advantage of Claude over ChatGPT is the way that it can connect to other apps and services, like Notion and Obsidian. Using Claude, I can actually have a conversation with my notes about specific topics.

## Why it works at all

Maybe this won't work for everyone and everything, and maybe sometime next month something will come along that is simpler and does a much better job. Until then, I felt this was good enough to share and hope it can be helpful to you.

Or even better, maybe someone is reading this and has a method that is simpler to grasp and easier to use.

It's good to keep in mind that there isn't a single right way to use Obsidian; it just gives you a set of functionalities. It's up to you to create a system that works the way you want to.