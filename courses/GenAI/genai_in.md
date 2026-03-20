# GenAI a Python

![Python](images/python.png)

Pavel Tišnovský,
tisnik@centrum.cz

---

## Obsah

* Frameworky pro GenAI
* Vlastnosti LLM
* OpenAI a další standardizovaná API
* Framework Llama Stack
* Langchain pro tvorbu aplikací využívajících GenAI
* RAG (Retrieval-augmented generation)
    - Tokenizace textu, tvorba embedded modelů
    - Vyhledávání založené na podobnosti vektorů
    - PgVector
    - FAISS

---

## Frameworky pro GenAI

* langchain
* langgraph
* autogen
* metaGPT
* phidata
* CrewAI
* pydanticAI
* controlflow
* langflow
* LiteLLM (???)
* Llama Stack

---

## Potřebujeme sofistikované frameworky?

@ list_models.py

---

```text
gpt-4
gpt-3.5-turbo
gpt-audio-1.5
gpt-audio-mini-2025-12-15
chatgpt-image-latest
gpt-5.2-codex
gpt-realtime-1.5
davinci-002
babbage-002
gpt-3.5-turbo-instruct
gpt-3.5-turbo-instruct-0914
dall-e-3
dall-e-2
gpt-3.5-turbo-1106
tts-1-hd
tts-1-1106
tts-1-hd-1106
text-embedding-3-small
text-embedding-3-large
gpt-4-turbo-preview
gpt-3.5-turbo-0125
gpt-4-turbo
gpt-4o
gpt-4o-2024-05-13
gpt-4o-mini-2024-07-18
gpt-4o-mini
gpt-4o-2024-08-06
gpt-4o-audio-preview
gpt-4o-realtime-preview
omni-moderation-latest
omni-moderation-2024-09-26
gpt-4o-realtime-preview-2024-12-17
gpt-4o-audio-preview-2024-12-17
gpt-4o-mini-realtime-preview-2024-12-17
gpt-4o-mini-audio-preview-2024-12-17
gpt-4o-mini-realtime-preview
gpt-4o-mini-audio-preview
computer-use-preview
o3-mini
o3-mini-2025-01-31
gpt-4o-2024-11-20
computer-use-preview-2025-03-11
gpt-4o-search-preview-2025-03-11
gpt-4o-search-preview
gpt-4o-mini-search-preview-2025-03-11
gpt-4o-mini-search-preview
gpt-4o-transcribe
gpt-4o-mini-transcribe
gpt-4o-mini-tts
o3-2025-04-16
o4-mini-2025-04-16
o3
o4-mini
gpt-4.1-2025-04-14
gpt-4.1
gpt-4.1-mini-2025-04-14
gpt-4.1-mini
gpt-4.1-nano-2025-04-14
gpt-4.1-nano
gpt-image-1
gpt-4o-realtime-preview-2025-06-03
gpt-4o-audio-preview-2025-06-03
o3-pro-2025-06-10
o4-mini-deep-research
gpt-4o-transcribe-diarize
o4-mini-deep-research-2025-06-26
gpt-5-chat-latest
gpt-5-2025-08-07
gpt-5
gpt-5-mini-2025-08-07
gpt-5-mini
gpt-5-nano-2025-08-07
gpt-5-nano
gpt-audio-2025-08-28
gpt-realtime
gpt-realtime-2025-08-28
gpt-audio
gpt-5-codex
gpt-image-1-mini
gpt-audio-mini
gpt-audio-mini-2025-10-06
gpt-5-search-api
gpt-realtime-mini
gpt-realtime-mini-2025-10-06
sora-2
sora-2-pro
gpt-5-search-api-2025-10-14
gpt-5.1-chat-latest
gpt-5.1-2025-11-13
gpt-5.1
gpt-5.1-codex
gpt-5.1-codex-mini
gpt-5.1-codex-max
gpt-image-1.5
gpt-5.2-2025-12-11
gpt-5.2
gpt-5.2-pro-2025-12-11
gpt-5.2-chat-latest
gpt-4o-mini-transcribe-2025-12-15
gpt-4o-mini-transcribe-2025-03-20
gpt-4o-mini-tts-2025-03-20
gpt-4o-mini-tts-2025-12-15
gpt-realtime-mini-2025-12-15
gpt-3.5-turbo-16k
tts-1
whisper-1
text-embedding-ada-002
```

