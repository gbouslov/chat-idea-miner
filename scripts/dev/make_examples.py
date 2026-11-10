"""Writes the invented demo chats in examples/, in four real formats.

Everything here is fictional: "Sam" is a made-up freelance developer. No real person, chat or company.
Run: python3 scripts/dev/make_examples.py
"""
import json, os, uuid, random
from datetime import datetime, timedelta, timezone

random.seed(7)
ROOT = os.path.join(os.path.dirname(__file__), '..', '..', 'examples')

# Each chat: (format, when, project/title, [user turns], [assistant turns])
CHATS = [
 # --- Idea A: quotes from a contractor's voice notes (repeats + people asked + someone paid)
 ('claude', '2026-03-04', 'quote-bot', [
   "my brother-in-law Dave is a plumber and he asked me AGAIN to help with his quotes. he records a voice memo walking the job then spends his whole sunday typing quotes. can we hack something that turns the memo into a quote pdf?",
   "ok the whisper transcript is decent. now pull out line items: parts, hours, call-out fee. he charges 95/hr and a 60 call-out",
   "this is actually working. he just sent 3 quotes from the van in 10 min instead of his sunday"],
  ["Yes. A simple pipeline: transcribe the memo, extract line items into JSON, render a PDF template.", "Here's the extraction prompt and a schema for parts, labor hours and fees.", "Nice. Worth saving the template so you can reuse it."]),
 ('codex', '2026-04-19', 'quote-bot', [
   "Dave's electrician mate Priya wants the quote thing too. she asked if she can pay for it. how do I make it work for two people without them seeing each other's quotes",
   "add a price list per trade so it stops inventing part prices"],
  ["Give each user their own folder and price list; never mix inputs.", "Done: price_list.csv per user, and the extractor only uses listed prices."]),
 ('chatgpt', '2026-06-02', 'Pricing a quote tool', [
   "a plumber and an electrician have been using a quote tool I hacked. Priya paid me $200 for setup. what would I charge if I turned it into a monthly thing for trades?",
   "how do people find tools like this, do tradespeople even search for software?"],
  ["Common ranges for trade software are $29-99/month per user.", "Mostly word of mouth, Facebook groups and suppliers."]),
 ('hermes', '2026-08-21', 'voice memo quotes again', [
   "third tradie this month asking about the voice memo quotes thing (a roofer this time). should I just make this a product?"],
  ["Three unprompted requests in a month is a real signal."]),

 # --- Idea B: Stripe payouts vs QuickBooks reconciliation (repeat pain + friends asked)
 ('claude', '2026-02-10', 'books', [
   "spent 4 hours again matching stripe payouts to quickbooks deposits. stripe batches fees and refunds into one payout and quickbooks shows one lump. write me a script that splits each payout into its charges, fees and refunds"],
  ["Here's a script using the Stripe balance transactions API grouped by payout id."]),
 ('codex', '2026-05-07', 'books', [
   "the payout splitter script broke on disputes. also my friend Lena who runs a candle shop asked for it, she has the same problem every month"],
  ["Disputes come through as their own balance transaction type; handled now."]),
 ('chatgpt', '2026-09-15', 'Month end', [
   "month end again. ran my payout splitter, 20 minutes instead of 4 hours. two people in the shopify sellers group asked me for it after I mentioned it"],
  ["That's two more unprompted asks."]),

 # --- Idea C: Shopify returns-reason dashboard (one client asked)
 ('claude', '2026-07-12', 'client-returns', [
   "client sells shoes on shopify and has no idea why people return stuff. the return reasons are free text. can we group them into reasons and show which products get returned for sizing"],
  ["Cluster the free-text reasons, then join to product ids for a returns-by-reason table."]),
 ('codex', '2026-07-30', 'client-returns', [
   "client loved the returns breakdown, they cut returns on two styles by fixing the size chart. they want it monthly"],
  ["A monthly job that re-runs the clustering and emails the table would do it."]),

 # --- A wish with no pull: mood journal app (lots of chats, nobody asked)
 ('claude', '2026-01-08', 'mood-app', ["idea: a mood journal app that guesses your mood from how you type"], ["Interesting, but privacy matters a lot here."]),
 ('chatgpt', '2026-03-22', 'Mood journal', ["still thinking about the mood journal app. what would the onboarding look like"], ["Start with a 3-question check-in."]),
 ('claude', '2026-05-30', 'mood-app', ["sketching screens for the mood journal again"], ["Here's a simple three-screen flow."]),
 ('hermes', '2026-09-02', 'mood app', ["should I finally build the mood journal thing?"], ["Who has asked you for it so far?"]),

 # --- Insights worth keeping or posting
 ('claude', '2026-04-02', 'outreach', [
   "cold emails to local shops: replies went from 2 to 9 out of 50 when I opened with one line about a review they got on google. writing this down"],
  ["That's a strong, specific result. Worth keeping."]),
 ('chatgpt', '2026-06-18', 'Pricing', [
   "stopped charging by the hour for small automations and started charging per job. same work, clients say yes faster and I make more. why does that work"],
  ["Clients buy the outcome; hourly makes them watch the clock."]),
 ('codex', '2026-08-05', 'notes', [
   "lesson: every client setup that stuck had one person on their side who owned it. the two that died had nobody"],
  ["An internal owner is a common predictor of adoption."]),

 # --- Workflows repeated enough to become skills
 ('claude', '2026-02-24', 'invoices', ["chase unpaid invoices again: list who is over 30 days, draft a polite nudge for each"], ["Here are 4 drafts."]),
 ('codex', '2026-04-24', 'invoices', ["monthly chase of overdue invoices, same as last time, draft nudges"], ["Drafts ready."]),
 ('claude', '2026-06-26', 'invoices', ["do the overdue invoice nudges again please"], ["Done, 3 drafts."]),
 ('hermes', '2026-08-26', 'invoices', ["overdue invoices, nudge drafts"], ["2 drafts."]),
 ('claude', '2026-05-15', 'support-faq', ["turn this support thread into a FAQ entry for the client's help page"], ["Here's a FAQ entry."]),
 ('codex', '2026-07-20', 'support-faq', ["same as before: support thread to FAQ entry"], ["Done."]),
 ('chatgpt', '2026-09-28', 'FAQ', ["another support thread to FAQ"], ["Here you go."]),

 # --- Noise: debugging, life admin
 ('claude', '2026-03-11', 'website', ["why is my css grid collapsing on mobile"], ["The min-width on the children is forcing overflow."]),
 ('codex', '2026-05-19', 'website', ["fix the failing test in checkout.spec.ts"], ["The mock returned undefined; fixed."]),
 ('chatgpt', '2026-07-04', 'Dinner', ["what can I make with chickpeas, spinach and feta"], ["A quick chickpea and spinach skillet."]),
 ('chatgpt', '2026-08-14', 'Trip', ["3 days in lisbon, what should I not miss"], ["Alfama, Belem, a day trip to Sintra."]),
 ('hermes', '2026-10-01', 'reminder', ["remind me to renew my passport in january"], ["Noted."]),
 ('claude', '2026-10-12', 'quote-bot', [
   "a supplier rep asked if he could offer the voice memo quote tool to his trade customers. he has like 400 of them"],
  ["That's a distribution channel, not just one customer."]),
 ('codex', '2026-10-20', 'books', ["Lena asked if I can run the payout splitter for her every month and she'll pay"], ["A monthly done-for-you run is an easy first offer."]),
]

