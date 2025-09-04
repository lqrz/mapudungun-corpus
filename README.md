# Mapudungun corpus

This repository contains the cleaned version of the Mapudungun dataset collected for the AVENUE project by CMU, the Chilean Ministry of Education, and the Instituto de Estudios Indígenas at Universidad de La Frontera.

You can download the raw audio data for all files from [here](http://tts.speech.cs.cmu.edu/mapudungun/AUDIO.zip).

---
# Usage

Run the `clean_transcriptions.py` script inside `src/data_cleaning`.

```bash
python clean_transcriptions.py data/raw/transcriptions data/cleaned/transcriptions
```

---

# Citation

If you use the original raw data, please use the following citation:
~~~
@dataset{mapudungun,
	title={Mapudungun Speech Corpus},
	author={Luis Caniupil, Flor Caniupil; Héctor Painequeo; Rosendo Huisca; Hugo Carrasco; Rodolfo M Vega; Lori Levin; Jaime Carbonell}
}
~~~

If you use the cleaned dataset or if you compare to our baseline results, please use the following citation:
~~~
@misc{duan2019mapudungun,
	author={Mingjun Duan, Carlos Fasola, Sai Krishna Rallabandi, Rodolfo M. Vega, Antonios Anastasopoulos, Lori Levin, and Alan W Black}
	title={A Resource for Computational Experiments on Mapudungun},
	note={preprint},
	year={2019}
}
~~~