---

## Potřebujeme sofistikované frameworky?

* Kvóty
* Konverzace
* Kontext
* Guardrails
* RAG
* BYOK
* MCP
* Agenti
* A2A

---

## Llama Stack

![Llama Stack logo](images/llama_stack_logo.png)

---

## Co je to Llama Stack?

* Framework pro tvorbu aplikací s AI
    - chat boti
    - obecně generativní AI (GenAI)
    - trénink, evaluace
* Skutečný framework nezávislý na programovacím jazyku
    - systém providerů
    - RAG, správa kvóty, guardrails, metriky atd.

---

### Nejjednodušší využití Llama Stacku

* Volání LLM
* Zpracování odpovědi od LLM
* "chatbot v.0.0.1"

---

### Skutečné požadavky jsou však širší

* Podpora RAG
* Historie konverzace
* Rozvětvení konverzace
* Zapamatování fakt o uživateli
* Volání MCP
* Kvóty
* Kontrola dotazů a odpovědí
* Volání více LLM, evaluace odpovědí atd.

---

### API a poskytovatelé

* Plně konfigurovatelné
* Lze získat seznam dostupných API
* Taktéž lze získat seznam dostupných poskytovatelů
* Pozor: závislosti vyžadované jednotlivými poskytovateli

---

![Providers](images/llama_stack_providers.png)

---

### Poskytovatelé (providers)

<table>
<tr><th>Označení</th><th>Stručný popis</th></tr>
<tr><td>Agents</td><td>interakce se systémem agentů (samotní agenti mohou provádět různé operace)</td></tr>
<tr><td>Inference</td><td>rozhraní k&nbsp;LLM modelům i k&nbsp;embedding modelům</td></tr>
<tr><td>VectorIO</td><td>původně rozhraní k&nbsp;vektorovým databázím (hledání podobných vektorů), nyní i fulltext hledání</td></tr>
</table>

---

### Poskytovatelé (providers)

<table>
<tr><td>Safety</td><td>detekce dotazů s&nbsp;nevhodným či nepovoleným obsahem apod.</td></tr>
<tr><td>Telemetry</td><td>telemetrie (OpenTelemetry ale i další)</td></tr>
<tr><td>Eval</td><td>vyhodnocování odpovědí modelů atd.</td></tr>
<tr><td>DatasetIO</td><td>čtení a zápisy datových sad z/do zvoleného systému (může být i lokální souborový systém)</td></tr>
</table>

---

### Komunikace s Llama Stackem

* CLI
* REST API
* Jako běžná knihovna (Python atd.)
* Llama Stack klient
    - podporuje REST API
    - podporuje i běh formou knihovny (async)

---

### Llama Stack klient

* Python
* Swift
* Kotlin
* Node.js

---

### Llama Stack jako knihovna

![LS1](images/llama_stack_as_library.svg)

---

### Llama Stack jako samostatná služba

![LS1](images/llama_stack_as_service.svg)

---

### Běh v kontejneru

![LS1](images/llama_stack_in_container.svg)

---

### Příklad služby postavené na Llama Stacku

* REST API postavené nad API Llama Stacku
* Obě možnosti spuštění Llama Stacku
* Implementace formou asynchronního kódu (Python)

---

![LS1](images/llama_stack_arch.svg)

---

### Llama Stack klient

* Využijeme klienta pro Python

```bash
uv init
uv add llama-stack-client
```

---

### Llama Stack běží jako samostatná služba

@ llama_stack_service.py

---

### Llama Stack je použit jako běžná knihovna

@ llama_stack_library.py

---

