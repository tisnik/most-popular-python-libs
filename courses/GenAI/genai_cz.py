# # GenAI a Python
# 
# ![Python](images/python.png)
# 
# Pavel Tišnovský,
# tisnik@centrum.cz
# 
# ---
# 
# ## Obsah
# 
# * Teoretická část
#     - Strojové učení a umělá inteligence
#     - Modely, trénink, vyhodnocování
#     - Neuronové sítě
#     - Generativní umělá inteligence
#     - Frameworky pro GenAI
#     - Základní vlastnosti LLM
#     - OpenAI a další standardizovaná API
#     - Framework Llama Stack
#     - Langchain pro tvorbu aplikací využívajících GenAI
#     - RAG (Retrieval-augmented generation)
# * Praktická část
#     - Volání LLM
#     - Langchain
#     - Tokenizace textu
#     - Tvorba embedded modelů
#     - Vyhledávání založené na podobnosti vektorů
#     - PgVector
#     - FAISS
#     - Evaluace
# 
# ---
#
# # Úvod
# 
# * Umělá inteligence
# * Vývoj umělé inteligence
# * Strojové učení
# * Vztah strojového učení a umělé inteligence
# 
# ---
# 
# ### Umělá inteligence
# 
# * Definice
#     - konstrukce strojů, které dokážou provádět činnosti vyžadující inteligenci, pokud by byly prováděny lidmi (Marvin Minsky, 1967)
#     - existují ovšem i alternativní definice
# * Modelování lidské mysli
#     - shora dolů (psychologie)
#     - zdola nahoru (neurověda)
#     - zprostředka (informatika)
# * Inteligentní chování může vzniknout ze spojení velkého množství jednoduchých systémů
#     - koncept neuronových sítí
# 
# ---
# 
# ## Vývoj umělé inteligence
# 
# * 1943-1955
#     - první myšlenky, že něco podobného může reálně vzniknout
#     - booleovský model neuronu
#     - A. Turing
#         - Computing Machinery and Intelligence
# * 1956
#     - McCarthy (LISP)
#     - (pravděpodobně) poprvé použil termín AI
#     - Newel a Simon: Logic theorist
# * velké očekávání pokroku v dalších letech
#     - dařilo se částečné řešení různých problémů
#     - prakticky každý měsíc nový objev
# * cca 1965
#     - vystřízlivění
#     - existovala sice spousta vyřešených problémů, ale ty byly triviální
#     - nalezeny limity, které se nedařilo překonat
#     - první "AI zima"
# * sedmdesátá léta
#     - systémy založené na znalostech
#     - vývoj v mnoha oblastech (hledání ropy atd.)
# * začátek osmdesátých let
#     - velké investice do AI
#     - očekávání se nenaplnila
#     - potom nastává druhá "AI zima"
# * druhá polovina osmdesátých let
#     - rozvoj neuronových sítí (což nebyla novinka)
# * 1995
#     - systémy SOAR (State, Operator and Result)
# * 2000
#     - big data (v tom pokračujeme i dnes)
#     - ale prozatím žádné větší objemy
#     - "wow" efekt na úrovni AI
# * 2010
#     - deep learning
# * 2020
#     - LLM (prompt engineering, ne fine tuning)
# * současnost
#     - LLM
#     - generativní AI
# 
# ---
# 
# ## Strojové učení
# 
# * podoblast umělé inteligence
# * změna interního stavu systému při tréninku
# * několik způsobů realizace strojového učení
# * "statistické učení"
# * typicky se nejedná o plně automatizovanou činnost
#     - vyžaduje chytrá (strategická) rozhodnutí
#     - výběr modelu
#     - výběr hyperparametrů modelu
#     - rozdělení vstupních dat
#     - filtrace dat
# * nalézají se skryté vzorky a vazby v datech
# 
# ---
# 
# ## Vztah strojového učení a umělé inteligence
# 
# ![vztah.png](images/ai_ml_dl.png)
# 
# * Umělá inteligence (AI)
#     - strojové učení (machine learning, ML)
#     - hluboké učení (deep learning, DL)
#     - robotika
#     - neuronové sítě (NN)
#     - zpracování přirozeného jazyka (NLP)
# * AI > ML > NN > DL
# 
# * Umělá inteligence
#     - objevování
#     - odvozování
#     - odůvodnění
# * Strojové učení
#     - (sofistikovaná) analýza
#     - predikce (!)
#     - rozhodování (klasifikace nebo regrese)
# 
# ---
# 
# ### Proč strojové učení?
# 
# * Chceme, aby se stroj naučil řešit zadaný problém na základě vzorových řešení:
#     - řešení je příliš komplikované
#     - problém se často mění, vyvíjí
#     - lidská práce je drahá (v porovnání se strojovou)
#     - máme k dispozici tolik dat, že je není možné zpracovat "ručně"
# 
# ---
# 
# ### Typické aplikace strojového učení
# 
# * Rozpoznávání vzorů
#     - věci/osoby/výrazy tváře na fotkách
#     - mluvená slova
#     - spam
#     - medicínská diagnóza
# * Rozpoznávání anomálií
#     - netypické sekvence finančních transakcí
#     - netypická data přicházející ze senzorů v atomové elektrárně
# * Předpovídání
#     - vývoj ceny akcií na burze / vývoj měnového kurzu
#     - jaké filmy bude mít daný člověk rád
#     - věk osoby na fotografii
# * Shlukování
#     - vyhledávání zpráv s podobným obsahem
#     - vyhledání skupin zákazníků s podobnými vlastnostmi
# 
# ---
# 
# ## Základní pojmy
# 
# * Datová sada
#     - trénovací data
#     - testovací data
# 
# ![dataset.png](images/dataset.png)
# 
# ---
# 
# ### Techniky strojového učení
# 
# * Supervised learning
#     - také se nazývá "predictive modeling"
#     - známe takzvané "kategorie" neboli odpovědi
# * Unsupervised learning
#     - neznáme odpovědi
#     - model musí najít struktury/vzory v datech
#     - typicky různé varianty clusteringu
# 
# ![ml.png](images/ml.png)
# 
# ---
# 
# ### Supervised learning
# 
# 1. trénink na základě vstupních dat
#     - model se naučí vztahy mezi daty a očekávanou odpovědí
# 2. predikce na základě jiných(!) dat
#     - problematika rozdělení dat
# 3. výsledky
#     - klasifikace: koupí si A, B nebo C?
#     - regrese: vektor příznaků, numerická hodnota nebo hodnoty
# 
# ---
# 
# ### Unsupervised learning
# 
# 1. trénink modelu na základě vstupních dat
#     - ovšem bez znalosti správných odpovědí
# 2. shluková analýza
# 3. latentní a faktorová analýza
# 
# ---
# 
# ### Další možnosti
# 
# 1. kombinace obou metod (bez/s učitelem)
# 2. učení se zpětnou vazbou
#     - pasivní
#     - aktivní
# 
# ---
# 
# ### Modely strojového učení
# 
# * ANN
# * Desicion trees
# * Support-vector machine
# * Regresní analýza
# * Bayesovské sítě
# * Genetické algoritmy
# * Neuronové sítě
# 
# ---
# 
# ### Jak začít?
# 
# 1. jaké atributy použít z dat?
# 2. jaký model vybrat
# 3. jak optimalizovat pro větší výkon
# 4. jak vytvořit model, který bude vhodný pro pro něj neznámá data?
# 5. jak odhadnout vhodnost modelu pro neznámá data?
# 
# ---
# 
# ### Komprimace dat
# * souvislost mezi ML a komprimací dat
# * predikce
# * tzv. optimální komprese
#     - při predikci lze použít aritmetické kódování
# 
# ---
# 
# ### Redukce dat
# 
# ![reduction.png](images/reduction.png)
# 
# ---
# 
# ### Redukce dat
# 
# ![reduction_supervised.png](images/reduction_supervised.png)
# 
# ---
# 
# ### Nedoučení a přeučení
# 
# * Nedoučení
#     - malá sada dat, na kterých je model trénován
#     - příliš složitý model
#     - data reprezentují pouze malý vzorek celého spektra hodnot
# * Přeučení
#     - velká vazba na trénovací data
#     - menší flexibilita práce s daty, která model nezná
#     - použití polynomu vyššího stupně, když by stačila lineární regrese
# 
# ---
# 
# ### Přeučení
# 
# ![overtrain.png](images/overtraining.png)
# 
# ---
# 
# ### Úspěšnost modelu
# 
# * Pro zcela nová (neznámá) data!
#     - ne pro trénovací množinu
#     - častá chyba
# 
# ---
# 
# ### Křížová validace (cross validation)
# 
# * rozdělení dat do bloků
#     - například na 1/10
#     - 9/10 pro trénink
#     - 1/10 pro otestování
# 
# ---
#
# ## Neuronové sítě
#
# ---
#
# # Generativní AI
#
# ![LS](images/lsc.jpg)
#
# ---
#
# ## Frameworky pro GenAI
# * langchain
# * langgraph
# * autogen
# * metaGPT
# * phidata
# * CrewAI
# * pydanticAI
# * controlflow
# * langflow
# * LiteLLM (???)
# * Llama Stack
# 
# ---
# 
# ## Potřebujeme sofistikované frameworky?
# * některé základní operace je možné provést i jen s využitím "pouhých" knihoven
# * příkladem může být knihovna OpenAI
# * a do určité míry taktéž LiteLLM

