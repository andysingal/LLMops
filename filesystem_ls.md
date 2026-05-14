[elasticsearch-fs](https://github.com/iamleonie/elasticsearch-fs)

"Virtual filesystem" means two different things depending on who you ask.

In operating systems: a layer that lets every program use the same open, read, write calls whether it's reading from an SSD, a USB stick, or a network share.

In AI agents: a filesystem-shaped interface on top of persistent storage, so the agent can run ls, cat, find, and grep over a database.

Same name. Different job.

This lets the agent use ls, cat, find, and grep over the stored data. The agent running, for example, grep -r "access_token" /docs is searching a [filesystem](https://leoniemonigatti.com/blog/virtual-filesystem-elasticsearch.html) and doesn’t know it’s interacting with a search index. Thus, commands like grep become an interface, the implementation of which can make use of powerful search features, such as vector search or hybrid search.




