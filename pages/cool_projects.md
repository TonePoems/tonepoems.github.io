---
layout: default
title: "Cool Projects"
permalink: /Cool_Projects
---

# Cool Projects

These are projects that I either found inspiration from, reference often, or just generally think are neat. 

This page is broken up into 

- [Technical Projects](#technical-projects)
- [Technical Articles/Blogs](#technical-articles)
- [Documentation and Visualization Tools](#documentation-and-visual-tools)



## Technical Projects

This is a collection of some of my favorite projects found online. They are usually a source of thought, inspiration, and often a good amount of imposter syndrome. I obviously don't have strict criteria for what projects really stick with me, but I have found that most often their motivation statement could be `¯\_(ツ)_/¯`. These projects are really exciting to me.

I will attempt to provide a decent summary of each, but please check out the original sources!

---

### [Button Stealer](https://anatolyzenkov.com/stolen-buttons/button-stealer)

A Chrome extension that "steals" a button from every website you open, adding it to a trophy wall of buttons you have encountered.

---

### [Extremely Linear Git History](https://github.com/zegl/extremely-linear)

Why use random checksums when you could use neat and tidy ordered numbers?

---

### [Open and Shut](https://github.com/veggiedefender/open-and-shut)

Type in Morse code by repeatedly slamming your laptop shut (Really worth checking out the readme for an example).

---

### [Copy Dialog Lunar Lander](https://github.com/Sanakan8472/copy-dialog-lunar-lander)

Play Lunar Lander in the Windows copy dialog box.

Why I love this so much:

- The idea of landscape from file transfer speed
- Difficulty level based on connection stability
- Messing with system settings to get "different worlds"
    - "OS built-in level editor"

---

### [WordTeX](https://www.youtube.com/watch?v=jlX_pThh7z8) 

A great video on typesetting in Word.

Also has a brief section on the Turing completeness of autocomplete, because why not.

---

### [The Fuck](https://github.com/nvbn/thefuck)

A command line application that corrects errors in previous console commands. It also allows setting an alias for a cleaner console log...

Example:

```
> git push
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master


> fuck
git push --set-upstream origin master [enter/↑/↓/ctrl+c]
Counting objects: 9, done.
```

---

### [Badness 0](https://www.youtube.com/watch?v=Y65FRxE7uMc)

A fantastic video from [suckerpinch](https://www.youtube.com/@tom7) that has a unique approach to typesetting. An awesome amount of work for a really fun product. 

---

### [Solid State Volumetric Display](https://youtu.be/wrfBjRp61iY?si=z9dZ_cHXfWCrwzCK)

![Solid State Volumetric Display image](..\resources\images\volume_display.png)

A cool video of a topic I find randomly interesting, volumemetric displays. Most of them are created with spinning or linear movement, so this is a neat approach. 

---


## Technical Articles
I have several blogs and technical sites I like to read. Usually get a batch of them every month then try to get through one a day. Gives a break from technical stuff, easy reading during lunch, or expand my range a bit. Started this a few years ago when a former boss suggested daily reading as a habit for expanding/connecting ideas and staying current with interesting things.

- [Stack Overflow Blog](https://stackoverflow.blog/): Mainly focused on Webdev and AI right now. Some interesting things in their history.

- [Stack Exchange hot questions](https://stackexchange.com/questions?tab=hot): A lot more random things, find something interesting every now and again.

- [Stephen Wolfram Writings](https://writings.stephenwolfram.com/) Math and technical heavy. His personal and work writeups are nuts.

- [Halfbakery](https://www.halfbakery.com/): Just for fun/fuel to my never-ending list of side projects I'll totally get to one day...

- [Joel on Software](https://www.joelonsoftware.com/): Not many updates but older articles.

- [Atlassian Blog](https://www.atlassian.com/blog): Most recent addition. Pretty liberal/HR heavy approaches but food for thought. I really like their concept of playbooks that they share in some of them.

- [RJ Andrews](https://www.chartography.net/) is the data scientist who did the "Info We Trust" book and the moon landing website. I'm subscribed to his monthly(?) newsletter.

- [Neil and Buzz Go for a Walk](https://tranquility.infowetrust.com/)
   - A fantastic interactive timeline of the first moon landing, created by the above RJ Andrews. He also has a [great writeup](https://infowetrust.com/project/tranquility-design) docmenting the process of creating it. This is a top tier example of getting a wide amount of info across in a clean and clear way. 


## Documentation and Visual Tools

Sourced from some work notes:

Someone asked today about Mermaid, and it made me want to share some of the other documentation and visual tools I've collected. Figured I should share the list with the whole operation. Please add to it if you have anything else!

- Obsidian: Great general purpose notetaking tool. Has good plugin support.

    - [Obsidian Kanban plugin](https://github.com/mgmeyers/obsidian-kanban): Creates a Kanban board for small tasks I can move as needed.

    - [Excalidraw plugin](https://github.com/zsviczian/obsidian-excalidraw-plugin): Integrates [Excalidraw]([https://excalidraw.com/](https://excalidraw.com/)), a feature rich sketching tool, into Obsidian.

    - [Obsidian Git plugin](https://github.com/denolehov/obsidian-git): Allows automatic backups of your obsidian vault.

    - [Dataview plugin](https://github.com/blacksmithgu/obsidian-dataview): Uses SQLite like commands to aggregate data from different files in the vault. I use it for totaling hours for my different projects to track percentages

    - Obsidian Checkboxes: I recently found a cool theme that extended markdown checkbobxes for different uses! So here it is in [snippit form](../resources/checkboxes.css), simply drop in your Obsidian Snippits folder and load into your application (May not work with all custom themes, but you can just modify the css).
        
```
- [ ] open  
- [x] complete  
- [!] important  
- [>] deferred  
- [?] question  
- [i] info  
- [-] canceled   
- [/] partial
```

- [Excalidraw](https://excalidraw.com/): Deserves its own mention outside of the Obsidian plugin

- [Mermaid](https://mermaid.live/): Great for a range of diagrams, flow, sequence, class, and git! There is also Obsidian support for simple Mermaid style diagrams within code blocks

- [Ascii Flow](https://asciiflow.com/): Good tool for generating formatted text blocks with proper spacing for code comments

- [Fighter Brief](https://fighterbrief.com/): Huge shoutout to John DeWeese for introducing this to me. Cool way to display a range of military equipment and movement. NOT CUI SAFE, just fun to mess around with.

- [Symbl](https://symbl.cc/): for all your symbol needs



{% include footer.html %}
