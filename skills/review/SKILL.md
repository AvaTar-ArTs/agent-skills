---
name: review
# v1 description (preserved 2026-10-03):
#   Review code changes with the Bugbot or Security Review subagent.
# v1: description: Dispatcher: asks whether you want Bugbot or Security Review, then routes to review-bugbot or review-security.
description: "Dispatcher: asks whether you want Bugbot or Security Review, then routes to review-bugbot or review-security."
disable-model-invocation: true
---
# Review

Ask the user which review to run with the AskQuestion tool. If the AskQuestion tool is not available, ask the user directly. Provide exactly one single-select question with two options:

- `bugbot`: Bugbot (`/review-bugbot`)
- `security`: Security Review (`/review-security`)

After the user chooses, run the matching review once:

- Bugbot: follow the `/review-bugbot` instructions.
- Security Review: follow the `/review-security` instructions.
