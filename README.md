# Architecture of Personality 0.3.1

Open-source pilot application for architectural interviews (MIT license).

## Features
- 27 Bulgarian questions, exactly 5 predefined answers each, across 9 sections.
- Separate resident profiles and comparison of conflicting answers.
- Rule-based preliminary architectural findings, with evidence question IDs.
- Optional OpenAI cloud analysis; PDF via browser Print, JSON export.
- Local browser persistence via `localStorage` (not synced across devices).

## Local launch
Install Python 3.10+ and run:

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Open http://127.0.0.1:8000

## Publish online (Render)
1. Create a GitHub repository and upload these files to the repository root.
2. In Render choose **New > Blueprint**, connect the repository and apply `render.yaml`.
3. Configure `OPENAI_API_KEY` in Render environment variables if AI analysis is desired. **Never commit a secret key.**
4. Wait for deployment, then open the URL Render assigns to the service.

**Deployment is not performed by this package.** Hosting may require account setup and may have usage limits or charges. API usage is billed separately.

## Privacy / production readiness
This is a public demonstration prototype, NOT a production system for confidential resident data. Responses remain in browser storage until analysis, when they are sent to the server. AI mode additionally sends analysis context to the configured AI provider. Do not enter sensitive personal information. No authentication, server-side storage, access controls, consent management, abuse controls, rate limiting or production security review is included. Add these before public use with real participants.

The generated findings are design hypotheses, not psychological diagnosis or an architectural approval.

## v0.3.1 changes
- Project brief with six optional fields and missing-data warnings.
- Grounded AI prompt with exact question texts, separate facts, needs and hypotheses.
- No changes to public URL after updating GitHub; Render auto-deploys.
- Demo only: no authentication or secure storage for real client data.

## v0.3.1
- Versioned local storage and automatic removal of only invalid legacy answers (other answers preserved).
- Server validation errors shown to the user instead of a generic connection error.
- Larger AI response limit and stricter source-grounding instructions.
- Improved PDF print pagination.
