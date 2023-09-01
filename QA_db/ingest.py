"""This is the logic for ingesting Notion data into LangChain."""
import pathlib
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
import faiss
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import pickle
from langchain.document_loaders import WebBaseLoader
print ("testtest")

# Here we load in the data in the format that Notion exports it in.
# ps = list(pathlib.Path("Notion_DB/").glob("**/*.md"))
# s123Docs = ['https://doc.arcgis.com/en/survey123/desktop/create-surveys/createsurveys.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/styleyourform.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/previewyourform.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/publishsurvey.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/updatesurvey.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/sharesurvey.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/includemap.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/decimaldatetime.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/xlsformessentials.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/xlsformsettings.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/xlsformsappearance.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/range.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/xlsformnotes.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/geopoints.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/geotracegeoshape.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/xlsformrepeats.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/xlsformcascadingselects.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/xlsformformulas.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/xlsformexpressions.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/xlsforminstancename.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/xlsformmedia.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/barcodes.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/imagemap.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/prepopulateanswers.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/esricustomcolumns.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/pulldatajavascript.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/watermarks.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/xlsformparameters.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/xlsformmultiplelanguagesupport.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/preparebasemaps.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/prepareforediting.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/survey123withexistingfeatureservices.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/webhooks.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/locationsharing.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/high-accuracy-prep.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/rangefinders-prep.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/smart-assistants-prep.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/drawannotatepalettes.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/connecttools.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/quickreferencecreatesurveys.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/troubleshootcreatesurveys.htm', 'https://doc.arcgis.com/en/survey123/desktop/create-surveys/knownissuescreatesurveys.htm', 'https://doc.arcgis.com/en/survey123/browser/create-surveys/createsurveys.htm', 'https://doc.arcgis.com/en/survey123/browser/create-surveys/styleyourform.htm', 'https://doc.arcgis.com/en/survey123/browser/create-surveys/previewyourform.htm', 'https://doc.arcgis.com/en/survey123/browser/create-surveys/publishsurvey.htm', 'https://doc.arcgis.com/en/survey123/browser/create-surveys/updatesurvey.htm', 'https://doc.arcgis.com/en/survey123/browser/create-surveys/sharesurvey.htm', 'https://doc.arcgis.com/en/survey123/browser/create-surveys/includemap.htm', 'https://doc.arcgis.com/en/survey123/browser/create-surveys/decimaldatetime.htm', 'https://doc.arcgis.com/en/survey123/browser/create-surveys/webdesigneressentials.htm', 'https://doc.arcgis.com/en/survey123/browser/create-surveys/range.htm', 'https://doc.arcgis.com/en/survey123/browser/create-surveys/xlsformmultiplelanguagesupport.htm', 'https://doc.arcgis.com/en/survey123/browser/create-surveys/webhooks.htm', 'https://doc.arcgis.com/en/survey123/browser/create-surveys/versioncontrol.htm', 'https://doc.arcgis.com/en/survey123/browser/create-surveys/locationsharing.htm', 'https://doc.arcgis.com/en/survey123/browser/create-surveys/quickreferencecreatesurveys.htm', 'https://doc.arcgis.com/en/survey123/browser/create-surveys/knownissuescreatesurveys.htm', 'https://doc.arcgis.com/en/survey123/reference/whatissurvey123.htm', 'https://doc.arcgis.com/en/survey123/reference/installsurvey123.htm', 'https://doc.arcgis.com/en/survey123/reference/integratewithotherapps.htm', 'https://doc.arcgis.com/en/survey123/reference/external-hardware.htm', 'https://doc.arcgis.com/en/survey123/reference/smartassistants.htm', 'https://doc.arcgis.com/en/survey123/reference/survey123withenterprise.htm', 'https://doc.arcgis.com/en/survey123/reference/formappcomparision.htm', 'https://doc.arcgis.com/en/survey123/reference/security.htm', 'https://doc.arcgis.com/en/survey123/reference/organizationsettings.htm', 'https://doc.arcgis.com/en/survey123/reference/enterpriseproperties.htm', 'https://doc.arcgis.com/en/survey123/reference/apiextensibility.htm', 'https://doc.arcgis.com/en/survey123/desktop/get-answers/opensurvey.htm', 'https://doc.arcgis.com/en/survey123/desktop/get-answers/submitsurveyresults.htm', 'https://doc.arcgis.com/en/survey123/desktop/get-answers/editexistingdata.htm', 'https://doc.arcgis.com/en/survey123/desktop/get-answers/capturegeometry.htm', 'https://doc.arcgis.com/en/survey123/desktop/get-answers/drawannotate.htm', 'https://doc.arcgis.com/en/survey123/desktop/get-answers/useofflinebasemaps.htm', 'https://doc.arcgis.com/en/survey123/desktop/get-answers/high-accuracy-use.htm', 'https://doc.arcgis.com/en/survey123/desktop/get-answers/rangefinders-use.htm', 'https://doc.arcgis.com/en/survey123/desktop/get-answers/measurewithspike.htm', 'https://doc.arcgis.com/en/survey123/desktop/get-answers/smart-assistants-use.htm', 'https://doc.arcgis.com/en/survey123/desktop/get-answers/quickreferencegetanswers.htm', 'https://doc.arcgis.com/en/survey123/desktop/get-answers/troubleshootgetanswers.htm', 'https://doc.arcgis.com/en/survey123/desktop/get-answers/knownissuesgetanswers.htm', 'https://doc.arcgis.com/en/survey123/browser/get-answers/opensurvey.htm', 'https://doc.arcgis.com/en/survey123/browser/get-answers/submitsurveyresults.htm', 'https://doc.arcgis.com/en/survey123/browser/get-answers/editexistingdata.htm', 'https://doc.arcgis.com/en/survey123/browser/get-answers/capturegeometry.htm', 'https://doc.arcgis.com/en/survey123/browser/get-answers/knownissuesgetanswers.htm', 'https://doc.arcgis.com/en/survey123/browser/analyze-results/viewresults.htm', 'https://doc.arcgis.com/en/survey123/browser/analyze-results/trackingsurveys.htm', 'https://doc.arcgis.com/en/survey123/browser/analyze-results/sharesurveyresults.htm', 'https://doc.arcgis.com/en/survey123/browser/analyze-results/printsurveyresults.htm', 'https://doc.arcgis.com/en/survey123/browser/analyze-results/featurereporttemplates.htm', 'https://doc.arcgis.com/en/survey123/browser/analyze-results/featurereportqueries.htm', 'https://doc.arcgis.com/en/survey123/browser/analyze-results/knownissuesanalyzeresults.htm', 'https://doc.arcgis.com/en/survey123/browser/analyze-results/troubleshootanalyzeresults.htm', 'https://doc.arcgis.com/en/survey123/faq/faqgeneral.htm', 'https://doc.arcgis.com/en/survey123/faq/faqcreatesurveys.htm', 'https://doc.arcgis.com/en/survey123/faq/faqgetanswers.htm', 'https://doc.arcgis.com/en/survey123/faq/faqanalyzeresults.htm', 'https://doc.arcgis.com/en/survey123/faq/whatsnewsurvey123.htm', 'https://doc.arcgis.com/en/survey123/faq/sneakpeek.htm', 'https://doc.arcgis.com/en/survey123/faq/systemrequirements.htm']
s123Docs = ['https://doc.arcgis.com/en/survey123/browser/analyze-results/featurereporttemplates.htm', 'https://doc.arcgis.com/en/survey123/browser/analyze-results/featurereportqueries.htm', 'https://doc.arcgis.com/en/survey123/browser/analyze-results/printsurveyresults.htm', 'https://doc.arcgis.com/en/survey123/browser/analyze-results/knownissuesanalyzeresults.htm']
loader = WebBaseLoader(s123Docs)

data = loader.load()


""" data = []
sources = []
for p in ps:
    with open(p) as f:
        data.append(f.read())
    sources.append(p)  """
    

# Here we split the documents, as needed, into smaller chunks.
# We do this due to the context limits of the LLMs.
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 256,
    chunk_overlap  = 20,
    length_function = len
)
docs = text_splitter.split_documents(data)
embeddings = OpenAIEmbeddings()
store = FAISS.from_documents(docs, embeddings)

""" docs = []
metadatas = []
for i, d in enumerate(data):
    splits = text_splitter.split_text(d)
    docs.extend(splits)
    metadatas.extend([{"source": sources[i]}] * len(splits)) """


# Here we create a vector store from the documents and save it to disk.
# store = FAISS.from_texts(docs, OpenAIEmbeddings())
faiss.write_index(store.index, "docs.index")
store.index = None
with open("faiss_store.pkl", "wb") as f:
    pickle.dump(store, f)
