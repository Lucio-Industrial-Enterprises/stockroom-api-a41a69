# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a delivery quote
in USD.

| Parameter  | Type  | Values                        | Default      |
|------------|-------|-------------------------------|--------------|
| weight_kg  | float | positive number               | *(required)* |
| zone       | str   | `"local"`, `"regional"`       | *(required)* |
| service    | str   | `"standard"`, `"express"`     | `"standard"` |

Express shipping adds a **$7.00 surcharge** on top of the standard rate for
either zone. Unknown zones or services raise `ValueError`.

### Rate table

| Zone     | Standard base | Express base |
|----------|---------------|--------------|
| local    | $5.00         | $12.00       |
| regional | $8.00         | $15.00       |

Per-kg rate: **$1.50** (all zones and services).

### CLI usage

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

Examples:

```
# Standard quote – 2 kg, local
python -m warehouse.cli 2 local
# → $8.00

# Express quote – 2 kg, local
python -m warehouse.cli 2 local --service express
# → $15.00

# Express quote – 3 kg, regional
python -m warehouse.cli 3 regional --service express
# → $19.50
```
