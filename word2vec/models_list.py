import gensim.downloader as downloader
 
# výpis existujících modelů
for model_name, info in downloader.info()['models'].items():
    print(f"{model_name}: {info['description'][:80]}...")
