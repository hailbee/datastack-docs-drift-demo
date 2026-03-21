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
