# PRD: BuildtheCrew

**Author:** Brent O'Malley
**Date:** 2026-05-08
**Status:** Draft — Stage 4 (Solution Review)

---

## 1. Hypothesis

We believe that giving distributed family + friend "crews" an AI-powered coordination app for aging-in-place loved ones will increase the number of older adults who successfully remain in their homes (vs. moving to assisted living) by reducing coordinator burnout and missed care tasks, measured by `[NEED: target metric — e.g., % of crews still active at 6 months, or self-reported caregiver burnout score]`.

## 2. Problem

**Who:** Adult children, siblings, friends, and neighbors of an older adult (typically 75+) who wants to age in place. The person who downloads the app is rarely a single "primary caregiver" — it's a *crew* of 3-12 people scattered across cities, with uneven availability and skills. None of them live with the loved one.

**How bad it is:**
- `[NEED: paste caregiver burnout stat — e.g., AARP "X% of family caregivers report high stress"]`
- `[NEED: paste aging-in-place demand stat — e.g., AARP "X% of adults 50+ want to remain in current home"]`
- `[NEED: paste market size — # of family caregivers in the US, projected growth]`

**Customer evidence:**
- `[NEED: paste 3-5 direct caregiver quotes from your user interviews — the rawer the better]`
- Common themes from interviews: `[NEED: 3 themes from your research, e.g., "the group text is unmanageable," "I don't know who's checking in this week," "Mom needs the gutters cleaned and nobody knows a good handyman"]`

**Current workarounds (proof the pain is real):**
- Group texts / WhatsApp threads that nobody can keep track of
- Shared Google Calendars manually maintained by one exhausted person
- Spreadsheets of meds, doctors, and contractors passed around as PDFs
- One sibling silently absorbing 80% of the coordination labor

**If we don't solve it:** Loved ones get moved to assisted living earlier than they want to, families fracture under uneven labor distribution, and the lead coordinator burns out (a documented health risk in itself).

## 3. Strategic Fit

