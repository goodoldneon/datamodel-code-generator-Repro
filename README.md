# `datamodel-code-generator` Repro

Repro of the `pydantic`-to-JSON marshalling limitation.

## Desired behavior

Given the following OpenAPI schema (found in `openapi.yaml`):

```yaml
Foo:
  type: object
  properties:
    required:
      type: integer
    required_default:
      type: integer
      default: 2
    required_nullable:
      type: integer
      nullable: true
    unrequired:
      type: integer
  required:
    - required
    - required_default
    - required_nullable
```

I would expect the following assertion pass (possibly with args passed to `foo.dict()`):

```py
foo = Foo(required=1, required_nullable=None)

assert foo.dict() == {
    "required": 1,
    "required_default": 1,
    "required_nullable": None,
}
```

## Usage

`models.py` was generated using `datamodel-codegen --input openapi.yaml --output models.py --strict-nullable --use-default`.
