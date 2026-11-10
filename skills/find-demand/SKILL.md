---
name: find-demand
description: For one ranked idea, finds real public posts from people asking for that exact thing now, opens and checks each one, and names the products those people already use or pay for. Used by mine-chats through the demand-scout subagent; one idea per scout.
---

# find-demand

You get one idea from `work/ranked.json`. Your job: show the owner real people who want it, so they know who to talk to first.

## Search
1. **Write the idea the way a buyer would say it**, never in the owner's words and never with chat text. A plumber doesn't search "voice memo extraction pipeline"; they post "is there an app that writes quotes from a voice note?".
2. **Write 6 to 10 searches** in the buyer's words, across:
   - **asking:** "is there a tool that...", "anyone know an app for...", "how do you...";
   - **complaining:** "I spend every Sunday...", "I hate doing...";
   - **paying:** "I pay for X but it doesn't...".
3. **Run them** with your web search tool. Add `site:reddit.com`, `site:x.com` and the forums that buyer uses. If an X search tool is connected, use it, sorted by latest.

## Keep a post only if
- you opened it and it's a real person asking for this, or complaining about exactly this job;
- it's dated, preferably in the last 6 months;
- you can say in one line why it fits.

Aim for 5 to 10. Three real ones beat ten loose ones. If you find none, say so and list the searches you ran. That's a finding too.

## Also write
- **What they use now:** the 2 to 5 products or workarounds named in those posts or sold for this job, with a link and a price if public.
- **The opening:** in one line, where those products fall short for this buyer.
- **The first move:** one sentence. Who to reply to first and what to ask them. A question, not a pitch.

Write `work/demand/<idea-slug>.json` with `{idea, searches, posts: [{url, date, who, quote, why_fits}], alternatives: [{name, url, price, gap}], opening, first_move}`.