### Komunikace s LLM

@ llama_stack_llm_call.py

---

### Získávání informací z poskytnutých dokumentů

* RAG
* Ovšem i další vstupy
    - sémantické vyhledávání
    - fulltext vyhledávání
    - hybridní vyhledávání

---

### Prvotní zpracování dokumentů

@ llama_stack_doc_1.py

---

### Prvotní zpracování dokumentů

@ llama_stack_doc_2.py

---

### Získání odpovědi z dokumentu

@ llama_stack_doc_3.py

---

### Ukázka 1/2

* Dokument:
    - `README.TXT` ze hry Supaplex
* Relevantní část z dokumentu:

```plaintext
[a round rock] - ZONK
       This is another very common obstacle (and usually a very
       unpleasant one) a Zonk tends to fall down whenever possible
       (i.e. there is a void underneath). Be careful, when a Zonk
       falls on you (Murphy) you will explode (read: die). Murphy can
       push Zonks to the side (not up and down) if nothing is blocking
       the Zonk (i.e. there is a void on the other side). Murphy can
       only push one Zonk at a time, so watch out when dropping Zonks
       next to each other! With some good timing, you can also drop
       Zonks on Electrons (see below) or Snik-snaks (see below) which
       will explode (and not bother you again). Zonks have the nasty
       habit of falling SIDEWAYS off Ram-Chips (see below) and other
       Zonks if possible (i.e. there is a void to the side), on all
       other objects the Zonks will lie steady.
```

---

### Ukázka 1/2
* Dotaz:
```plaintext
What is Zonk?
```
* Odpověď:
```plaintext
"ZONK" refers to an element in the videogame Supaplex. In the
game, a Zonk is depicted as a round rock, and it is a common and typically
unpleasant obstacle. Zonks tend to fall downwards whenever possible, for
instance, if there is a void directly underneath them. Players must be cautious
as a Zonk falling on the character (Murphy) results in an explosion and
game-over for the player. Murphy can push Zonks laterally (but not vertically)
if there is space for them to move, but can only push one Zonk at a time. Good
timing is needed to use Zonks strategically, such as dropping them on top of
enemies (like Snik-snaks) to eliminate them through explosions.
```

---

## Llama Stack

* Shrnutí

---

### ✅ Pro

* Relativně dobře promyšlená technologie
    - vše řízeno konfiguračním souborem
* Do značné míry nezávislá na klientských aplikacích
* Potenciál pro vznik dalších poskytovatelů (providers)
    - event-driven přístup(?)

---

### ❌ Proti

* Nestabilita celé platformy (konfigurace, API, poskytovatelé)
* Poměrně strohá dokumentace, příklady použití atd.
* Poměrně značné množství chyb a regresí

---

![Langchain logo](images/langchain.png)

---

### Langchain

* Framework pro GenAI a Python
* Chatboti
* RAG
* Paměť konverzací
* Shrnutí konverzací
* Generování syntetických dat

---

### Langchain

* Jednoduché úkoly je možné řešit jednoduše
* Mnohdy pouze několikařádkové skripty

---

### Získání odpovědi z LLM

@ openai_query.py

---

```text
content='Hi! How can I assist you today?'
additional_kwargs={'refusal': None}
response_metadata={
    'token_usage': {'completion_tokens': 9, 'prompt_tokens': 9, 'total_tokens': 18, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
    'model_provider': 'openai',
    'model_name': 'gpt-4o-mini-2024-07-18',
    'system_fingerprint': 'fp_373a14eb6f',
    'id': 'chatcmpl-DCUolN2ELURIoXdSt7YNoBbWbCiy4',
    'service_tier': 'default',
    'finish_reason': 'stop',
    'logprobs': None
}
id='lc_run--019c8bba-55c1-70e3-bd12-993701b96a2b-0'
tool_calls=[]
invalid_tool_calls=[]
usage_metadata={'input_tokens': 9, 'output_tokens': 9, 'total_tokens': 18, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
```

---

