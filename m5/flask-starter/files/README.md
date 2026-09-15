# Minimal DataMan Flask Starter

Use this starter for the first real Flask/Codespaces implementation step in Module 5.

Files:
- `app.py` — Flask/interface coordination
- `business_logic.py` — reusable DataMan rule behavior
- `data_store.py` — deliberately simple state boundary
- `templates/index.html` — user-facing response
- `requirements.txt` — Flask dependency

Run in Codespaces from this folder:

```bash
python -m pip install -r requirements.txt
python -m flask --app app run --debug --host=0.0.0.0
```

Controlled test:
1. Submit a wrong answer once. Expected: `Try again.`
2. Submit a wrong answer a second time. Expected: correct answer revealed.
3. Restart the app to reset the in-memory state.
4. Make the controlled change named on the Canvas page.
5. Run the same behavior again and inspect what changed.

This starter is instructional scaffolding, not the final DataMan architecture. The in-memory store is intentionally temporary so you can see the data/state boundary before introducing a database.
