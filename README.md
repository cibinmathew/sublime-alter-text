# alter-text

Quickly alter text in Sublime Text.
- `replace_text_with`:  Replace selected text with equivalent number of a specified character(eg: space)
- `todo` Cycle between snake, title, pascal, camel and original
- `todo` Collapse whites in the order of to (no space if leading spaces, single line, to single space)


## How to Use

From Command palette, type `Alter Text: Replace with`

No default keybinding is provided. Use like below as necessary
```
[
    { "keys": ["ctrl+r"], "command": "replace_text_with", "args": { "replacement": " " } },
    { "keys": ["ctrl+-"], "command": "replace_text_with", "args": { "replacement": "-" } }
]
```
## How to Install

### Install with Package Control
To Install via [Package Control](https://packagecontrol.io/). 
- Search for package: `Alter Text`

### TODOs
- [x] Submit to package control channel
- [ ] Add multi cursor modifications
- [ ] Add FAQ

## FAQ
todo

### Motivation

### Contributors

<a href="https://github.com/cibinmathew/sublime-alter-text/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=cibinmathew/sublime-alter-text" />
</a>

### License

[MIT License](./LICENSE)
