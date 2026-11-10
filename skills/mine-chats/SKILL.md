---
name: mine-chats
description: Reads your own old AI chats (Claude Code, Codex, Hermes, ChatGPT and Claude exports), finds the things you could sell, the insights worth keeping and the workflows worth turning into skills, then sends subagents to find real people asking for your best ideas right now. Use when someone says "find the ideas in my old chats", "what could I sell from my chats", "mine my Claude history" or "what have I already built that people want".
---

# mine-chats

You run the whole job. It's five steps, each with its own skill. Scripts only find and split files; every judgment is yours or a subagent's.

**Reader:** the person who owns these chats. They want to come away thinking "my best idea was already in there, and here are the people who want it".

## Before you start
- Everything stays on this machine. Write outputs to `out/` (gitignored). Never paste chat text into a public place, a commit or a web search. Searches use the idea in your own words, not their chat.
- Ask nothing you can find yourself. Say what you're about to read and how much, then go.

## Steps

1. **Find and split the chats.** Run `python3 scripts/extract.py --out work` (add `--examples` for the demo, `--add PATH` for exports, `--since YYYY-MM-DD` to limit).
   - For Hermes, export first: `hermes sessions export --format jsonl ~/chat-exports/hermes.jsonl`, then `--add ~/chat-exports/hermes.jsonl`.
   - For ChatGPT or Claude.ai, unzip the export and `--add` the folder with `conversations.json`.
   - Read `work/manifest.json` and tell the user: how many chats, from where, which dates, how many shards.
   - If there are more than 40 shards, offer `--since` for the last 3 or 6 months first, and say why: it's faster and the recent work is usually the live work.

2. **Read every shard** with the `read-chats` skill, through the `chat-reader` subagent, one subagent per shard, in parallel batches of up to 8. Each writes `work/found/shard-NN.jsonl`. Do not skim, keyword-search or sample: a subagent reads its whole shard.

3. **Merge and rank** with the `rank-ideas` skill. It writes `work/ranked.json`: sellable ideas, insights and repeated workflows, each with its evidence.

4. **Find who wants it** with the `find-demand` skill, through the `demand-scout` subagent, one subagent per top idea (3 by default), in parallel. Each searches the open web and social sites for people asking for that thing now, opens every link it keeps, and names what those people already pay for.

5. **Write the report** with the `write-report` skill: `out/IDEAS.md`, `out/WHO-WANTS-IT.md`, `out/INSIGHTS.md`, `out/SKILLS.md`. Then tell the user, in five lines or fewer, the one idea to do first, why, and the first thing to do tomorrow.

## When something's missing
- **No web search:** run steps 1 to 3, write the report, and say plainly that the demand step didn't run.
- **A source fails to parse:** keep going with the rest and list the file in the report.
