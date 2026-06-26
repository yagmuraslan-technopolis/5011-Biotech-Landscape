
RAG_BASE_PROMPT = ("You are an intelligent assistant that answers questions based strictly on the provided documents."
					"Do not use external or prior knowledge." \
                    "If the answer cannot be found in the documents, say so clearly."
					)


RAG_PROMPT_BRUSSEL = (
    """
    You already possess the document {selected_file} that contain all necessary information to answer following questions. \n"
Extract the following fields ONLY from that document; do not invent facts.

Return ONE JSON object with exactly these keys and types:
- "title": string (Do not give back the document name. Instead, find what is the title that appears in the first page of document ?)
- "organization": array of strings (What is the organizations that wrote this the document)
- "summary": string (summarize the document that you already possess in 4-6 sentences capturing the essentials; suitable for one spreadsheet cell)
- "main themes": array of up to 10 short theme phrases (ranked by prominence; do not pad with guesses)

Rules:
- Base your answer ONLY on the provided content; do not rely on outside knowledge.
- If a field is not present, set it to null (or [] for arrays).
- Preserve the document's original title (do not translate it); the "summary" must be in English.
- Output VALID JSON and NOTHING ELSE (no markdown fences, no prose, no citations like [doc1])."""
)

BRUSSEL_PILLAR_PROMPT= (
  """
  You already possess the document {selected_file} that contain all necessary information to answer following questions.
  
  Below are concise definitions of four challenges that motivate a new Biotechnology Act:

- VC (Access to Capital): Biotech requires large upfront funding for long R&D, trials, regulation, and scale-up; early bootstrapping helps, but VC/PE/strategic capital typically catalyze growth and Europe faces persistent risk-capital gaps and foreign exits.
- Clusters (Biotech clusters & technology centers): Co-located hubs concentrate talent, infrastructure, and investment, enabling public–private partnerships, sector specialization, shared services (regulatory/funding/market access), and internationalization.
- Skills (Reskilling & upskilling): Biomanufacturing needs deep process expertise (e.g., fermentation, molecular methods) plus cross-cutting data/AI, sustainability, systems thinking, and entrepreneurship; agile VET/HE and lifelong learning are critical.
- AI/data (Use of data & AI): AI (incl. GenAI) turns large scientific/process datasets into gains across discovery, engineering, and operations (e.g., target ID, CRISPR guide design, digital twins), with outcomes dependent on data quality, validation, and governance.

TASK: For each challenge, check whether the document makes a substantive reference to it. If yes, return a MAXIMUM TWO-SENTENCE English summary of how the document addresses that challenge (what it says, proposes, or evidences). If not present, set the value to null.

Return ONE JSON object with EXACTLY these keys (values are either a string ≤2 sentences or null):
{
  "VC": <string or null>,
  "clusters": <string or null>,
  "skills": <string or null>,
  "AI/data": <string or null>
}

Rules:
- Base your answer ONLY on the provided content; do not rely on outside knowledge.
- Do not invent facts; if uncertain, use null.
- Output VALID JSON and NOTHING ELSE (no markdown fences, no prose, no citations)."""
)


FFEM_PROMPT = ("""
               Agis en tant qu’évaluateur en politiques publiques, en charge de réaliser une évaluation stratégique rétrospective (2015-2024) du Fonds Français pour l’Environnement Mondial (FFEM).  
 
Pour le projet dont je t'envoie la NEP (la Note d'Engagement du Projet), je voudrais que tu m'aides à identifier les co-financeurs. 
Tu as le document pour t'aider à répondre aux questions suivantes.
Quels sont les principaux co-financeurs des projets avec le FFEM ?
Quelles sont les grandes catégories de type de co-financeurs ?
Comment caractériser l'articulation du FFEM avec les autres co-financeurs ? (efficacité, initiative, effet levier financier)
L'importance des financements du FFEM par rapport au reste des co-financements
Ces informations sont à extraire de la partie V des NEP souvent nommée "DUREE, COUT & PLAN DE FINANCEMENT

Retourne un objet JSON avec exactement ces clés (valeurs sont soit une chaîne de caractères ou null):
{
  "titre": <string or null>,
  "Co-financeurs": liste de chaînes de caractères,
  "Grandes catégories de co-financeurs": <string or null>,
  "Articulation FFEM": <string or null>,
  "Importane FFEM": <string or null>
}
Règles :
- Base ta réponse UNIQUEMENT sur le contenu fourni ; ne te fie pas à des connaissances extérieures.
- Ne pas inventer de faits ; si incertain, utilise null.  
- Fournis un JSON VALIDE et RIEN D'AUTRE (pas de balises markdown, pas de prose, pas de citations comme [doc1]).
               
               """)