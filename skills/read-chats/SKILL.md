---
name: read-chats
description: Reads one shard of someone's old AI chats in full and writes down every sellable idea, insight and repeated workflow in it, each with the chat id, date and the exact words that show it. Used by mine-chats through the chat-reader subagent; one shard per reader.
---

# read-chats

You get one shard: `work/shards/shard-NN.md`. Read all of it. Every block starts `### <chat id> | <date> | <source> | <project>`. `YOU:` is the owner, `AI:` is the assistant (trimmed).

## What to look for
Write one JSON line per finding to `work/found/shard-NN.jsonl`:

```json
{"kind": "sell|insight|workflow", "name": "short name in plain words", "what": "one sentence",
 "chat": "c0003", "date": "2026-03-04", "file": "...", "quote": "the owner's exact words that show it",
 "signals": ["asked", "paid", "repeat", "built", "result", "wish"], "note": "why this counts"}
```

- **sell:** a thing the owner built, fixed or kept doing that someone else could pay for. A tool, a service, a template, a done-for-you job.
- **insight:** a lesson with a result behind it, in the owner's words. "Replies went from 2 to 9 out of 50 when..." counts. A vague opinion doesn't.
- **workflow:** the same job asked of the AI again and again ("same as last time", "again"). That's a skill waiting to be written.

## The signals, in order of weight
1. **asked:** someone other than the owner asked for it ("he asked me again", "she wants it too").
2. **paid:** money changed hands or was offered.
3. **result:** a measured before and after (4 hours to 20 minutes).
4. **repeat:** it comes back across chats. You only see one shard, so note it; rank-ideas counts across shards.
5. **built:** a working version exists.
6. **wish:** the owner keeps wanting it, but nobody asked. Record it, marked `wish`. It's a lead, not a win.

## Rules
- The quote is copied exactly from a `YOU:` line, never paraphrased, never from an `AI:` line.
- One finding per chat per idea. Several chats about the same idea are several lines; rank-ideas merges them.
- Skip debugging, recipes, travel and admin unless the owner turned them into something others want.
- If the shard has nothing, write an empty file and say so. Don't invent a finding to fill it.
