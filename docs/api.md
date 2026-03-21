# API Reference

## POST /users

Creates a user.

### Request body

| Field | Type | Required | Default |
|---|---|---|---|
| email | string (email) | yes | — |
| full_name | string | yes | — |
| plan | string | no | `"free"` |

### Example

```bash
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"email":"jane@example.com","full_name":"Jane Doe","plan":"free"}'
```

### Example response

```json
{
  "id": "usr_123",
  "email": "jane@example.com",
  "full_name": "Jane Doe",
  "plan": "free"
}
```

---

## GET /purchases/{purchase_id}

Retrieves a purchase by ID.

### Example

```bash
curl http://localhost:8000/purchases/pur_123
```

### Example response

```json
{
  "purchase_id": "pur_123",
  "status": "processed",
  "amount_cents": 2599,
  "currency": "USD"
}
```
