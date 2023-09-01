# Test for embedding DB for Survey123 doc

## Steps:

### Environment set up:
- Create env: conda create --name qabot
- Activate env: conda activate qabot
- Install python3：conda install python=3
- Install streamlit: pip install streamlit
- Install requirements：pip install -r requirements.txt
- set OPENAI_API_KEY=<>
- Install missing libs: pip install unstructured
### Ingest docs
- python ingest.py
### Local QA test
- python qa.py "what is the feature report?"
### Start stremlit UI
- python -m streamlit run Home.py (Can't work with proxy, need to access the internet)

### Test app host on VM
http://dev0028317.esri.com:8501
