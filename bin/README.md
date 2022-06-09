# For development
## How to update parser

1. Edit [`lib/parser_definition`](./lib/parser_definition) as you expect
2. Perform the following command (you need to install [`getoptions`](https://github.com/ko1nksm/getoptions#installation) and [`gengetoptions`](https://github.com/ko1nksm/getoptions#installation))

```shell
gengetoptions parser -f lib/parser_definition parser_definition parse prog > lib/parser
```
