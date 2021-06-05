from models import Foo

foo = Foo(required=1, required_nullable=None)

assert foo.dict() == {
    "required": 1,
    "required_default": 2,
    "required_nullable": None,
    "unrequired": None,
}

assert foo.dict(exclude_unset=True) == {
    "required": 1,
    "required_nullable": None,
}

# I need something that will return:
# {
#    "required": 1,
#    "required_default": 2,
#    "required_nullable": None,
# }
