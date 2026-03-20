# DataStack Docs Drift Demo

This repository demonstrates a documentation drift automation workflow powered by Devin.

In many engineering teams, API implementations evolve over time while documentation falls behind. This project simulates that situation and shows how an automated workflow can detect documentation drift and assign a remediation task to Devin.

## API Overview

### Create User

Endpoint: `POST /users`

Request body:

```json
{
  "name": "Jane Doe"
}
```

Example response:

```json
{
  "id": "usr_123",
  "name": "Jane Doe"
}
```

---

### Get Order

Endpoint: `GET /orders/{order_id}`

Example request:

```bash
curl http://localhost:8000/orders/ord_123
```

Example response:

```json
{
  "order_id": "ord_123",
  "status": "paid"
}
```

---

## Note

The documentation in this repository intentionally contains outdated API examples to simulate documentation drift. The FastAPI implementation in `app/main.py` contains the current truth.

The goal of this demo is to detect these mismatches and use Devin to automatically propose documentation updates via a pull request.
