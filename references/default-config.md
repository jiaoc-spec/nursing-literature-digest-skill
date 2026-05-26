# Default Nursing Literature Digest Configuration

Use these defaults when the user asks for a starter daily nursing literature digest.

## Schedule And Delivery

- Frequency: daily
- Time: `09:00`
- Timezone: ask the user; if unclear, use the user's local timezone.
- Recipient: ask the user.
- Email connector: Gmail when connected.
- Local archive:
  - `nursing-literature-digests/YYYY-MM-DD.md`
  - `nursing-literature-digests/YYYY-MM-DD.docx` only when requested
  - `nursing-literature-digests/fulltext-inbox/to-download-YYYY-MM-DD.md`
  - `nursing-literature-digests/fulltext-summaries/`
  - `nursing-literature-digests/data/YYYY-MM-DDTHHMMSSZ.json`
  - `nursing-literature-digests/state.json`

## Default Config Shape

```json
{
  "recipient_email": "user@example.com",
  "crossref_mailto": "user@example.com",
  "ncbi_email": "user@example.com",
  "language": "zh-CN",
  "timezone": "Europe/Berlin",
  "schedule_time": "09:00",
  "output_dir": "nursing-literature-digests",
  "include_pubmed": true,
  "include_arxiv": true,
  "rows": 20,
  "arxiv_rows": 25,
  "pubmed_rows": 30,
  "max_papers": 40,
  "keyword_groups": [
    {
      "label": "psychiatric nursing",
      "terms": [
        "psychiatric nursing",
        "mental health nursing",
        "psychiatric-mental health nursing",
        "inpatient psychiatric nursing",
        "community mental health nursing"
      ]
    },
    {
      "label": "therapeutic relationship / communication",
      "terms": [
        "therapeutic relationship",
        "therapeutic communication",
        "therapeutic alliance",
        "nurse-patient relationship",
        "milieu therapy"
      ]
    },
    {
      "label": "borderline personality disorder",
      "terms": [
        "borderline personality disorder",
        "emotionally unstable personality disorder",
        "personality disorder nursing",
        "BPD nursing care"
      ]
    },
    {
      "label": "dialectical behavior therapy",
      "terms": [
        "dialectical behavior therapy",
        "dialectical behaviour therapy",
        "DBT skills training",
        "DBT nursing",
        "DBT psychiatric"
      ]
    },
    {
      "label": "schizophrenia / psychosis nursing",
      "terms": [
        "schizophrenia nursing",
        "psychosis nursing care",
        "first-episode psychosis",
        "early psychosis intervention",
        "antipsychotic nursing"
      ]
    },
    {
      "label": "bipolar disorder nursing",
      "terms": [
        "bipolar disorder nursing",
        "bipolar disorder care",
        "mania nursing",
        "mood stabilizer nursing"
      ]
    },
    {
      "label": "psychiatric crisis / emergency",
      "terms": [
        "psychiatric crisis intervention",
        "mental health crisis nursing",
        "psychiatric emergency nursing",
        "suicide prevention nursing",
        "self-harm nursing",
        "aggression management psychiatric"
      ]
    },
    {
      "label": "trauma-informed care",
      "terms": [
        "trauma-informed care",
        "trauma-informed nursing",
        "PTSD nursing",
        "complex PTSD care",
        "adverse childhood experiences nursing"
      ]
    },
    {
      "label": "forensic psychiatric nursing",
      "terms": [
        "forensic psychiatric nursing",
        "forensic mental health nursing",
        "compulsory psychiatric treatment",
        "involuntary hospitalization nursing",
        "secure psychiatric unit"
      ]
    },
    {
      "label": "psychopharmacology nursing",
      "terms": [
        "psychopharmacology nursing",
        "psychiatric medication management",
        "clozapine nursing",
        "medication adherence psychiatric",
        "antidepressant nursing"
      ]
    }
  ]
}
```

## Default Sources

- **PubMed/MEDLINE** (primary): via NCBI E-utilities `esearch` + `efetch`. Covers all major nursing and psychiatric nursing journals. Includes MeSH terms and structured abstracts.
- **Elsevier** through Crossref member `78`; uses Crossref created-date because some records have future issue dates.
- **Springer Nature** through Crossref member `297`.
- **Wiley** through Crossref member `311`.
- **Taylor & Francis / Routledge** through Crossref member `301`.
- **arXiv** through `https://export.arxiv.org/api/query` — covers nursing informatics, health AI, and eHealth preprints.
- **OpenAlex** enrichment by DOI when available.

arXiv results must be labeled as preprints.

## Key Psychiatric Nursing Journals (covered by default sources)

- Journal of Psychiatric and Mental Health Nursing (Wiley)
- International Journal of Mental Health Nursing (Wiley)
- Archives of Psychiatric Nursing (Elsevier)
- Issues in Mental Health Nursing (Taylor & Francis)
- Perspectives in Psychiatric Care (Wiley)
- Journal of Psychosocial Nursing and Mental Health Services (Taylor & Francis)
- Psychiatric Services (APA — via PubMed)
- Journal of the American Psychiatric Nurses Association (Sage — via PubMed)
- Administration and Policy in Mental Health (Springer Nature)
- International Journal of Nursing Studies (Elsevier)

## Interpretation Rules

- Summarize from title, abstract, MeSH terms, keywords, subjects, and metadata only.
- If the abstract is unavailable, include the paper as a title-only candidate when the title or query term matches the user's keywords.
- Clearly state that no abstract/full text was read for title-only candidates.
- Do not infer goal, method, or result without an abstract or explicit full text.
- Create a separate follow-up list for title-only candidates. The user logs in themselves; Codex can then process that explicit batch using the active session or local PDFs.
- Do not auto-login to PubMed Central, hospital library systems, or publisher websites.
- Note when a paper is a systematic review or meta-analysis — these carry higher evidence weight in nursing practice.
