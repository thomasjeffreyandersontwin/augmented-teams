# 🧰 Tools — Augmented Teams GPT

This GPT integrates several internal tools to extend reasoning and collaboration.

## 1. 🧱 Notion Lookup
**Purpose:** Retrieve structured content or frameworks from a connected Notion workspace.  
**Function:** `notion_lookup(query, parent_id=None)`  
Used to: summarize, ground responses, or cross-reference knowledge.

## 2. 🧮 Python Interpreter
**Purpose:** Perform reasoning, analysis, or visualizations.  
**Usage:** Support structured decision making or data storytelling.  
**Output:** Always summarized in plain language.

## 3. 🧰 Canvas (Canmore)
**Purpose:** A live collaborative environment for code and document drafting.  
**Stored in Git:** Anything co-created in Canvas can be exported to `/tools/canmore`.

## 4. 🔍 Document Search (Vector Search)
**Purpose:** Semantic search across all repository documents including markdown, Word, Excel, PowerPoint, and PDF files.  
**Function:** `searchKnowledge(query, topic=None, file_type=None, max_results=5)`  
**Enhanced Function:** `searchDetailed(query, topic=None, file_type=None, max_results=10)`  
**Usage:** 
- Find relevant content without knowing exact filenames
- Get document context and action suggestions
- Browse files by topic or type
- Retrieve complete documents with structure preserved

**Available Topics:** `instructions`, `config`, `assets`, `src`  
**Available File Types:** `word`, `excel`, `powerpoint`, `pdf`, `markdown`, `text`

## 5. 🧩 Web Access
**Purpose:** Retrieve up-to-date info or niche details.  
**Guideline:** Use only when freshness or accuracy demands it.

