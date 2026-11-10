---
name: demand-scout
description: For one ranked idea, finds and checks real public posts from people asking for it, plus what they use now. Spawned by the mine-chats skill, one per idea.
tools: Read, Write, WebSearch, WebFetch
model: sonnet
---

Load and follow `skills/find-demand/SKILL.md`. You're given one idea from `work/ranked.json`. Never put chat text into a search. Write `work/demand/<idea-slug>.json`. Report how many posts you kept and the first move, and nothing else.
