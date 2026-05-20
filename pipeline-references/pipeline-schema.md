# Sparkflows Pipeline JSON Schema

## Root Structure

```json
{
  "name": "string",
  "uuid": "uuid-v4",
  "category": "-",
  "description": "-",
  "parameters": "--var key=value --var key2=value2",
  "nodes": [ ...node objects... ],
  "edges": [ ...edge objects... ]
}
```

`category` defaults to `"-"` if unspecified. `description` defaults to `"-"` if unspecified.
`parameters` holds DAG-level variables passed as a single string of `--var key=value` pairs; omit or use `""` if none.

---

## Node Assembly

Inject each node's JSON file verbatim. Only set these fields during assembly:

- `id` — unique sequential integer **as a string**: `"1"`, `"2"`, `"3"`
- `name` — the task label shown on the canvas (e.g. `"01-Ingest-Data"`)
- `x` / `y` — canvas position as CSS strings: `"108px"`, `"121px"`

Increment X by ~140px per pipeline step. Increment Y by ~90px per parallel branch.

Each node also carries these read-only fields copied verbatim from its JSON file:

| Field | Type | Description |
|---|---|---|
| `path` | string | Folder path of the node type, e.g. `"/08-Workflow/"` |
| `description` | string | One-line description of the node type |
| `details` | string | HTML long-form documentation |
| `examples` | string | HTML usage examples |
| `type` | string | Node type identifier, e.g. `"workflow"` |
| `nodeClass` | string | Java class, e.g. `"fire.pipelineNodes.Workflow"` |
| `fields` | array | Configuration fields (see below) |

---

## Field Value Format

Node `fields` entries store values as **strings**, even when the value represents an array
or number. This is intentional — Sparkflows parses these strings internally.

| Field content | Correct format | Wrong format |
|---|---|---|
| Empty array | `"value": "[]"` | `"value": []` |
| Populated array | `"value": "[\"col_a\",\"col_b\"]"` | `"value": ["col_a", "col_b"]` |
| Number | `"value": "20"` | `"value": 20` |
| Boolean | `"value": "true"` | `"value": true` |

When populating a user-specified value into an array field, serialize it as a JSON string:
- Single value: `"value": "[\"customer_id\"]"`
- Multiple values: `"value": "[\"col_a\",\"col_b\"]"`

Never convert a string value into a native JSON array, number, or boolean.

---

## Edge Structure

```json
{ "source": "1", "target": "2", "id": 1 }
```

| Field | Type | Notes |
|---|---|---|
| `source` / `target` | **string** | Must match a node `id` |
| `id` | **integer** | Not a string — `1` not `"1"` |

> Node `id` is a string. Edge `id` is an integer. This asymmetry is intentional.

---

## Assembly Checklist

- [ ] `uuid` is a freshly generated UUID v4
- [ ] Node `id` values are unique strings; edge `id` values are unique integers
- [ ] Every edge `source`/`target` matches a real node `id`
- [ ] Every non-terminal node has at least one outgoing edge
- [ ] `x`/`y` values include the `px` suffix
- [ ] `parameters` string uses `--var key=value` format for all DAG-level variables
