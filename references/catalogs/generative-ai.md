# Generative AI Nodes

## Hugging Face
- **Hugging Face Custom Category Sentiment Analysis** `13-Generative-AI/01-Hugging-Face/hf_custom_categories_sentiment_analysis.json` — Sentiment Analysis with custom categories using models hosted in Hugging Face repository.
- **Hugging Face Grammatical Correctness** `13-Generative-AI/01-Hugging-Face/hf_grammatical_correctness.json` — Grammatical Correctness using models hosted in Hugging Face repository.
- **Hugging Face Natural Language Inference** `13-Generative-AI/01-Hugging-Face/hf_natural_language_inference.json` — Natural Language Inference using models hosted in Hugging Face repository.
- **Hugging Face Question Natural Language Inference** `13-Generative-AI/01-Hugging-Face/hf_question_natural_language_inference.json` — Question Natural Language Inference using models hosted in Hugging Face repository.
- **Hugging Face Sentiment Analysis** `13-Generative-AI/01-Hugging-Face/hf_sentiment_analysis.json` — Sentiment Analysis using models hosted in Hugging Face repository.
- **Hugging Face Summarization** `13-Generative-AI/01-Hugging-Face/hf_summarization.json` — Summarization using models hosted in Hugging Face repository.
- **Hugging Face Tone Analysis** `13-Generative-AI/01-Hugging-Face/hf_tone_analysis.json` — Tone Analysis using models hosted in Hugging Face repository.

## Ingestion
- **Confluence Reader** `13-Generative-AI/02-Ingestion/confluence_node.json` — Executes the Confluence Reader operation.
- **Document To Text** `13-Generative-AI/02-Ingestion/document_to_text.json` — The DocumentToText node extracts text content from documents, including PDF, TXT, DOCX, and image files, located in a specified file path or directory.
- **Service Now Data Extraction** `13-Generative-AI/02-Ingestion/servicenow_data_extraction_node.json` — Processes It wont take any input, as this will be the 1st node in the workflow data.
- **Sharepoint Data Extraction** `13-Generative-AI/02-Ingestion/sharepoint_node.json` — Retrieves files and pages from a SharePoint site, extracts their content (e.
- **Audio Diarization** `13-Generative-AI/02-Ingestion/speech_to_text.json` — This node processes audio files to transcribe and diarize speech, identifying different speakers in the audio.
- **Video Summarization** `13-Generative-AI/02-Ingestion/video_summary.json` — This process involves creating text summary for the video.
- **Web Scraper** `13-Generative-AI/02-Ingestion/web_scrapper.json` — Scrapes Webpages.

## Vectorization
- **Azure AI Search Upsert** `13-Generative-AI/03-Vectorization/azure_ai_search_upsert.json` — This process involves indexing document embeddings into Azure AI Search for efficient vector-based similarity search and retrieval.
- **Save Chroma DB** `13-Generative-AI/03-Vectorization/save_to_chroma.json` — Save Vector Embeddings to Chroma DB.
- **Save Faiss DB** `13-Generative-AI/03-Vectorization/save_to_faiss.json` — Save Vector Embeddings to faiss db.
- **Save to Pinecone** `13-Generative-AI/03-Vectorization/save_to_pinecone.json` — This process involves storing document embeddings in a Pinecone vector database for efficient similarity search and retrieval.
- **Create Text Embedding** `13-Generative-AI/03-Vectorization/text_embedder.json` — This node enables the creation of a embedding text data and output as dataframe.

## Retrieval
- **Azure AI Search Retrieve** `13-Generative-AI/04-Retrieval/azure_ai_search_retrieve.json` — Retrieve the most relevant knowledge from Azure AI Search using vector, keyword, or hybrid retrieval.
- **Read Chroma DB** `13-Generative-AI/04-Retrieval/read_from_chroma_db.json` — Read Vector Embeddings from Chroma DB Collection gives user query.
- **Read Faiss DB** `13-Generative-AI/04-Retrieval/read_from_faiss_db.json` — Read Vector Embeddings, from faiss db.
- **Read Pinecone DB** `13-Generative-AI/04-Retrieval/read_from_pinecone_db.json` — Read Vector Embeddings from Pinecone db.

## LLM Inference
- **Interactive LLM Agent** `13-Generative-AI/05-LLM-Inference/interactive_llm_agent.json` — This node enables standalone or dataframe-optional LLM queries across multiple providers (OpenAI, Bedrock, Gemini).
- **Invoice Extraction** `13-Generative-AI/05-LLM-Inference/invoice_extraction.json` — Processes It may take in Dataframe as an input data.
- ** Multi LLM Query** `13-Generative-AI/05-LLM-Inference/multi_llm_query.json` — The Multi LLM Query node is designed to query multiple large language models (LLMs) from providers such as OpenAI, Bedrock, and Gemini, using a DataFrame as input.
- **Output Formatter** `13-Generative-AI/05-LLM-Inference/output_formatter.json` — This node formats output from Columns.
- **SerperAI Search** `13-Generative-AI/05-LLM-Inference/serper_api.json` — The SerperAI Search node fetches real-time search results from Google services (Web, News, Images, Shopping, Places) using the SerperAI API.
- **Text Analysis** `13-Generative-AI/05-LLM-Inference/text_analysis.json` — Reads It takes directory or path as an input and produces Outputs a Dataframe with 2 columns speaker and dialouge.
