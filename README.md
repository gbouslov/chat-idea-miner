# chat-idea-miner

Your old AI chats are full of ideas you forgot about. This finds them, then finds the people already asking for them.

A free skill for **Claude Code** and **Codex**. It reads your own chats from Claude Code, Codex, Hermes, ChatGPT and Claude.ai, and writes you four files:

- **`IDEAS.md`**: the things you could sell, ranked. Each one shows the chats it came from, with your own words. What ranks highest: someone else asked for it, someone paid, you have a before-and-after number.
- **`WHO-WANTS-IT.md`**: for your top 3, real people posting right now that they need exactly that, with links, plus what they already pay for and where it falls short.
- **`INSIGHTS.md`**: lessons with a result behind them, worth keeping or posting.
- **`SKILLS.md`**: jobs you keep asking the AI to do again, drafted as skills.

Everything runs on your machine. Your chats are never uploaded or put into a search.

## Run it

```bash
git clone https://github.com/gbouslov/chat-idea-miner
cd chat-idea-miner
claude          # or: codex
```

Then paste:

```
find the ideas in my old chats
```

**Try the demo first.** Paste `find the ideas in my old chats, use the example chats` to run it on 30 invented chats from a fictional freelancer. The result is in [DEMO.md](DEMO.md).

## Where it looks
| Source | Where | What to do |
|---|---|---|
| Claude Code | `~/.claude/projects` | nothing |
| Codex | `~/.codex/sessions` | nothing |
| Hermes | its session store | `hermes sessions export --format jsonl ~/chat-exports/hermes.jsonl` |
| ChatGPT, Claude.ai | Settings → Export data | unzip, then say "also read ~/Downloads/<folder>" |

Lots of chats? Say "only the last 3 months" and it uses `--since`.

## How it works
One skill runs five steps:
1. **`scripts/extract.py`** finds your chats and splits them into shards. That's the only script, and it makes no judgments.
2. **`chat-reader` subagents**, one per shard and in parallel, read every line and write down each sellable idea, insight and repeated job, with your exact words as the evidence.
3. **`rank-ideas`** merges them across all your chats. Pull beats polish: three people asking for something beats one idea you love.
4. **`demand-scout` subagents**, one per top idea, search the web, Reddit and X for people asking for it now, and open every link they keep.
5. **`write-report`** writes the four files.

The skills are in [`skills/`](skills) and the subagents in [`.claude/agents/`](.claude/agents). Codex reads [`AGENTS.md`](AGENTS.md).

## License
MIT
