spruce
---

A no-nonsense static site generator written in Python.

What spruce enforces:

- Simple, markdown-powered webpages. YAML front-matter is supported for reasons that will be clear later.

What spruce does not enforce:

- The usage of themes. BYOCSS.
- Date-dependent posts. If you want to keep things chronological, you can. But you don't need to if you don't want to!

## Design

- `assets/`: images, CSS, you name it
- `config.toml`: Metadata about the site
<!-- - `nav/`: Top-level files (and directories) defined here will get added to --> 
