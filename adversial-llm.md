[GateKeep-RAG](https://github.com/saturn-16/GateKeep-RAG)

GateKeep RAG is an enterprise-grade, permission-aware multi-tenant Retrieval-Augmented Generation (RAG) platform built with FastAPI, PostgreSQL + Alembic, Qdrant vector database, local sentence-transformer embeddings, and local/remote LLM support (MockLLM / Ollama llama3.2:3b).

Every document chunk carries tenant ownership and role/clearance access control lists (ACLs). Search is pre-filtered directly inside Qdrant before vector similarity search, post-verified against PostgreSQL before prompt compilation, and cryptographically recorded in an append-only, hash-chained audit ledger.


- Pre-Filtering in Vector DB (Qdrant): Every document chunk is indexed with metadata tags for tenant_id, required roles, and clearance_level. During vector search, we construct payload filters (must clauses in Qdrant) bound to the authenticated caller's identity. Search happens only over authorized chunks.

- Relational Defense-in-Depth (PostgreSQL): Vector stores aren't ACID source-of-truth authorization engines. Even if a vector index is corrupted or a filter misconfigured, candidate chunks are re-checked against active relational permissions (can_access) in PostgreSQL before the prompt is assembled. If a mismatch occurs, it halts and logs a security alert.

- Tamper-Evident Audit Ledger: Every query records who asked, what chunks were retrieved, and what was returned. Rows are signed with an append-only SHA-256 cryptographic hash chain per tenant using PostgreSQL advisory locks (pg_advisory_xact_lock). If an attacker or compromised service modifies or drops a past log, the chain breaks immediately (verified via an audit verification endpoint).

- No-Results Parity: When an unauthorized user asks for restricted data, the system returns the exact same refusal shape and HTTP status as a standard "zero semantic matches" query to minimize enumeration side channels.

[source_1](https://www.reddit.com/r/LLMDevs/comments/1wznf37/why_prompt_guardrails_fail_at_multitenant_rag_and/)