### Nastavení parametrů posílaných do LLM

@ temperature.py

---

### Šablona pro posílané dotazy

@ prompt.py

---

```text
{'language': 'Czech',
 'text': 'In Czech, you can say \'hi\' by using the word "Ahoj."
 Another more formal way to greet someone is "Dobrý den,"
 which means "Good day."'
}
```

---

### Řetězce (chains)

@ prompt2.py

---

### Operátor "kolony"

@ chain.py

---

### Paměť s konverzací

@ context.py

---

### Zjištění počtu tokenů

@ tokens1.py

---

### Zprávy posílané člověkem vs zprávy od AI

@ tokens2.py

---

### Zpracování dokumentů (RAG atd.)

* document loaders
* text splitters
* embedding

---

### Načtení textového dokumentu

@ text_loader_1.py

---

### Načtení dokumentu z Webu

@ web_based_loader.py

---

### Chunking

@ text_splitter_1.py

---

### Nastavení oblasti překryvu

@ text_splitter_2.py

---

### Embedding

---

@ embeddings_1.py

---

```text
SentenceTransformer(
  (0): Transformer({'max_seq_length': 128, 'do_lower_case': False, 'architecture': 'BertModel'})
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
)
Embeddings shape: (384,)
<class 'numpy.ndarray'> (384,)
```

---

@ embeddings_2.py

---

```text
SentenceTransformer(
  (0): Transformer({'max_seq_length': 128, 'do_lower_case': False, 'architecture': 'BertModel'})
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
)
Embeddings shape: (7, 384)
<class 'numpy.ndarray'> (384,)
<class 'numpy.ndarray'> (384,)
<class 'numpy.ndarray'> (384,)
<class 'numpy.ndarray'> (384,)
<class 'numpy.ndarray'> (384,)
<class 'numpy.ndarray'> (384,)
<class 'numpy.ndarray'> (384,)
```

---

@ embeddings_3.py

---

```text
SentenceTransformer(
  (0): Transformer({'max_seq_length': 128, 'do_lower_case': False, 'architecture': 'BertModel'})
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
)
Embeddings shape: (6, 384)
[[ 0.34784642  0.16516836  0.8089123  ...  0.3040554  -0.03139809
   0.01735951]
 [ 0.16027431 -0.47784272  0.14267115 ...  0.35347047  0.09468529
   0.16065338]
 [ 0.6181423  -0.24776635 -0.23564625 ...  0.17215669  1.1165967
   0.63950485]
 [ 0.6088224   0.58308387  0.40460858 ...  0.08260158  0.81306946
   0.16788094]
 [ 0.11015982  0.10045858 -0.24472675 ... -0.06199183  0.46151292
  -0.12090201]
 [ 0.15316603 -0.05734093 -0.276057   ...  0.01458577  0.24355118
  -0.44814664]]
tensor([[ 1.0000,  0.0134, -0.0661,  0.0697,  0.0171,  0.0515],
        [ 0.0134,  1.0000, -0.0014, -0.0654, -0.0510,  0.0028],
        [-0.0661, -0.0014,  1.0000, -0.1279, -0.0577,  0.3191],
        [ 0.0697, -0.0654, -0.1279,  1.0000,  0.1503, -0.0457],
        [ 0.0171, -0.0510, -0.0577,  0.1503,  1.0000, -0.0364],
        [ 0.0515,  0.0028,  0.3191, -0.0457, -0.0364,  1.0000]])
```

---

@ embeddings_4.py

---

```text
SentenceTransformer(
  (0): Transformer({'max_seq_length': 128, 'do_lower_case': False, 'architecture': 'BertModel'})
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
)
Embeddings shape: (7, 384)
Index: 7
----------------------------------------
Query: What is your age?
Most 3 similar sentences:
1: How old are you? (Distance: 13.968358993530273)
2: To be or not to be, that is the question (Distance: 69.80448913574219)
3: The tesselated polygon is a special type of polygon (Distance: 92.1417007446289)
```

---