# Výpis všech dostupných modelů

from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
models = client.models.list()

for model in models:
    print(model.id)

# ---
# 
# ## Potřebujeme sofistikované frameworky?
# 
# * Kvóty
# * Konverzace
# * Kontext
# * Guardrails
# * RAG
# * BYOK
# * MCP
# * Agenti
# * A2A
# 
# ---
# 
# ## Llama Stack
# 
# ![Llama Stack logo](images/llama_stack_logo.png)
# 
# ---
# 
# ## Co je to Llama Stack?
# 
# * Framework pro tvorbu aplikací s AI
#     - chat boti
#     - obecně generativní AI (GenAI)
#     - trénink, evaluace
# * Skutečný framework nezávislý na programovacím jazyku
#     - systém providerů
#     - RAG, správa kvóty, guardrails, metriky atd.
# 
# ---
# 
# ### Nejjednodušší využití Llama Stacku
# 
# * Volání LLM
# * Zpracování odpovědi od LLM
# * "chatbot v.0.0.1"
# 
# ---
# 
# ### Skutečné požadavky jsou však širší
# 
# * Podpora RAG
# * Historie konverzace
# * Rozvětvení konverzace
# * Zapamatování fakt o uživateli
# * Volání MCP
# * Kvóty
# * Kontrola dotazů a odpovědí
# * Volání více LLM, evaluace odpovědí atd.
# 
# ---
# 
# ### API a poskytovatelé
# 
# * Plně konfigurovatelné
# * Lze získat seznam dostupných API
# * Taktéž lze získat seznam dostupných poskytovatelů
# * Pozor: závislosti vyžadované jednotlivými poskytovateli
# 
# ---
# 
# ![Providers](images/llama_stack_providers.png)
# 
# ### Poskytovatelé
#
# * Agents
#     - interakce se systémem agentů (samotní agenti mohou provádět různé operace)
# * Inference
#     - rozhraní k&nbsp;LLM modelům i k embedding modelům
# * VectorIO
#     - původně rozhraní kvektorovým databázím (hledání podobných vektorů)
#     - nyní i fulltext hledání
# * Safety
#     - detekce dotazů s nevhodným či nepovoleným obsahem apod.
# * Telemetry
#     - telemetrie
#     - OpenTelemetry ale i další
# * Eval
#     - vyhodnocování odpovědí modelů atd.
# * DatasetIO
#     - čtení a zápisy datových sad z/do zvoleného systému
#     - může být i lokální souborový systém
#
# ---
#
# ### Současná situace okolo Llama Stacku
#
# * Meta -> vLLM
# * Zaměření na kompatibilitu s Responses API (OpenAI)
# * Podpora pro agentic flow (ovšem jen základní)
# * Postupně se některé další funkce odstraňují (!)
# * Výsledkem je nestabilita celé platformy
# * Pokud vyvíjíte stabilní projekt, je Llama Stack riziko
#

