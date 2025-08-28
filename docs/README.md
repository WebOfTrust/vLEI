# vLEI Credential Documentaion

## Quick Start

1. **Local Development:**

From `./docs`

   ```bash
   python3 -m http.server 8000
   ```

Visit: <http://localhost:8000>

2. **Content Changes:**
   - Edit `.md` files in the `content/` directory
   - Refresh browser to see changes

## Content Management

### Adding New Pages

1. **Create content file:** Add `new-page.md` to `content/` directory
2. **Register file:** Add `'new-page'` to the `knownFiles` array in `app.js`
3. **Add navigation:** Update navbar in `index.html` if needed

### Internal Links

- **Page:** `[New Page](new-page)`

### Mermaid Diagrams

```content
\`\`\`mermaid
graph TD
    A[Start] --> B[End]
\`\`\`
```