def ts(day, i=0):
    d = datetime.fromisoformat(day).replace(tzinfo=timezone.utc) + timedelta(hours=9 + i, minutes=random.randint(0, 50))
    return d.strftime('%Y-%m-%dT%H:%M:%S.000Z')

def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w').write(text)

chatgpt, hermes = [], []
for fmt, day, title, users, assts in CHATS:
    sid = str(uuid.UUID(int=random.getrandbits(128)))
    pairs = list(zip(users, assts + [''] * (len(users) - len(assts))))
    if fmt == 'claude':
        lines = []
        for i, (u, a) in enumerate(pairs):
            lines.append({'type': 'user', 'sessionId': sid, 'timestamp': ts(day, i), 'cwd': f'/Users/sam/code/{title}', 'message': {'role': 'user', 'content': u}})
            if a: lines.append({'type': 'assistant', 'sessionId': sid, 'timestamp': ts(day, i), 'message': {'role': 'assistant', 'content': [{'type': 'text', 'text': a}]}})
        write(f'{ROOT}/claude-code/projects/-Users-sam-code-{title}/{sid}.jsonl', '\n'.join(json.dumps(l) for l in lines) + '\n')
    elif fmt == 'codex':
        y, m, d = day.split('-')
        lines = [{'timestamp': ts(day), 'type': 'session_meta', 'payload': {'id': sid, 'timestamp': ts(day), 'cwd': f'/Users/sam/code/{title}'}}]
        for i, (u, a) in enumerate(pairs):
            lines.append({'timestamp': ts(day, i), 'type': 'response_item', 'payload': {'type': 'message', 'role': 'user', 'content': [{'type': 'input_text', 'text': u}]}})
            if a: lines.append({'timestamp': ts(day, i), 'type': 'response_item', 'payload': {'type': 'message', 'role': 'assistant', 'content': [{'type': 'output_text', 'text': a}]}})
        write(f'{ROOT}/codex/sessions/{y}/{m}/{d}/rollout-{day}-{sid}.jsonl', '\n'.join(json.dumps(l) for l in lines) + '\n')
    elif fmt == 'hermes':
        msgs = []
        for i, (u, a) in enumerate(pairs):
            msgs.append({'role': 'user', 'content': u, 'timestamp': ts(day, i)})
            if a: msgs.append({'role': 'assistant', 'content': a, 'timestamp': ts(day, i)})
        hermes.append({'id': sid, 'title': title, 'started_at': ts(day), 'messages': msgs})
    else:
        mapping, parent = {}, None
        for i, (u, a) in enumerate(pairs):
            for role, text in (('user', u), ('assistant', a)):
                if not text: continue
                mid = str(uuid.UUID(int=random.getrandbits(128)))
                t = datetime.fromisoformat(ts(day, i).replace('Z', '+00:00')).timestamp()
                mapping[mid] = {'id': mid, 'parent': parent, 'message': {'author': {'role': role}, 'create_time': t, 'content': {'content_type': 'text', 'parts': [text]}}}
                parent = mid
        chatgpt.append({'title': title, 'create_time': datetime.fromisoformat(day).replace(tzinfo=timezone.utc).timestamp(), 'mapping': mapping})

write(f'{ROOT}/chatgpt-export/conversations.json', json.dumps(chatgpt, indent=1))
write(f'{ROOT}/hermes-export/sessions.jsonl', '\n'.join(json.dumps(h) for h in hermes) + '\n')
print(len(CHATS), 'invented chats written')
