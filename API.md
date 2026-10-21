# API notes
Base URL: `http://127.0.0.1:8000/api`

## Create a tender
`POST /tenders`
```json
{"title":"Supply of laptops","agency":"Example Agency","category":"ICT","description":"Supply laptops with warranty","closing_date":"2027-03-31","location":"KwaZulu-Natal"}
```
Required fields: `title`, `agency`, `category`, `description`, `closing_date`.

## Create a business profile
`POST /profiles`
```json
{"business_name":"Example Solutions","contact_name":"Demo Contact","email":"demo@example.com","categories":"ICT, training","description":"Provides IT support and training"}
```
Required fields: all five shown above.

## Submit a bid
`POST /bids`
```json
{"tender_id":"TND-001","business_name":"Example Solutions","contact_email":"demo@example.com","proposal":"We can deliver the listed equipment and warranty support.","price":"ZAR 125000"}
```
Required fields: all five shown above. Tender must exist and have status `Open`.

## Data files
JSON arrays are stored in `data/tenders.json`, `data/profiles.json`, and `data/bids.json`. Back up the folder before editing/deleting those files. This demo has no concurrent-write locking or production-grade validation.
