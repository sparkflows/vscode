# Sparkflows Workflow JSON Schema

## Root Structure

```json
{
  "name": "string",
  "uuid": "uuid-v4",
  "category": "-",
  "nodes": [ ...node objects... ],
  "edges": [ ...edge objects... ],
  "dataSetDetails": [],
  "engine": "scala | pyspark | polars",
  "nodeDebugConfigs": {}
}
```

`category` defaults to `"-"` if unspecified. `dataSetDetails` is always `[]`. `nodeDebugConfigs` is always `{}`.

---

## Node Assembly

Inject each node's JSON file verbatim. Only set these two fields during assembly:

- `id` — unique sequential integer **as a string**: `"1"`, `"2"`, `"3"`
- `x` / `y` — canvas position as CSS strings: `"108px"`, `"121px"`

Increment X by ~140px per pipeline step. Increment Y by ~90px per parallel branch.

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
- Single column: `"value": "[\"customer_id\"]"`
- Multiple columns: `"value": "[\"col_a\",\"col_b\"]"`

Never convert a string value into a native JSON array, number, or boolean.

---

## Edge Structure

```json
{ "source": "1", "target": "2", "id": 1, "index": 0 }
```

| Field | Type | Notes |
|---|---|---|
| `source` / `target` | **string** | Must match a node `id` |
| `id` | **integer** | Not a string — `1` not `"1"` |
| `index` | integer | Always `0` |
| `targetAnchor` | string | Required when target node has named `inputAnchors` |
| `sourceAnchor` | string | Required when source node has named `outputAnchors` |

> Node `id` is a string. Edge `id` is an integer. This asymmetry is intentional.

When a node's `inputAnchors` or `outputAnchors` array contains named entries (e.g., `"Left"/"Right"` or `"First"/"Second"`), the connecting edge must include the matching `targetAnchor` or `sourceAnchor`. Check the node JSON file for anchor names.

---

## Assembly Checklist

- [ ] `uuid` is a freshly generated UUID v4
- [ ] Node `id` values are unique strings; edge `id` values are unique integers
- [ ] Every edge `source`/`target` matches a real node `id`
- [ ] Named anchors are included on edges where required
- [ ] Every non-terminal node has at least one outgoing edge
- [ ] `x`/`y` values include the `px` suffix