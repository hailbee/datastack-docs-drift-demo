# Curl Examples

## Create user

```bash
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"email":"jane@example.com","full_name":"Jane Doe","plan":"free"}'
```

## Get purchase

```bash
curl http://localhost:8000/purchases/pur_456
```
