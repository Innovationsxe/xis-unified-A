# Manual smoke test plan

1. Start `python server.py`; open `http://127.0.0.1:8000`.
2. Confirm three sample tenders load and the counters show tender/profile/bid counts.
3. Search for `ICT`; confirm the computer equipment tender remains visible.
4. Create a business profile with category `ICT`; confirm success message and saved profile list.
5. Return to Discover; check that the matching profile may be suggested on the ICT tender.
6. Open Publish tender; create a tender with all required fields; confirm it appears in Discover.
7. Click Prepare bid on an open tender, fill all fields and submit; confirm a bid ID appears.
8. Open Agency review; confirm the submission is visible with tender name, business, price and proposal.
9. Stop and restart the server; confirm created records remain in `data/*.json`.
10. Try submitting an empty form; browser validation should stop submission.

## Known limitations
This is a manual smoke test plan, not evidence of a full automated test suite or security audit.