**Why this, why now:**
- Aging baby boomers — the largest generational cohort — are entering the 75+ window over the next decade.
- Adult children are more geographically dispersed than any prior generation.
- AI is finally good enough to do the coordination work that requires *judgment* (who to assign, what's urgent, summarizing chaos) — not just calendaring.

**Competitive context:**
- **Lotsa Helping Hands / CaringBridge:** Calendar-based meal trains. Built for short-term crises (cancer, surgery), not multi-year aging-in-place. No AI, no service hiring.
- **Papa:** Pairs elders with paid companions. Solves loneliness for the elder, not coordination across the family.
- **Carely / ianacare:** Caregiver coordination but caregiver-led, not crew-peer model. `[NEED: confirm/expand from your competitive notes]`
- **TaskRabbit / Thumbtack:** Solve home services hiring but with zero context about the loved one.

**Why our approach wins:** Crew-peer model (no single "lead caregiver" required) + AI that does the actual coordination work + integrated services hiring with elder-context. No competitor combines all three.

## 4. Solution

A mobile-first app where a crew of family + friends collaboratively cares for a loved one aging in place. AI does three core jobs:

### Core Capabilities

**(a) AI Care Coordinator / Scheduler**
Crew members add availability, skills, and location. Loved one's needs are entered once (meds, meals, rides, check-ins, recurring tasks). AI proposes a weekly schedule that fairly distributes load, accounts for who lives closest, and re-balances when someone's plans change. Crew members claim, swap, or decline tasks — AI re-assigns gaps.

**(b) AI Crew Comms Summarizer**
The crew chat, doctor visit notes, and event log get summarized into a digestible "What you missed" feed for each crew member based on what's relevant to *them*. Catches up the cousin who checks in on Sundays without forcing them to scroll 200 messages.

**(c) AI Services Hiring Assistant**
When a home task comes up (lawn, gutters, broken dishwasher, snow removal), AI helps the crew find, vet, and book a local service provider. Knows the loved one's home, preferences, and budget. Tracks completion. Surfaces recurring needs proactively ("It's been 3 weeks since the lawn was mowed").

### Primary User Flow

```
1. Crew founder downloads app, creates loved one's profile (name, home, key needs)
2. Invites crew members via SMS/email — each sets availability + skills
3. AI generates Week 1 schedule → crew reviews, claims, edits
4. Crew chats inside app about loved one; AI summarizes per-person daily
5. Home task comes up (e.g., "fridge is making a noise")
   → AI suggests local repair pros, crew approves, AI books + tracks
6. Loved one's status visible to all (last check-in, upcoming visits, open tasks)
```

### Key States
- **Healthy crew:** all needs covered, balanced load, low alert volume
- **Gap detected:** unfilled task within 24h → AI nudges available crew members
- **Overload detected:** one crew member doing >40% of tasks → AI flags + suggests rebalance
- **Loved-one signal:** missed check-in, missed meds → escalation to nearest crew member

### AI Behavior Spec (15+ examples)

**Coordinator / Scheduler**

| # | Input | Expected Output |
|---|-------|-----------------|
| 1 | "Sarah cancels Tuesday 3pm pharmacy run" | Reassigns to next-closest available crew member; if none, posts to crew with 24h deadline |
| 2 | New crew member added with "weekends only, lives 2hrs away" | Assigns Saturday/Sunday tasks only; avoids weekday short-notice |
| 3 | Loved one's doctor adds new med "twice daily with food" | Creates recurring task; assigns to whoever already does meals; flags conflict if someone else owns meds |
| 4 | Crew member marks task "complete" 4 hours late | Logs delay silently; if pattern repeats 3x, surfaces gently to that member, not whole crew |
| 5 | Two tasks scheduled for same crew member 30 min apart, 45 min driving distance | Flags conflict; proposes swap with available member |
| 6 | Crew member with "no medical tasks" preference assigned med pickup | Rejects assignment; reassigns and explains why |
| 7 | Holiday week — 6 of 8 crew members marked unavailable | Surfaces crisis; suggests temporarily hiring a paid visit; does NOT silently overload remaining 2 |

**Crew Comms Summarizer**

| # | Input | Expected Output |
|---|-------|-----------------|
| 8 | 47 chat messages over 3 days, mostly about Mom's cardiology appt | "Mom saw Dr. Chen Tuesday. New BP med, follow-up in 6 weeks. Sarah has the prescription. No major concerns." |
| 9 | Single message: "Dad fell but he's okay" buried in chat about lawn care | Pulls fall to top of summary as priority; lawn care below |
| 10 | Two crew members debating whether to hire a cleaner | Summarizes positions; does NOT take a side; flags as "open decision" |
| 11 | Crew member asks AI "what did I miss this week?" | Personalized summary based on tasks they own + their relationship (e.g., medical updates for the sibling who's an RN) |
| 12 | Doctor visit note uploaded as photo | OCRs, summarizes, tags meds/follow-ups, asks crew to confirm before adding to schedule |
| 13 | Message contains medical jargon ("eGFR dropped to 45") | Summarizes in plain language with optional "what this means" expansion |

**Services Hiring**

| # | Input | Expected Output |
|---|-------|-----------------|
| 14 | "Lawn needs mowing, Dad's in Cleveland 44109" | 3 vetted providers with ratings, prices, availability; remembers preferred one for next time |
| 15 | "Gutters" booking after a previous lawn-care provider did good work | Asks if same provider does gutters; if yes, prefers them |
| 16 | Crew approves $400 dishwasher repair without budget set | Books it; logs cost; suggests setting a monthly budget so future approvals are faster |
| 17 | Loved one calls plumber directly, charges $800 | Logs the cost, doesn't double-book; flags to crew so they can follow up |
| 18 | Provider asks for keys / access to home | Routes to nearest crew member; never authorizes home access without human approval |
| 19 | Repeat seasonal task (snow removal) | Proactively suggests rebooking 1 week before first forecast snow |
| 20 | User asks AI to hire a "home health aide" | Rejects — out of scope for V1 (medical). Suggests crew add this manually or refer to licensed agency |

**Rejection / safety criteria (must hold across all capabilities):**
- Never makes medical decisions or interprets medical advice
- Never authorizes home entry without explicit crew approval
- Never books a paid service over `[NEED: budget threshold, e.g., $250]` without human approval
- Never shares loved one's location, health data, or schedule outside the crew
- If loved one is in distress signal (missed check-in, fall flag), escalates to humans within 60 seconds — does not attempt to handle alone

## 5. Non-Goals

- We are **NOT** providing licensed medical care, telehealth, or home health aide services in V1. We coordinate the humans who do.
- We are **NOT** building a companion chatbot for the loved one in V1. The elder is in the background; the crew is the user. (V2 candidate.)
- We are **NOT** integrating with hospital EHR systems in V1.
- We are **NOT** replacing emergency services. Fall detection / 911 is out of scope — we recommend separate medical alert devices.
- We are **NOT** charging the loved one. Pricing targets the crew (likely the lead coordinator's credit card).
- We are **NOT** building a marketplace of paid caregivers (that's Papa / Honor's space). We coordinate unpaid family + paid services for *home tasks*.

## 6. Success Metrics

| Metric | Type | Baseline | Target | Timeframe |
|--------|------|----------|--------|-----------|
| Active crews at 90 days post-signup | Primary | n/a (new product) | `[NEED: target]` | 90 days |
| % of loved ones still aging-in-place at 12 months | Primary | `[NEED: industry baseline from research]` | `[NEED: target lift]` | 12 months |
| Crew load balance (Gini coefficient of task distribution) | Secondary | n/a | <0.4 (reasonably even) | 90 days |
| Self-reported lead caregiver burnout score | Secondary | `[NEED: baseline from intake survey]` | -25% | 6 months |
| Services bookings per crew per month | Secondary | n/a | `[NEED: target]` | 90 days |

**Guardrails (must NOT get worse):**
- AI assignment rejection rate (crew member declines AI suggestion) <20%
- Summary accuracy (crew rates summary "got the important stuff" thumbs-up) >85%
- Zero incidents of unauthorized home access via services booking
- Zero incidents of AI making a medical decision or recommendation

## 7. Rollout Plan

- **Phase 1 — Closed beta (10 crews):** Hand-recruited from `[NEED: source — your interview pool?]`. Heavy support, weekly check-ins. Goal: prove crews stay active past day 30.
- **Phase 2 — Limited launch (100 crews):** Single geography for services hiring (suggest Cleveland or wherever your interview base is densest). Validate the AI coordinator quality.
- **Phase 3 — Public launch:** Open signups, expand services geography. Marketing focused on the "I'm the one doing everything" sibling.

**Go/no-go criteria to advance phases:**
- Phase 1 → 2: ≥7 of 10 crews still active at day 60, summary thumbs-up >75%
- Phase 2 → 3: Active crews at 90 days >`[NEED: target]`, zero safety guardrail violations

**Rollback plan:** AI features can be disabled per-crew via feature flag; app falls back to manual scheduling + chat. Services hiring can be paused without breaking the rest of the app.

## 8. Open Questions

- `[NEED: pricing model — freemium? per-crew subscription? services markup? — owner: Brent, deadline: TBD]`
- `[NEED: how does the loved one consent to being coordinated? Privacy + dignity question — owner: Brent + legal review]`
- `[NEED: what's the minimum viable crew size? Does this work for a crew of 2?]`
- `[NEED: how do we handle a crew member who goes rogue / abusive — moderation policy]`
- `[NEED: HIPAA posture — we're not a covered entity, but med info is sensitive. Privacy counsel review needed.]`
- `[NEED: services provider vetting — own marketplace, or partner with Thumbtack/Angi API?]`

---

## Stage 4 Checklist

- [x] Edge cases identified (in AI behavior spec)
- [x] Rollout plan determined (phased)
- [ ] Cross-functional requirements specified — **gap:** legal/privacy review, services partnerships, payment processing not yet detailed
- [ ] Tracking and analytics events defined — **gap:** specific event taxonomy missing
- [x] Risks and mitigations documented (guardrails + rejection criteria)

---

**Gaps to fill before this PRD is review-ready:**
1. Paste 3-5 caregiver quotes from your interviews (Section 2)
2. Paste market stats — caregiver burnout %, aging-in-place demand %, market size (Section 2)
3. Paste your competitor list with notes (Section 3)
4. Set targets for the metrics table (Section 6)
5. Resolve the 6 open questions in Section 8
