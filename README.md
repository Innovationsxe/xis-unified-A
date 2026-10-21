# XIS Unified — Updated Working MVP (v0.2.0)

A local demonstration build for XE 54 Intelligence Solutions' tender platform concept. It is a runnable starting point, not a production procurement system.

## Included features
- Tender discovery with keyword search.
- Sample tenders, clearly illustrative.
- Create and save business profiles.
- Agency demo form to publish a tender.
- Bidder demo form to submit a bid to an open tender.
- Agency review view for submitted bids.
- Rule-based keyword matching to suggest relevant tenders to saved business profiles. This is not a trained AI model and does not rank bidder quality.
- JSON data persistence under `data/`.

## Requirements
Python 3.10+; no third-party Python packages required.

## Run on Windows
1. Extract the ZIP folder.
2. Open the folder in File Explorer.
3. In the folder address bar, type `cmd` and press Enter.
4. Run `py server.py` (or `python server.py`).
5. Open `http://127.0.0.1:8000` in your browser.
6. Stop the server by returning to the terminal and pressing `Ctrl+C`.

## Run on macOS / Linux
```bash
python3 server.py
```
Then open `http://127.0.0.1:8000`.

## API quick reference
- `GET /api/health` — health check
- `GET /api/tenders` — list tenders
- `POST /api/tenders` — create tender
- `GET /api/profiles` — list business profiles
- `POST /api/profiles` — create business profile
- `GET /api/bids` — list bid submissions
- `POST /api/bids` — submit bid

POST endpoints accept JSON. See `docs/API.md` for examples.

## Data and limitations
The first run creates JSON data files and seeds three illustrative tenders. Data is stored locally without authentication or encryption. This MVP is for development/demo use only: do not enter real personal information, confidential bids, credentials, or live procurement information. It has no authentication, role permissions, secure document uploads, notifications, external tender feeds, audit log, legal compliance workflow, or production database. Do not deploy publicly as-is.

## Suggested next production steps
1. Confirm official tender data sources and permitted access.
2. Add authentication, role-based access control and verified agency accounts.
3. Move storage to PostgreSQL and add migrations/backups.
4. Add secure document uploads, malware scanning, versioning and audit logs.
5. Implement transparent configurable evaluation criteria; keep final decisions with authorised human evaluators.
6. Add privacy/security review, procurement-law review, tests, CI and deployment configuration.

## Repository
Target GitHub repository: https://github.com/Innovationsxe/xis-unified-A
This ZIP is a prepared local working package; it has not been pushed to GitHub.
