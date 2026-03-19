# DataStack Docs Drift Demo

This repo demonstrates a docs-drift workflow powered by Devin.

## API Overview

### Create user

Endpoint: `POST /users`

Request body:

```json
{
  "email": "jane@example.com",
  "full_name": "Jane Doe",
  "plan": "free"
}
```

Response:

```json
{
  "id": "usr_123",
  "email": "jane@example.com",
  "full_name": "Jane Doe",
  "plan": "free"
}
```

### Get purchase

Endpoint: `GET /purchases/{purchase_id}`

Response:

```json
{
  "purchase_id": "pur_456",
  "status": "processed",
  "amount_cents": 2599,
  "currency": "USD"
}
```
