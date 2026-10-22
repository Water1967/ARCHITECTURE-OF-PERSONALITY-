# Architecture of Personality 0.4

Open-source architectural interview prototype. Bulgarian UI, 27 questions with five options, separate resident profiles, optional OpenAI analysis, project brief, and **deterministic functional programming**.

## New in 0.4
- Functional room/zone schedule with illustrative area ranges and question evidence.
- Adjacency/separation matrix and a schematic SVG relationship diagram.
- Target-area plausibility warnings and explicit missing-data notes.
- Distinguishes registered residents from residents with any answers.
- No CAD plan, no regulatory verification, no validated psychological assessment.

## Run
`pip install -r requirements.txt`
`uvicorn app:app --reload`

## Deploy
Upload repository-root files to existing GitHub repo. Render Blueprint auto-deploys using existing `render.yaml`. Keep `OPENAI_API_KEY` only in Render environment variables.

## Privacy
Public demo only. Responses are saved in browser localStorage, and sent to the server when analyzing; AI mode additionally sends context to the configured provider. Do not enter confidential personal data. No authentication, consent management, access controls or production security audit.

MIT license.
