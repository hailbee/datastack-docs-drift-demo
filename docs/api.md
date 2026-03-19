# API Reference

## POST /users

Creates a user.

### Request body

| Field | Type | Required |
|---|---|---|
| name | string | yes |

### Example

```bash
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Jane Doe"}'